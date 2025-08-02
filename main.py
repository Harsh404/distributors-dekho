from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from llm import LLM

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
