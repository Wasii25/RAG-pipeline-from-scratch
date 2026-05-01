from sentence_transformers import SentenceTransformer
import numpy as np
import requests
#CHUNKER
def chunk_text(text, chunk_size=100, overlap=20):
    words = text.split()
    chunks = []
    step_size = chunk_size - overlap
    for i in range(0, len(words), step_size):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)
    return chunks


#EMBEDDER
def embedder(sentences):
    model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(sentences)
    return embeddings


#VECTOR STORE
def retieve(query, chunks, embeddings, model, top_k=3):
    embedded_query = model.encode(query)
    scores = [
        np.dot(embedded_query, emb)/(np.linalg.norm(embedded_query)*np.linalg.norm(emb)) for emb in embeddings
    ]
    indices = np.argsort(scores)[::-1]
    return [chunks[i] for i in indices[:top_k]]

def generate(query, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""Use the following context to answer the question.

Context:
{context}

Question: {query}"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    print(response.json())
    return response.json()["response"]

if __name__ == "__main__":
    # 1. Load some text (just hardcode a paragraph or read a .txt file)
    text = open("sample.txt").read()

    # 2. Chunk it
    chunks = chunk_text(text)

    # 3. Embed the chunks
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)

    # 4. Ask a question
    query = "what is the main topic of this text"

    # 5. Retrieve relevant chunks
    top_chunks = retieve(query, chunks, embeddings, model)
    

    # 6. Generate answer
    answer = generate(query, top_chunks)
    print(answer)
