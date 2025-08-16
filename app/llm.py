from langchain_community.chat_models import ChatOpenAI  

def call_llm(prompt):
    llm = ChatOpenAI(
        model_name="gpt-4o-mini"  
    )
    response = llm.invoke(prompt)
    return response.content if hasattr(response, "content") else response



