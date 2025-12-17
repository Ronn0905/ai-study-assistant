from fastapi import FastAPI
from .db.mongo import db
from .routes.ai_routes import router as ai_router



app = FastAPI(title="AI Study Assistant")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # allow frontend http://localhost:5174
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register AI routes
app.include_router(ai_router)


@app.get("/")
async def root():
    return {"message": "FastAPI backend is running 🚀"}

@app.get("/health")
async def health():
    # Check MongoDB connection by counting documents in "users"
    count = await db["users"].count_documents({})
    return {"status": "ok", "db": "connected", "user_count": count}
