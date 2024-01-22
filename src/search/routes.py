import openai
from fastapi import APIRouter, Depends
from llama_index import SQLDatabase
from llama_index.indices.struct_store import NLSQLTableQueryEngine
from sqlalchemy import create_engine
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
    # response_model=SearchResponse,
)
async def search(
    request: SearchRequest,
    # db_session: AsyncSession = Depends(get_db_session),
):
    engine = create_engine(current_config.SQLALCHEMY_DATABASE_URI)
    sql_database = SQLDatabase(engine, include_tables=["loans", "clients", "branches", "pledges"])
    query_engine = NLSQLTableQueryEngine(sql_database)
    response = query_engine.query("Какой не закрытый большой займ есть")
    return {"Hello": str(response)}
