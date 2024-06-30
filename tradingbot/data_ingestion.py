from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from tradingbot.helper import load_file
import os
import pandas as pd

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def ingest_data(status):
    vector_store = AstraDBVectorStore(
            embedding=embedding,
            collection_name="financebot",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE,
        )
    
    storage=status
    
    if storage==None:
        docs=load_file()
        inserted_ids = vector_store.add_documents(docs)
    else:
        return vector_store 
    
    return vector_store, inserted_ids

if __name__=='__main__':
    vector_store,inserted_ids = ingest_data(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vector_store.similarity_search("can you tell me the low budget sound basshead.")
    for res in results:
            print(f"* {res.page_content} [{res.metadata}]")