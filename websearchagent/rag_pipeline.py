from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from .connect import llm,embeddings
def rag_pipeline(results,query):
        client = QdrantClient(":memory:")

        # Update size to 768 for Nomic Embed v1.5
        client.create_collection(
            collection_name="demo_collection",
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),  # Changed from 3072 to 768
        )


        vector_store = QdrantVectorStore(
            client=client,
            collection_name="demo_collection",
            embedding=embeddings,)
        for result in results:
            markdown_content = getattr(result, "markdown", None)
            if markdown_content:
                docs = [Document(page_content=result.markdown.fit_markdown)]
                #print(markdown_content.fit_markdown)




                # Fast text splitting - smaller chunks for speed
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,  # Smaller chunks = faster retrieval
                    chunk_overlap=100,

                )

                split_docs = text_splitter.split_documents(docs)

                vector_store.add_documents(docs)
        res = vector_store.similarity_search(query)
        # ✅ Persist to disk
        #vectorstore.persist()
        #print("Documents added successfully.")
        system_prompt="You are a helpful assistant.Answer ONLY from the provided context."

        # Call the LLM using the context from the vector database
        llm_response = llm.invoke(f"{system_prompt}\nContext: {res}\nQuestion: {query} ")
        #print(llm_response.content)
        return str(llm_response.content)
