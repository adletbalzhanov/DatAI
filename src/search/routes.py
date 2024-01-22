import openai
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import current_config
from src.database.dependencies import get_db_session
from src.search.schemas import SearchRequest, SearchResponse

router = APIRouter(
    prefix="/api/v1/search",
    tags=["search"],
)

openai.api_key = current_config.OPENAI_API_KEY.get_secret_value()


@router.post(
    "/",
    response_model=SearchResponse,
)
async def search(
    request: SearchRequest,
    db_session: AsyncSession = Depends(get_db_session),
):
    sql_database = SQLDatabase(engine, include_tables=["loans", "clients", "branches", "pledges"])
    return {"Hello": "world"}
