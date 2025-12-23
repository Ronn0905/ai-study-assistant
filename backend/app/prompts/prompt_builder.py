def build_study_prompt(
    topic: str,
    difficulty: str,
    user_query: str,
    context: str
) -> str:
    return f"""
You are an AI study assistant.

Topic: {topic}
Difficulty: {difficulty}

Previous Context:
{context}

User Question:
{user_query}

Respond with:
1. Concept summary
2. Step-by-step explanation
3. Example
4. 3 quiz questions with answers
"""
