from fastapi import FastAPI
from fastapi.applications import AppType

from src.database.dependencies import DatabaseState


async def lifespan(current_app: AppType):
    current_app.state.database = DatabaseState()
    yield
    await current_app.state.database.dispose()


app = FastAPI(title="DatAI")


@app.get("/")
async def search():
    """This API returns search result over the database."""
    return {"message": "Hello World"}
