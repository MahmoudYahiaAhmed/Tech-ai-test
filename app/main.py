from fastapi import FastAPI, UploadFile, File, Form
from app.ingestion import ingest_pdf
from app.vector_db import retrieve_relevant
from app.agents.generator import generate_mcqs
from app.agents.evaluator import evaluate_questions
 
app = FastAPI()

@app.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    toc, _ = await ingest_pdf(file)
    return {"table_of_contents": toc}

@app.post("/generate/questions")
async def generate_questions(concept: str = Form(...)):
    docs = retrieve_relevant(concept)
    questions = await generate_mcqs(concept, docs)
    evaluation = await evaluate_questions(questions)
    return {"questions": questions, "evaluation": evaluation}