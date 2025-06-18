"""
Routes package for the Virtual Research Assistant API.
Contains all route modules organized by functionality.
"""

from .research_routes import router as research_router
from .health_routes import router as health_router
from .info_routes import router as info_router

__all__ = ["research_router", "health_router", "info_router"] 