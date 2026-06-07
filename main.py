from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from src.pipeline import pipeline

if __name__ == "__main__":
    pipeline()