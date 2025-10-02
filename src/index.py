import os, chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from ingest import parse_pdfs, parse_videos, parse_audios
embeddings = OllamaEmbeddings(model="nomic-embed-text")
docs = parse_pdfs() + parse_videos() + parse_audios()
vectorstore = Chroma.from_documents(
docs,
embeddings,
collection_name="extremadura",
persist_directory="db"
)
vectorstore.persist()
print("Índice creado y guardado en db/")
