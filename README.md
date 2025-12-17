# AI Study Assistant

A full-stack AI-powered study assistant that helps users understand and solve coding problems with step-by-step explanations.

## 🚀 Features
- Chat-based AI interface for coding questions
- Backend powered by FastAPI
- Frontend built with React (Vite)
- MongoDB integration for future chat storage
- Clean, modular project structure

## 🛠 Tech Stack
**Frontend**
- React
- Vite
- JavaScript
- CSS

**Backend**
- FastAPI
- Python
- MongoDB (Motor + PyMongo)
- Uvicorn
- HTTPX

## ⚙️ Setup Instructions

### Backend
```bash
cd backend/backend
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload

