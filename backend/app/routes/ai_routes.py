from fastapi import APIRouter, Query
from pydantic import BaseModel

from app.prompts.prompt_builder import build_study_prompt
from app.db.mongo import (
    save_interaction,
    get_recent_context,
    get_session_history
)
from app.utils.ai_client import analyze_problem

# ✅ router MUST be defined at top-level
router = APIRouter()


class ProblemRequest(BaseModel):
    problem: str
    session_id: str


@router.post("/analyze-problem")
async def analyze(request: ProblemRequest):
    problem = request.problem
    session_id = request.session_id

    previous_context = await get_recent_context(session_id)
    context_text = "\n".join(previous_context)

    prompt = build_study_prompt(
        topic="Data Structures and Algorithms",
        difficulty="Medium",
        user_query=problem,
        context=context_text
    )

    result = await analyze_problem(prompt)

    await save_interaction(
        session_id=session_id,
        query=problem,
        response=result
    )

    return result


@router.get("/history/{session_id}")
async def get_history(
    session_id: str,
    limit: int = Query(50, ge=1, le=200)
):
    history = await get_session_history(session_id, limit)

    return {
        "session_id": session_id,
        "count": len(history),
        "items": history
    }
