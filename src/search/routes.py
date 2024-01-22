from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.dependencies import get_db_session
from src.search.schemas import SearchRequest, SearchResponse

router = APIRouter(
    prefix="api/v1/search",
    tags=["search"],
)


@router.post(
    "/",
    response_model=SearchResponse,
)
async def search(
    request: SearchRequest,
    db_session: AsyncSession = Depends(get_db_session),
):
    pass
