from sentence_transformers import SentenceTransformer
import numpy as np
#CHUNKER
def chunk_text(text, chunk_size=100, overlap=20):
    words = text.split()
    l = len(text)
    chunks = []
    step_size = chunk_size - overlap
    for i in range(0, len(words), step_size):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append(chunk)
    return chunks
        

    return chunk_list

#EMBEDDER
def embedder(sentences):
    model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(sentences)
    return embeddings


#VECTOR STORE
def retieve(query, chunks, embeddings, top_k=3):
    embedded_query = embedder(query)
    scores = [
        np.dot(embedded_query, emb)/(np.linalg.norm(embedded_query)*np.linalg.norm(emb)) for emb in embeddings
    ]
    indices = np.argsort(scores)[::-1]
    return [chunks[i] for i in indices[:top_k]]
