# AI Study Assistant

A full-stack AI-powered study assistant that helps users understand and solve coding problems with clear, step-by-step explanations through a chat-based interface.

This project is aimed at students preparing for coding interviews, data structures & algorithms practice, and general programming concepts.

---

## 🚀 Features

- 💬 Chat-based AI interface for coding questions
- 🧠 AI-generated explanations for problem solving
- ⚙️ Backend built with FastAPI
- 🎨 Frontend built with React (Vite)
- 🧪 Swagger API documentation
- 🛢 MongoDB integration (extensible for chat history)
- 🗂 Clean and modular project structure

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- FastAPI
- Python
- MongoDB (Motor + PyMongo)
- Uvicorn
- HTTPX

---

## 📁 Project Structure

```text
ai-study-suite/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── utils/
│   │   ├── db/
│   │   └── main.py
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   ├── index.html
│   └── package.json
│
├── .gitignore
└── README.md

## ⚙️ Setup Instructions

### 🔧 Backend Setup

1. Navigate to the backend directory:
```bash
cd backend

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate

3. Install backend dependencies:

python -m pip install -r requirements.txt


4. Start the backend server:

python -m uvicorn app.main:app --reload


5. Open Swagger API documentation:

http://127.0.0.1:8000/docs

🎨 Frontend Setup

1. Navigate to the frontend directory:

cd frontend


2. Install frontend dependencies:

npm install


3. Start the frontend development server:

npm run dev


4. Open the application in your browser:

http://localhost:5173

