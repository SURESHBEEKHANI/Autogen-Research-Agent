"""
Research routes for the Virtual Research Assistant API.
Handles paper search, analysis, and processing functionality.
"""

from fastapi import APIRouter, HTTPException, Depends
from schema.data_validation import PaperSummary, ResearchQuery, ResearchResponse
from src.agents import ResearchAgents
from src.data_loader import DataLoader
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/research", tags=["Research"])

# Dependency to get API key
def get_api_key():
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        logger.error("GROQ_API_KEY is not configured")
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not configured. Please set it in your environment variables."
        )
    return groq_api_key

# Dependency to get initialized agents
def get_agents(api_key: str = Depends(get_api_key)):
    try:
        return ResearchAgents(api_key)
    except Exception as e:
        logger.error(f"Failed to initialize ResearchAgents: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to initialize AI agents: {str(e)}"
        )

# Dependency to get data loader
def get_data_loader():
    try:
        return DataLoader()
    except Exception as e:
        logger.error(f"Failed to initialize DataLoader: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to initialize data loader: {str(e)}"
        )

@router.post("/", response_model=ResearchResponse)
@router.post("", response_model=ResearchResponse)
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
        logger.info(f"Processing research query: {query.query} from sources: {query.sources}")
        
        all_papers = []
        
        # Fetch from selected sources
        if "ArXiv" in query.sources:
            try:
                logger.info("Fetching papers from ArXiv...")
                arxiv_papers = data_loader.fetch_arxiv_papers(query.query, limit=query.num_results)
                logger.info(f"Found {len(arxiv_papers)} papers from ArXiv")
                all_papers.extend(arxiv_papers)
            except Exception as e:
                logger.error(f"Error fetching from ArXiv: {e}")
                # Continue with other sources instead of failing completely
            
        if "Google Scholar" in query.sources:
            try:
                logger.info("Fetching papers from Google Scholar...")
                google_scholar_papers = data_loader.fetch_google_scholar_papers(query.query)
                logger.info(f"Found {len(google_scholar_papers)} papers from Google Scholar")
                all_papers.extend(google_scholar_papers[:query.num_results])
            except Exception as e:
                logger.error(f"Error fetching from Google Scholar: {e}")
                # Continue with other sources instead of failing completely

        if not all_papers:
            logger.warning(f"No papers found for query: {query.query}")
            raise HTTPException(
                status_code=404,
                detail=f"No papers found for query: {query.query}. Please try a different search term."
            )

        processed_papers = []

        # Process each paper: generate summary and analyze advantages/disadvantages
        for i, paper in enumerate(all_papers):
            try:
                logger.info(f"Processing paper {i+1}/{len(all_papers)}: {paper.get('title', 'Unknown')[:50]}...")
                
                # Generate summary
                summary = agents.summarize_paper(paper.get('summary', ''))
                
                # Analyze advantages/disadvantages
                adv_dis = agents.analyze_advantages_disadvantages(summary)

                processed_papers.append(PaperSummary(
                    title=paper.get("title", "No title available"),
                    link=paper.get("link", "No link available"),
                    summary=summary,
                    advantages_disadvantages=adv_dis
                ))
                
                logger.info(f"Successfully processed paper {i+1}")
                
            except Exception as e:
                logger.error(f"Error processing paper {paper.get('title', 'Unknown')}: {str(e)}")
                # Add a basic paper entry instead of skipping
                processed_papers.append(PaperSummary(
                    title=paper.get("title", "No title available"),
                    link=paper.get("link", "No link available"),
                    summary="Error processing this paper",
                    advantages_disadvantages="Analysis failed for this paper"
                ))
                continue

        logger.info(f"Successfully processed {len(processed_papers)} papers")
        
        return ResearchResponse(
            papers=processed_papers,
            total_papers=len(processed_papers),
            query=query.query,
            sources_used=query.sources
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in research_papers: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred while processing the research query: {str(e)}"
        )

@router.get("/sources", response_model=dict)
async def get_available_sources():
    """Get list of available data sources"""
    return {
        "available_sources": ["ArXiv", "Google Scholar"],
        "description": "Research paper sources that can be used for queries"
    } 