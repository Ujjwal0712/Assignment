import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
CHROMA_DB_PATH = "./data/chroma_db"
HF_TOKEN = os.getenv("HF_TOKEN")