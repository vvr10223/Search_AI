import os

import dotenv
dotenv.load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-2.0-flash",
    temperature=0.7,
    max_retries=2,
    google_api_key=os.getenv("LLM_API_KEY")#"AIzaSyBRH3AEcj-ucJvRB2UbVwDewYpe9MYGkus",
)
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text:v1.5",
)
