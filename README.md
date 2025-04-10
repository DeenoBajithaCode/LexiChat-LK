# LexiChat LK - Chat with Your Sri Lankan Constitution

This project builds a chatbot that lets users ask questions about the Sri Lankan constitution. It parses the constitution PDF, chunks and embeds the content, stores it in a vector database, and uses OpenAI + LangChain to provide accurate answers with references.

## Features

- Upload and parse the constitution PDF
- Chunk and embed documents using sentence-transformers
- Store embeddings in FAISS or Chroma
- Use LangChain + OpenAI for Retrieval-Augmented Generation (RAG)
- Returns grounded answers with source references

## Requirements

- Python 3.8+
- langchain
- openai
- PyMuPDF or pdfplumber
- sentence-transformers
- faiss-cpu or chromadb
- Django

Install dependencies:

```bash
pip install -r requirements.txt
