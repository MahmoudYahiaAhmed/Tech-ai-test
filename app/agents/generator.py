from app.llm import call_llm  

async def generate_mcqs(concept, docs):
    context = "\n\n".join(docs) if docs else ""
    prompt = (
        f"Using the following context, generate 5 multiple-choice questions about {concept}:\n\n"
        f"{context}\n\n"
        "Format the questions with options A-D and indicate the correct answer after each question."
    )
    response =  call_llm(prompt)
    return response