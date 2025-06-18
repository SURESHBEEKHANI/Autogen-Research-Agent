# Research Agent Backend

A FastAPI-based research assistant that fetches and analyzes research papers from multiple sources using AI.

## Features

- 🔍 **Multi-Source Search**: Search papers from ArXiv and Google Scholar
- 🤖 **AI Analysis**: Generate summaries and analyze advantages/disadvantages using Groq API
- 📊 **RESTful API**: Clean API endpoints with automatic documentation
- 🔒 **Error Handling**: Robust error handling and logging

## Setup

### Prerequisites

- Python 3.8+
- Groq API key (get from https://console.groq.com/)

### Installation

1. **Clone the repository and navigate to backend:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   
   Create a `.env` file in the backend directory:
   ```bash
   # .env
   GROQ_API_KEY=your_actual_groq_api_key_here
   LOG_LEVEL=INFO
   ```

5. **Run the application:**
   ```bash
   python main.py
   ```

   The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### Research Endpoints

- `POST /research/` - Search and analyze research papers
- `GET /research/sources` - Get available data sources

### Info Endpoints

- `GET /` - API root information
- `GET /api-info` - Detailed API information

### Health Endpoints

- `GET /health` - Basic health check
- `GET /health/status` - Detailed health status

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Usage Example

```bash
# Search for research papers
curl -X POST "http://127.0.0.1:8000/research/" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "machine learning",
    "sources": ["ArXiv", "Google Scholar"],
    "num_results": 5
  }'
```

## Troubleshooting

### Common Issues

1. **500 Internal Server Error**: 
   - Check if GROQ_API_KEY is set in your `.env` file
   - Verify your Groq API key is valid
   - Check the logs for specific error messages

2. **No papers found**:
   - Try different search terms
   - Check if data sources are accessible
   - Verify network connectivity

3. **Import errors**:
   - Ensure all dependencies are installed
   - Check Python version compatibility

### Logging

The application uses Python's logging module. Set `LOG_LEVEL` in your `.env` file to control verbosity:
- `DEBUG`: Detailed debug information
- `INFO`: General information (default)
- `WARNING`: Warning messages only
- `ERROR`: Error messages only

## Development

### Project Structure

```
backend/
├── main.py              # FastAPI application entry point
├── Routes/              # API route handlers
│   ├── research_routes.py
│   ├── info_routes.py
│   └── health_routes.py
├── src/                 # Core application logic
│   ├── agents.py        # AI agents for analysis
│   └── data_loader.py   # Data fetching from sources
├── schema/              # Data validation schemas
│   └── data_validation.py
└── requirements.txt     # Python dependencies
```

### Adding New Data Sources

1. Add the source to `data_loader.py`
2. Update the available sources in `research_routes.py`
3. Add error handling for the new source

## License

This project is licensed under the MIT License. 