from __future__ import annotations
from typing import Any, Literal, Optional
from pydantic import BaseModel, Field, HttpUrl, field_validator, model_validator


class Actor(BaseModel):
    name: str
    surname: str = ""


class Writer(BaseModel):
    name: str
    surname: str = ""


def _split_full_name(full: str) -> tuple[str, str]:
    full = (full or "").strip()
    if not full:
        return "", ""
    parts = full.split()
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], " ".join(parts[1:])


def _parse_runtime_to_minutes(runtime: Any) -> int:

    if runtime is None:
        return 0
    if isinstance(runtime, int):
        return runtime
    s = str(runtime).strip().lower()
    digits = "".join(ch for ch in s if ch.isdigit())
    return int(digits) if digits else 0


def _parse_votes(v: Any) -> Optional[int]:
    if v is None or v == "":
        return None
    if isinstance(v, int):
        return v
    s = str(v).strip().replace(",", "")
    if not s.isdigit():
        return None
    return int(s)


class Film(BaseModel):
    imdbID: str = Field(..., min_length=3)
    Title: str
    Year: int
    Rated: str
    Runtime: str  
    Genre: str
    Language: str
    Country: str
    Plot: str


    Actors: list[Actor]
    Writer: list[Writer]

    type: Literal["movie", "series"] = "movie"
    imdbRating: Optional[float] = None
    imdbVotes: Optional[int] = None
    Images: list[HttpUrl] = Field(default_factory=list)

    runtimeMinutes: int = 0

    @field_validator("Actors", mode="before")
    @classmethod
    def parse_actors(cls, v: Any) -> list[Actor]:
        if v is None:
            return []
        if isinstance(v, list):
            out: list[Actor] = []
            for item in v:
                if isinstance(item, Actor):
                    out.append(item)
                elif isinstance(item, dict):
                    out.append(Actor(**item))
                else:
                    name, surname = _split_full_name(str(item))
                    out.append(Actor(name=name, surname=surname))
            return out

        s = str(v)
        parts = [p.strip() for p in s.split(",") if p.strip()]
        out: list[Actor] = []
        for p in parts:
            name, surname = _split_full_name(p)
            out.append(Actor(name=name, surname=surname))
        return out

    @field_validator("Writer", mode="before")
    @classmethod
    def parse_writers(cls, v: Any) -> list[Writer]:
        if v is None:
            return []
        if isinstance(v, list):
            out: list[Writer] = []
            for item in v:
                if isinstance(item, Writer):
                    out.append(item)
                elif isinstance(item, dict):
                    out.append(Writer(**item))
                else:
                    name, surname = _split_full_name(str(item))
                    out.append(Writer(name=name, surname=surname))
            return out

        s = str(v)
        parts = [p.strip() for p in s.split(",") if p.strip()]
        out: list[Writer] = []
        for p in parts:
            name, surname = _split_full_name(p)
            out.append(Writer(name=name, surname=surname))
        return out

    @field_validator("Images", mode="before")
    @classmethod
    def validate_images_list(cls, v: Any) -> Any:
        if v is None:
            return []
        if isinstance(v, str):
            return [v]
        return v

    @field_validator("Year")
    @classmethod
    def validate_year(cls, v: int) -> int:
        if v <= 1900:
            raise ValueError("Year mora biti veća od 1900.")
        return v

    @model_validator(mode="after")
    def validate_runtime_and_ratings(self) -> "Film":
        minutes = _parse_runtime_to_minutes(self.Runtime)
        if minutes <= 0:
            raise ValueError("Runtime mora biti veći od 0 (npr. '120 min').")
        self.runtimeMinutes = minutes

        if self.imdbRating is not None:
            if not (0.0 <= float(self.imdbRating) <= 10.0):
                raise ValueError("imdbRating mora biti između 0 i 10.")

        if self.imdbVotes is not None:
            if int(self.imdbVotes) <= 0:
                raise ValueError("imdbVotes mora biti veći od 0.")

        required_str_fields = ["Title", "Rated", "Runtime", "Genre", "Language", "Country", "Plot"]
        for f in required_str_fields:
            if not getattr(self, f, ""):
                raise ValueError(f"{f} je obavezno polje.")

        if not self.Actors:
            raise ValueError("Actors je obavezno polje (mora imati barem jednog glumca).")
        if not self.Writer:
            raise ValueError("Writer je obavezno polje (mora imati barem jednog autora).")

        return self




class FilmListResponse(BaseModel):
    total: int
    items: list[Film]
