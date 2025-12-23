# AI Study Assistant

A full-stack AI-powered study assistant that helps users understand and solve coding problems with clear, step-by-step explanations through a chat-based interface.

This project is aimed at students preparing for coding interviews, data structures & algorithms practice, and general programming concepts.

---

## Features

- Chat-based AI interface for coding questions
- AI-generated explanations for problem solving
- Backend built with FastAPI
- Frontend built with React (Vite)
- Swagger API documentation
- MongoDB integration (extensible for chat history)
- Clean and modular project structure

---

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- MongoDB
- OpenAI API / LLM Integration

---

## Project Structure

```
ai-study-assistant/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── models/
│   │   └── utils/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your configuration:
```
OPENAI_API_KEY=your_api_key_here
MONGO_URI=your_mongodb_uri
```

5. Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

---

## Usage

1. Start both the backend and frontend servers
2. Open the application in your browser
3. Enter a coding question or problem
4. Receive AI-generated explanations and solutions
5. Chat history is stored for reference

---

## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive Swagger API documentation.

---

## Future Enhancements

- User authentication
- Persistent chat history with sessions
- Code execution environment
- Problem categorization and tagging
- Export chat sessions

---

## License

This project is open source and available under the MIT License.
