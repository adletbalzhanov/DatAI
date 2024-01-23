from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.applications import AppType

from src.search.routes import router as search_router


@asynccontextmanager
async def lifespan(current_app: AppType):
    yield


fastapi_app = FastAPI(title="DatAI", lifespan=lifespan)

fastapi_app.include_router(search_router)
