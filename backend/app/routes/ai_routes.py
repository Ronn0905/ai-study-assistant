from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel
from ..utils.ai_client import analyze_problem
from ..db.mongo import db

router = APIRouter()

class ProblemRequest(BaseModel):
    problem: str

@router.post("/analyze-problem")
async def analyze(request: ProblemRequest):
    problem = request.problem
    print("📥 Received:", problem)

    result = await analyze_problem(problem)

    doc = {
        "problem": problem,
        "response": result,
        "timestamp": datetime.utcnow()
    }
    await db["history"].insert_one(doc)

    return result
