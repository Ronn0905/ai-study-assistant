from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "study_assistant")

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Default provider: openrouter | openai | huggingface
PROVIDER = os.getenv("PROVIDER", "openrouter")
