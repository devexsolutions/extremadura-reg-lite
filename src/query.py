import os
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = Ollama(model="mistral")
vectorstore = Chroma(persist_directory="db", embedding_function=embeddings)
qa = RetrievalQA.from_chain_type(
llm=llm,
retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
return_source_documents=True
)
def ask(question: str) -> str:
  return qa.run(question)
