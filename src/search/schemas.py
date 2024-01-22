from pydantic import BaseModel


class SearchRequest(BaseModel):
    db_query_tables: list
    search_query: str


class SearchResponse(BaseModel):
    search_response: str
