import httpx
import json
import re
from typing import Dict, Any
from ..core import config


def normalize_llm_response(parsed: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ensures the LLM response always contains expected fields.
    Adds safe defaults for missing keys.
    """
    return {
        "summary": parsed.get("summary", ""),
        "brute_force": parsed.get("brute_force", ""),
        "optimized": parsed.get("optimized", ""),
        "complexity": parsed.get("complexity", ""),
        "hints": parsed.get("hints", ""),
        "quiz": parsed.get("quiz", [])
    }


async def analyze_problem(prompt: str) -> Dict[str, Any]:
    """
    Sends a prompt to OpenRouter LLM and returns a safe, structured response.

    Behavior:
    - Attempts strict JSON parsing
    - Normalizes missing fields
    - Falls back to raw text if parsing fails
    - Never crashes the API
    """

    system_prompt = """
You are an expert coding tutor.
You MUST return strictly valid JSON.
Do not include markdown, explanations, or extra text.
"""

    user_prompt = f"""
{prompt}

Return your answer strictly in JSON with the following fields:
- summary
- brute_force
- optimized
- complexity
- hints
- quiz (array of objects with question and answer)

Example quiz format:
"quiz": [
  {{"question": "...", "answer": "..."}}
]

❗ ONLY return valid JSON.
"""

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.4,
                    "max_tokens": 900
                }
            )

        data = response.json()

        # -----------------------
        # (1) HANDLE API ERRORS
        # -----------------------
        if "error" in data:
            return {
                "error": "OpenRouter API error",
                "details": data["error"]
            }

        if "choices" not in data or not data["choices"]:
            return {
                "error": "No choices returned by LLM",
                "raw": data
            }

        content = data["choices"][0]["message"]["content"]

        # -----------------------
        # (2) EXTRACT JSON SAFELY
        # -----------------------
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            # Fallback: raw text response
            return {
                "raw_text": content
            }

        json_text = match.group(0)

        # -----------------------
        # (3) PARSE + NORMALIZE JSON
        # -----------------------
        try:
            parsed = json.loads(json_text)
            return normalize_llm_response(parsed)
        except json.JSONDecodeError:
            return {
                "raw_text": json_text
            }

    except Exception as e:
        return {
            "error": "Exception occurred while calling LLM",
            "details": str(e)
        }
