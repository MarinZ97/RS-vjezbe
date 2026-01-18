from __future__ import annotations
import json
from pathlib import Path
from typing import Any
import httpx
from fastapi import HTTPException
from app.core.config import MOVIES_JSON_URL, REQUEST_TIMEOUT_SECONDS
from app.models.film import Film, _parse_votes


DATA_FALLBACK_PATH = Path(__file__).resolve().parents[1] / "data" / "movies.json"


class MoviesStore:
    def __init__(self) -> None:
        self.movies: list[Film] = []

    async def load(self) -> None:
        raw = await self._load_raw_json()
        items = self._normalize_to_list(raw)

        movies: list[Film] = []
        errors: list[str] = []

        for idx, item in enumerate(items):
            try:
                if "imdbVotes" in item:
                    parsed = _parse_votes(item.get("imdbVotes"))
                    item["imdbVotes"] = parsed

                movies.append(Film.model_validate(item))
            except Exception as e:
                errors.append(f"Item #{idx}: {e}")

        if not movies:
            raise RuntimeError("Nijedan film nije uspješno učitan. Provjeri JSON i validaciju.")

        self.movies = movies


        if errors:

            pass

    async def _load_raw_json(self) -> Any:
        if MOVIES_JSON_URL and MOVIES_JSON_URL != "PASTE_JSON_URL_HERE":
            try:
                async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT_SECONDS) as client:
                    resp = await client.get(MOVIES_JSON_URL)
                    resp.raise_for_status()
                    return resp.json()
            except Exception:
                pass

        if not DATA_FALLBACK_PATH.exists():
            raise RuntimeError(
                "Ne mogu učitati JSON: URL nije postavljen iili ne radi, datoteka ne postoji: "
                f"{DATA_FALLBACK_PATH}"
            )
        return json.loads(DATA_FALLBACK_PATH.read_text(encoding="utf-8"))

    def _normalize_to_list(self, raw: Any) -> list[dict]:
        if isinstance(raw, list):
            return [x for x in raw if isinstance(x, dict)]
        if isinstance(raw, dict):
            for key in ("movies", "data", "items", "results"):
                if key in raw and isinstance(raw[key], list):
                    return [x for x in raw[key] if isinstance(x, dict)]
            if "imdbID" in raw and "Title" in raw:
                return [raw]
        raise RuntimeError("Nepoznat JSON format (nije lista filmova s ključem movies/data/items/results).")

    def get_by_imdb_id(self, imdb_id: str) -> Film:
        for m in self.movies:
            if m.imdbID.lower() == imdb_id.lower():
                return m
        raise HTTPException(status_code=404, detail=f"Film s imdbID='{imdb_id}' ne postoji.")

    def get_by_title(self, title: str) -> Film:
        t = title.strip().lower()
        for m in self.movies:
            if m.Title.strip().lower() == t:
                return m
        raise HTTPException(status_code=404, detail=f"Film s Title='{title}' ne postoji.")
