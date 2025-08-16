from app.llm import call_llm

async def evaluate_questions(questions):
    prompt = (
        "Evaluate the following multiple-choice questions for correctness, ambiguity, and quality. "
        "Provide feedback and improvements if needed.\n\n"
        f"{questions}"
    )
    response =  call_llm(prompt)
    return response