import openai
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from llama_index import SQLDatabase
from llama_index.core.response.schema import Response
from llama_index.indices.struct_store import NLSQLTableQueryEngine
from sqlalchemy import create_engine

from src.config import current_config
from src.dependencies import api_key_header
from src.search.schemas import SearchRequest, SearchResponse

router = APIRouter(
    prefix="/api/v1/search",
    tags=["search"],
)

openai.api_key = current_config.OPENAI_API_KEY


@router.post(
    "/",
    response_model=SearchResponse,
)
async def search(
    request: SearchRequest,
    api_key_header: APIKeyHeader = Depends(api_key_header),
):
    engine = create_engine(current_config.SQLALCHEMY_DATABASE_URI)
    sql_database = SQLDatabase(
        engine,
        include_tables=request.db_query_tables,
    )

    query_engine = NLSQLTableQueryEngine(sql_database)
    response = await query_engine.aquery(request.search_query)

    # specifically checking that it is Response from LLama Index
    if isinstance(response, Response):
        return {"search_response": response.response}

    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="service unavailable at the moment",
    )
