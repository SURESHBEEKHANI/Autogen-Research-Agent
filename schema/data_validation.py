from pydantic import BaseModel
from typing import List, Optional
# Pydantic models for request/response
class ResearchQuery(BaseModel):
    query: str
    sources: List[str] = ["ArXiv", "Google Scholar"]
    num_results: int = 5

class PaperSummary(BaseModel):
    title: str
    link: str
    summary: str
    advantages_disadvantages: str

class ResearchResponse(BaseModel):
    papers: List[PaperSummary]
    total_papers: int
    query: str
    sources_used: List[str]

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
