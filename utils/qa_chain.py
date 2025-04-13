# utils/qa_chain.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.docstore.document import Document

from utils.embedder import chunk_text, build_faiss_index
from utils.parser import extract_text_from_pdf

import os

# Load environment variable for OpenAI
from dotenv import load_dotenv
load_dotenv()

def build_qa_chain(pdf_path):
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Step 2: Chunk the text
    chunks = chunk_text(text)

    # Step 3: Build FAISS index
    index, _ = build_faiss_index(chunks)

    # Step 4: Convert chunks into Document objects
    docs = [Document(page_content=chunk) for chunk in chunks]

    # Step 5: Wrap with LangChain FAISS vectorstore
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS(embedding_model.embed_documents([doc.page_content for doc in docs]), docs, index)

    # Step 6: Build the QA chain with OpenAI
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return qa
