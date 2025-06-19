# Dockerfile for Python 3.11 backend

FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y build-essential curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m appuser

# Set work directory
WORKDIR /app

# Install Python dependencies in a separate layer for better caching
COPY requirements.txt ./
COPY .env .env
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Expose the default port (FastAPI/Uvicorn)
EXPOSE 8000

# Healthcheck (optional, adjust as needed)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:8000/health || exit 1

# Default command (adjust as needed for your app)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
