"""
Research routes for the Virtual Research Assistant API.
Handles paper search, analysis, and processing functionality.
"""

from fastapi import APIRouter, HTTPException, Depends
from schema.data_validation import PaperSummary, ResearchQuery, ResearchResponse
from src.agents import ResearchAgents
from src.data_loader import DataLoader
import os

router = APIRouter(prefix="/research", tags=["Research"])

# Dependency to get API key
def get_api_key():
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not configured. Please set it in your environment variables."
        )
    return groq_api_key

# Dependency to get initialized agents
def get_agents(api_key: str = Depends(get_api_key)):
    return ResearchAgents(api_key)

# Dependency to get data loader
def get_data_loader():
    return DataLoader()

@router.post("/", response_model=ResearchResponse)
async def research_papers(
    query: ResearchQuery,
    agents: ResearchAgents = Depends(get_agents),
    data_loader: DataLoader = Depends(get_data_loader)
):
    """
    Search and analyze research papers from multiple sources.
    
    - **query**: The research topic to search for
    - **sources**: List of data sources to search (ArXiv, Google Scholar)
    - **num_results**: Number of results to return per source
    """
    try:
        all_papers = []
        
        # Fetch from selected sources
        if "ArXiv" in query.sources:
            arxiv_papers = data_loader.fetch_arxiv_papers(query.query, limit=query.num_results)
            all_papers.extend(arxiv_papers)
            
        if "Google Scholar" in query.sources:
            google_scholar_papers = data_loader.fetch_google_scholar_papers(query.query)
            all_papers.extend(google_scholar_papers[:query.num_results])

        if not all_papers:
            raise HTTPException(
                status_code=404,
                detail=f"No papers found for query: {query.query}"
            )

        processed_papers = []

        # Process each paper: generate summary and analyze advantages/disadvantages
        for paper in all_papers:
            try:
                summary = agents.summarize_paper(paper['summary'])
                adv_dis = agents.analyze_advantages_disadvantages(summary)

                processed_papers.append(PaperSummary(
                    title=paper["title"],
                    link=paper["link"],
                    summary=summary,
                    advantages_disadvantages=adv_dis
                ))
            except Exception as e:
                # Log error but continue processing other papers
                print(f"Error processing paper {paper.get('title', 'Unknown')}: {str(e)}")
                continue

        return ResearchResponse(
            papers=processed_papers,
            total_papers=len(processed_papers),
            query=query.query,
            sources_used=query.sources
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the research query: {str(e)}"
        )

@router.get("/sources", response_model=dict)
async def get_available_sources():
    """Get list of available data sources"""
    return {
        "available_sources": ["ArXiv", "Google Scholar"],
        "description": "Research paper sources that can be used for queries"
    } 