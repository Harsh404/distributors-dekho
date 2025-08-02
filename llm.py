import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # Loads .env

class LLM:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com")

        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        self.client = Groq(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def get_synonyms(self, word: str, count: int = 5) -> list[str]:
        prompt = f"Generate {count} synonyms for the word: '{word}'. Return them as a comma-separated list."

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # or llama3-70b-8192, mixtral, etc.
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1092,
        )

        raw_output = response.choices[0].message.content
        return [w.strip() for w in raw_output.split(",") if w.strip()]
