from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from Routes import research_router, health_router, info_router
import uvicorn

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Virtual Research Assistant API",
    description="A FastAPI-based research assistant that fetches and analyzes research papers from multiple sources",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(info_router, prefix="/api")
app.include_router(health_router, prefix="/api")
app.include_router(research_router, prefix="/api")

# Add aliases for /health and /research (without /api) for compatibility
app.include_router(health_router, prefix="/health")
app.include_router(research_router, prefix="/research")

if __name__ == "__main__":
    """
    Run the FastAPI app using uvicorn.
    """
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)