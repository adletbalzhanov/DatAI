from pydantic import BaseModel


class DBConfig(BaseModel):
    user: str
    password: str
    host: str
    port: int
    db: str


class SearchRequest(BaseModel):
    db_config: DBConfig
    db_query_tables: list
    search_query: str


class SearchResponse(BaseModel):
    search_response: str
