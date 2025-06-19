# Autogen Research Agent

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/SURESHBEEKHANI/Autogen-Research-Agent.git)

A full-stack, AI-powered research assistant for searching, summarizing, and analyzing academic papers from multiple sources. Combines a FastAPI backend with a modern React/TypeScript frontend for a seamless research experience.

---

## 🏗️ Architecture

```
[Frontend (React/TypeScript)] <----> [Backend (FastAPI, Python)] <----> [External APIs: ArXiv, Google Scholar, Groq]
```
- **Frontend**: User interface for searching, viewing, and analyzing papers
- **Backend**: Handles data retrieval, AI summarization, and API endpoints

---

## 🚀 Features

### Backend
- Multi-source search: ArXiv & Google Scholar
- AI-powered summarization and pros/cons analysis (Groq API)
- RESTful API with automatic Swagger/ReDoc docs
- Robust error handling and logging
- Health/status endpoints

### Frontend
- Smart search interface (source selection, result count, validation)
- AI-generated summaries and analysis display
- Card-based, expandable results with direct links
- Modern, responsive UI (React, TypeScript, Tailwind CSS)
- Fast performance (Vite), mobile-friendly

---

## 🛠️ Tech Stack
- **Backend**: FastAPI, Python 3.8+, Groq API, ArXiv API, Google Scholar
- **Frontend**: React 18, TypeScript, Tailwind CSS, Vite, Axios
- **Other**: Docker, MIT License

---

## ⚡ Setup & Installation

### Backend
1. Clone the repo and enter backend:
   ```bash
   git clone <repository-url>
   cd Autogen-Research-Agent/backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env`:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   LOG_LEVEL=INFO
   ```
5. Run the backend:
   ```bash
   python main.py
   # or for production
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Frontend
1. Enter frontend directory:
   ```bash
   cd ../frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the frontend:
   ```bash
   npm run dev
   ```
4. Open [http://localhost:3000](http://localhost:8000/docs) in your browser.

---

## 📦 Repository

- **GitHub:** [https://github.com/SURESHBEEKHANI/Autogen-Research-Agent.git](https://github.com/SURESHBEEKHANI/Autogen-Research-Agent.git)
- This is the official repository for the Autogen Research Agent project. Star or fork to contribute, report issues, or stay updated.

---

## 📞 Usage
- Search for papers by topic, select sources, and set result count
- View AI-generated summaries and pros/cons for each paper
- Click direct links to original papers
- Use the API directly for programmatic access

---

## 📚 API Endpoints (Backend)
- `POST /research/` — Search and analyze research papers
- `GET /research/sources` — List available data sources
- `GET /api-info` — API information
- `GET /health` — Basic health check
- `GET /health/status` — Detailed health status
- Interactive docs: [Swagger UI](http://localhost:8000/docs), [ReDoc](http://localhost:8000/redoc)

---

## 🤝 Development & Contribution
1. Fork the repository
2. Create a feature branch
3. Make your changes (add tests if possible)
4. Submit a pull request

---

## 📄 License
MIT License — see LICENSE file for details.

---

## 📞 Support
- Check troubleshooting in backend/frontend READMEs
- Review API docs at `/docs`
- Open an issue on GitHub