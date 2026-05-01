# RAG Pipeline from Scratch

A minimal Retrieval-Augmented Generation (RAG) pipeline built from first principles — no LangChain, no abstractions. Just raw components wired together.

## What it does

Takes a text document, answers questions about it by:
1. Splitting the document into overlapping chunks
2. Embedding each chunk into a vector using a pretrained sentence transformer
3. Finding the most relevant chunks to a query via cosine similarity
4. Feeding those chunks as context into a local LLM to generate an answer

## Pipeline

```
Document → Chunker → Embedder → Vector Store
                                     ↑
               Query ────────────────┘
                                     ↓
                              Top-K Chunks → LLM → Answer
```

## Components

| Component | Description |
|---|---|
| **Chunker** | Splits text into overlapping word-level windows |
| **Embedder** | Encodes chunks using `all-MiniLM-L6-v2` (384-dim vectors) |
| **Vector Store** | Cosine similarity search over chunk embeddings using NumPy |
| **Generator** | Local LLM via Ollama (`llama3.2`) for answer generation |

## Setup

**Requirements**
- Python 3.10+
- [Ollama](https://ollama.com) installed and running

```bash
# Clone the repo
git clone https://github.com/yourusername/rag-pipeline-from-scratch
cd rag-pipeline-from-scratch

# Create and activate a virtual environment
python -m venv ragvenv
source ragvenv/bin/activate

# Install dependencies
pip install sentence-transformers numpy requests

# Pull the LLM
ollama pull llama3.2
```

## Usage

Add your document as `sample.txt` in the project root, then:

```bash
# Make sure Ollama is running
ollama serve &

# Run the pipeline
python main.py
```

Edit the `query` variable in `main.py` to ask your own question.

## Dependencies

- [`sentence-transformers`](https://www.sbert.net/) — chunk embeddings
- `numpy` — cosine similarity search
- `requests` — Ollama API calls
- [`ollama`](https://ollama.com) — local LLM inference

## Why no vector DB or framework?

Built this to understand what RAG systems actually do under the hood. Every production framework (LangChain, LlamaIndex) is just a more engineered version of these same four steps.
![Screenshot From 2026-05-01 10-13-38](https://github.com/user-attachments/assets/e18c2237-5292-4aa3-96c7-2aa3571f8ba1)
