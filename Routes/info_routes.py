"""
Info routes for the Virtual Research Assistant API.
Handles general API information and documentation endpoints.
"""

from fastapi import APIRouter

router = APIRouter(tags=["Info"])

@router.get("/", response_model=dict)
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Virtual Research Assistant API",
        "version": "1.0.0",
        "description": "A FastAPI-based research assistant that fetches and analyzes research papers from multiple sources",
        "endpoints": {
            "/research": "POST - Search and analyze research papers",
            "/research/sources": "GET - Get available data sources",
            "/health": "GET - Health check endpoint",
            "/health/status": "GET - Detailed health check",
            "/docs": "GET - API documentation (Swagger UI)",
            "/redoc": "GET - Alternative API documentation (ReDoc)"
        },
        "documentation": {
            "swagger_ui": "/docs",
            "redoc": "/redoc",
            "openapi_json": "/openapi.json"
        }
    }

@router.get("/api-info", response_model=dict)
async def api_info():
    """Detailed API information"""
    return {
        "name": "Virtual Research Assistant API",
        "version": "1.0.0",
        "description": "A FastAPI-based research assistant that fetches and analyzes research papers from multiple sources",
        "features": [
            "Search research papers from ArXiv",
            "Search research papers from Google Scholar",
            "AI-powered paper summarization",
            "Advantages and disadvantages analysis",
            "Multiple data source support"
        ],
        "technologies": [
            "FastAPI",
            "Python",
            "Groq API",
            "AutoGen",
            "ArXiv API",
            "Google Scholar"
        ]
    } 