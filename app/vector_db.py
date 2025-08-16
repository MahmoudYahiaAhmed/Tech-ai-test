import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings())
collection = client.get_or_create_collection(name="pdf_chunks")
 
def store_chunks(texts, metadata):
    safe_metadata = {k: (str(v) if isinstance(v, (list, dict)) else v) for k, v in metadata.items()}
    ids = [f"chunk_{i}" for i in range(len(texts))]
    metadatas = [safe_metadata] * len(texts)
    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )

def retrieve_relevant(concept):
    results = collection.query(
        query_texts=[concept],
        n_results=5
    )
    return results['documents'][0] if results['documents'] else []