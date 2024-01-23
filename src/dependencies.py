import secrets

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from src.config import current_config


async def api_key_header(
    api_key_header: str = Security(APIKeyHeader(name="Authorization", auto_error=False))
):
    if api_key_header is not None and secrets.compare_digest(
        api_key_header, f"Basic {current_config.DATAI_API_KEY}"
    ):
        return api_key_header

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
