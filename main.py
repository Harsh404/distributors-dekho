from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from llm import LLM
import uvicorn
import sys

app = FastAPI(title="Groq Synonym Generator API")
llm = LLM()

class SynonymRequest(BaseModel):
    word: str

class SynonymResponse(BaseModel):
    word: str
    synonyms: List[str]

@app.post("/generate-synonyms", response_model=SynonymResponse)
async def generate_synonyms(request: SynonymRequest):
    try:
        synonyms = llm.get_synonyms(request.word)
        return SynonymResponse(word=request.word, synonyms=synonyms)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = 8003 # default port
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port '{sys.argv[1]}', using default port 8000.")
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
