import motor.motor_asyncio
from datetime import datetime
from app.core import config

client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGO_URI)
db = client[config.DB_NAME]

# Collection
study_history_collection = db["study_history"]


# -----------------------------
# SAVE INTERACTION (NEW SCHEMA)
# -----------------------------
async def save_interaction(
    session_id: str,
    query: str,
    response: dict
):
    await study_history_collection.insert_one({
        "session_id": session_id,
        "query": query,

        # ✅ structured fields (new schema)
        "summary": response.get("summary"),
        "optimized": response.get("optimized"),
        "quiz": response.get("quiz"),

        # ✅ store full response for compatibility + debugging
        "raw_response": response,

        "timestamp": datetime.utcnow()
    })


# ------------------------------------
# CONTEXT FETCH (USED FOR PROMPT BUILD)
# ------------------------------------
async def get_recent_context(session_id: str, limit: int = 3) -> list[str]:
    cursor = (
        study_history_collection
        .find({"session_id": session_id})
        .sort("timestamp", -1)
        .limit(limit)
    )

    summaries = []
    async for doc in cursor:
        # 🧠 handle ALL historical schemas
        raw = (
            doc.get("raw_response")
            or doc.get("response")
            or {}
        )

        summary = doc.get("summary") or raw.get("summary")

        if summary:
            summaries.append(summary)

    return summaries[::-1]


# ------------------------------------
# FULL SESSION HISTORY (API ENDPOINT)
# ------------------------------------
async def get_session_history(session_id: str, limit: int = 50):
    cursor = (
        study_history_collection
        .find({"session_id": session_id})
        .sort("timestamp", -1)
        .limit(limit)
    )

    results = []
    async for doc in cursor:
        # 🧠 support ALL schema versions
        raw = (
            doc.get("raw_response")
            or doc.get("response")
            or {}
        )

        results.append({
            "query": doc["query"],

            # ✅ structured → raw_response → response
            "summary": doc.get("summary") or raw.get("summary"),
            "optimized": doc.get("optimized") or raw.get("optimized"),
            "quiz": doc.get("quiz") or raw.get("quiz"),

            "timestamp": doc["timestamp"]
        })

    return results[::-1]
