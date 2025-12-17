import httpx
import json
import re
from ..core import config


async def analyze_problem(problem: str) -> dict:
    """
    Sends a coding problem to OpenRouter API and returns safe JSON.
    Handles errors, missing fields, and malformed model output.
    """

    prompt = f"""
    You are an expert coding tutor. Analyze the following problem:

    {problem}

    Return your answer strictly in JSON with these fields:
    - summary
    - brute_force
    - optimized
    - complexity
    - hints

    ❗ ONLY return valid JSON. No markdown or extra text.
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
                        {"role": "system", "content": "You output strictly JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.4,
                    "max_tokens": 800
                }
            )

        data = response.json()

        # -----------------------
        # (1) HANDLE OPENROUTER ERRORS
        # -----------------------
        if "error" in data:
            return {"error": "OpenRouter API error", "details": data["error"]}

        if "choices" not in data:
            return {"error": "No 'choices' returned", "raw": data}

        content = data["choices"][0]["message"]["content"]

        # -----------------------
        # (2) EXTRACT JSON SAFELY
        # -----------------------
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            return {"error": "Model output missing JSON", "raw": content}

        json_text = match.group(0)

        # -----------------------
        # (3) PARSE JSON SAFELY
        # -----------------------
        try:
            return json.loads(json_text)
        except json.JSONDecodeError:
            return {"error": "JSON parse failed", "raw": json_text}

    except Exception as e:
        return {"error": "Exception occurred", "details": str(e)}
