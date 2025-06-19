# Virtual Research Assistant

A FastAPI-based research assistant that fetches and analyzes research papers from multiple sources using AI-powered summarization and analysis.

## 🚀 Features

- **Multi-Source Research Retrieval**: Fetch papers from ArXiv and Google Scholar
- **AI-Powered Analysis**: Generate summaries and analyze advantages/disadvantages using Groq LLM
- **RESTful API**: Clean, documented API endpoints with automatic OpenAPI documentation
- **Error Handling**: Comprehensive error handling and validation
- **CORS Support**: Cross-origin resource sharing enabled for web applications
- **Health Monitoring**: Built-in health check endpoints

## 📋 Prerequisites

- Python 3.8+
- GROQ API key (get one at [https://console.groq.com/](https://console.groq.com/))

## 🛠️ Installation

1. **Clone the repository** (if not already done):
```bash
git clone <repository-url>
cd Autogen-Research-Agent
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 🚀 Running the FastAPI Server

### Development Mode
```bash
python fastapi_app.py
```

### Production Mode (with uvicorn)
```bash
uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --reload
```

The server will start at `http://localhost:8000`

## 📚 API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Available Endpoints

#### 1. Health Check
```http
GET /api/health
```
Returns the health status of the API.

**Response:**
```json
{
  "status": "healthy",
  "message": "Virtual Research Assistant API is running",
  "version": "1.0.0"
}
```

#### 2. Get Available Sources
```http
GET /api/sources
```
Returns list of available data sources.

**Response:**
```json
{
  "sources": [
    {
      "name": "ArXiv",
      "description": "Open access repository for academic papers",
      "url": "https://arxiv.org"
    },
    {
      "name": "Google Scholar",
      "description": "Academic search engine for scholarly literature",
      "url": "https://scholar.google.com"
    }
  ]
}
```

#### 3. Research Papers Search
```http
POST /api/research
```

**Request Body:**
```json
{
  "query": "machine learning",
  "sources": ["ArXiv", "Google Scholar"],
  "num_results": 5
}
```

**Response:**
```json
{
  "query": "machine learning",
  "papers": [
    {
      "title": "Paper Title",
      "link": "https://arxiv.org/abs/...",
      "summary": "AI-generated summary of the paper",
      "advantages_disadvantages": "Analysis of pros and cons"
    }
  ],
  "total_papers": 5,
  "sources_used": ["ArXiv", "Google Scholar"]
}
```

## 🧪 Testing the API

### Using the Test Client
```bash
python test_fastapi_client.py
```

### Using curl
```bash
# Health check
curl http://localhost:8000/api/health

# Search for papers
curl -X POST "http://localhost:8000/api/research" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "quantum computing",
    "sources": ["ArXiv"],
    "num_results": 3
  }'
```

### Using Python requests
```python
import requests

# Search for papers
response = requests.post(
    "http://localhost:8000/api/research",
    json={
        "query": "machine learning",
        "sources": ["ArXiv"],
        "num_results": 5
    }
)

if response.status_code == 200:
    data = response.json()
    print(f"Found {data['total_papers']} papers")
    for paper in data['papers']:
        print(f"- {paper['title']}")
```

## 🔧 Configuration

### Environment Variables
- `GROQ_API_KEY`: Your Groq API key (required)

### API Configuration
The API can be configured by modifying the following in `fastapi_app.py`:
- CORS settings
- Rate limiting
- Request/response models
- Error handling

## 🏗️ Architecture

```
fastapi_app.py          # Main FastAPI application
├── src/
│   ├── agents.py       # AI agents for summarization and analysis
│   └── data_loader.py  # Data fetching from ArXiv and Google Scholar
├── test_fastapi_client.py  # Test client for API
└── requirements.txt    # Python dependencies
```

## 🔒 Security Considerations

- **API Key**: Store your GROQ_API_KEY in environment variables, never in code
- **CORS**: Configure CORS settings properly for production
- **Rate Limiting**: Consider adding rate limiting for production use
- **Input Validation**: All inputs are validated using Pydantic models

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Cloud Deployment
The FastAPI app can be deployed to:
- **Heroku**: Use the provided Dockerfile
- **AWS Lambda**: Use Mangum adapter
- **Google Cloud Run**: Use the provided Dockerfile
- **Azure App Service**: Deploy as a web app

## 🐛 Troubleshooting

### Common Issues

1. **GROQ_API_KEY not found**
   - Ensure `.env` file exists with your API key
   - Check that `python-dotenv` is installed

2. **Import errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.8+ required)

3. **No papers found**
   - Check your internet connection
   - Verify the search query is valid
   - Some sources may have rate limits

4. **AI analysis fails**
   - Verify your GROQ API key is valid
   - Check your Groq account has sufficient credits

## 📝 API Response Codes

- `200`: Success
- `400`: Bad Request (invalid parameters)
- `404`: No papers found
- `500`: Internal Server Error

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆚 Comparison with Streamlit Version

| Feature | Streamlit | FastAPI |
|---------|-----------|---------|
| Interface | Web UI | REST API |
| Use Case | Interactive demo | Production API |
| Documentation | Built-in UI | OpenAPI/Swagger |
| Integration | Manual | Programmatic |
| Scalability | Limited | High |
| Deployment | Streamlit Cloud | Any platform |

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API documentation at `/docs`
3. Open an issue on GitHub 

This is the README for the project root. 