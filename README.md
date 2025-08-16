#  Algebra Review QA System

This project provides an **interactive question generation and evaluation tool** for educational PDFs, especially focused on **Algebra review materials**.  

**FastAPI** – For programmatic access to PDF ingestion, question generation, and evaluation.

---
 
## Features

- **PDF Ingestion**  
  Extracts the **Table of Contents** and **page text** from an uploaded PDF, stores it in a vector database (ChromaDB), and indexes it for retrieval.

- **Context-Aware MCQ Generation**  
  Generates multiple-choice questions based on retrieved context using LLMs (LangChain + OpenAI API).

- **MCQ Evaluation**  
  Analyzes generated questions for correctness, ambiguity, and quality, providing feedback.

- **Search & Retrieval**  
  Retrieves relevant content chunks from the vector database for a given concept/topic.

---

##  Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) – REST API
- **Database**: [ChromaDB](https://www.trychroma.com/) – vector database for context retrieval
- **LLM**: [LangChain](https://www.langchain.com/) with `ChatOpenAI`
- **PDF Processing**: [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz`)
- **Containerization**: Docker

---
## Run FastAPI Backend 

cd app

uvicorn main:app --reload --host 0.0.0.0 --port 8000

Swagger Docs:
http://localhost:8000/docs

## Docker Deployment

**docker build -t fastapi-qa-app .**

## Run Container 

docker run -e OPENAI_API_KEY="put ur api key here!" -p 8000:8000 fastapi-qa-app


## API Endpoints
1. PDF Ingestion
POST /ingest
Body: multipart/form-data with PDF file
Response:
{
  "table_of_contents": [
    "Page 1: Introduction",
    "Page 2: Algebra Basics"
  ]
}
2. Generate MCQs
POST /generate/questions
Body: form-data with concept string
Response:
{
  "questions": "...",
  "evaluation": "..."
}
