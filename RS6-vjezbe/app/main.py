from __future__ import annotations
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import filmovi
from app.services.movies_store import MoviesStore


@asynccontextmanager
async def lifespan(app: FastAPI):
    store = MoviesStore()
    await store.load()

    app.state.store = store
    yield


app = FastAPI(
    title="Mikroservis Filmovi (FastAPI)",
    description="Mikroservis za dohvaćanje filmova iz JSON-a.",
    version="1.0.0",
    lifespan=lifespan,
)




def _get_store_from_state():
    return app.state.store

filmovi.get_store = _get_store_from_state 

app.include_router(filmovi.router)
