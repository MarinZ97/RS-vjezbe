from __future__ import annotations
from typing import Literal, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from app.models.film import Film, FilmListResponse
from app.services.movies_store import MoviesStore
from fastapi import Request

router = APIRouter(prefix="/filmovi", tags=["Filmovi"])


def get_store(request: Request) -> MoviesStore:
    return request.app.state.store


@router.get("", response_model=FilmListResponse)
def get_all_movies(
    min_year: Optional[int] = Query(default=None, ge=1901, description="Minimalna godina (>= 1901)"),
    max_year: Optional[int] = Query(default=None, ge=1901, description="Maksimalna godina (>= 1901)"),
    min_rating: Optional[float] = Query(default=None, ge=0, le=10, description="Minimalni imdbRating (0-10)"),
    max_rating: Optional[float] = Query(default=None, ge=0, le=10, description="Maksimalni imdbRating (0-10)"),
    type: Optional[Literal["movie", "series"]] = Query(default=None, description="Tip: movie ili series"),
    store: MoviesStore = Depends(get_store),
) -> FilmListResponse:
    if min_year is not None and max_year is not None and min_year > max_year:
        raise HTTPException(status_code=422, detail="min_year ne može biti veći od max_year.")
    if min_rating is not None and max_rating is not None and min_rating > max_rating:
        raise HTTPException(status_code=422, detail="min_rating ne može biti veći od max_rating.")

    items = store.movies

    if type is not None:
        items = [m for m in items if m.type == type]

    if min_year is not None:
        items = [m for m in items if m.Year >= min_year]
    if max_year is not None:
        items = [m for m in items if m.Year <= max_year]

    if min_rating is not None:
        items = [m for m in items if (m.imdbRating is not None and m.imdbRating >= min_rating)]
    if max_rating is not None:
        items = [m for m in items if (m.imdbRating is not None and m.imdbRating <= max_rating)]

    return FilmListResponse(total=len(items), items=items)


@router.get("/{imdb_id}", response_model=Film)
def get_movie_by_imdb_id(imdb_id: str, store: MoviesStore = Depends(get_store)) -> Film:
    return store.get_by_imdb_id(imdb_id)


@router.get("/title/{title}", response_model=Film)
def get_movie_by_title(title: str, store: MoviesStore = Depends(get_store)) -> Film:
    return store.get_by_title(title)
