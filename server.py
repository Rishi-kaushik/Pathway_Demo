from fastapi import FastAPI
from pydantic import BaseModel
from pathway_config import get_client
from pathway.table import Table
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

class QueryRequest(BaseModel):
    q: str

app = FastAPI()
client = get_client()

# Vector table used for retrieval
doc_table = Table(client, name="doc_vectors")

# Setup LangChain RAG components
embeddings = OpenAIEmbeddings()
retriever = doc_table.as_retriever(embedding_fn=embeddings.embed_query)
llm = OpenAI(temperature=0)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

@app.post("/query")
async def query_body(req: QueryRequest):
    answer = qa.run(req.q)
    return {"query": req.q, "answer": answer}