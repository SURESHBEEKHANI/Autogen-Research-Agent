"""
Health routes for the Virtual Research Assistant API.
Handles health checks and monitoring endpoints.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/", response_model=dict)
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}

@router.get("/status", response_model=dict)
async def detailed_health_check():
    """Detailed health check with additional information"""
    return {
        "status": "healthy",
        "message": "API is running",
        "version": "1.0.0",
        "service": "Virtual Research Assistant API"
    } 