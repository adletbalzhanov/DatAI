import openai
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from llama_index import SQLDatabase
from llama_index.core.response.schema import Response
from llama_index.indices.struct_store import NLSQLTableQueryEngine
from sqlalchemy import create_engine

from src.config import current_config
from src.dependencies import api_key_header
from src.search.schemas import DBConfig, SearchRequest, SearchResponse

router = APIRouter(
    prefix="/api/v1/search",
    tags=["search"],
)

openai.api_key = current_config.OPENAI_API_KEY


def _create_database_uri(db_config: DBConfig) -> str:
    return (
        f"mysql+mysqlconnector://{db_config.user}:{db_config.password}"
        f"@{db_config.host}:{db_config.port}/{db_config.db}"
    )


@router.post(
    "/",
    response_model=SearchResponse,
)
async def search(
    request_payload: SearchRequest,
    api_key_header: APIKeyHeader = Depends(api_key_header),
):
    engine = create_engine(_create_database_uri(request_payload.db_config))
    sql_database = SQLDatabase(
        engine,
        include_tables=request_payload.db_query_tables,
    )

    query_engine = NLSQLTableQueryEngine(sql_database)
    response = await query_engine.aquery(request_payload.search_query)

    # specifically checking that it is Response from LLama Index
    if isinstance(response, Response):
        return {"search_response": response.response}

    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="service unavailable at the moment",
    )
