import os, whisper, yt_dlp
from pathlib import Path
from langchain.schema import Document
from llama_parse import LlamaParse
from langchain.document_loaders import DirectoryLoader
LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
parser = LlamaParse(api_key=LLAMA_CLOUD_API_KEY, result_type="markdown")
def parse_pdfs():
  pdf_folder = Path("data/pdfs")
  docs = []
  for f in pdf_folder.glob("*.pdf"):
    docs += parser.load_data(str(f))
  return [Document(page_content=d.text, metadata={"source": d.metadata.get("file_name")}) for d in docs]
def parse_videos():
  video_folder = Path("data/videos")
  docs = []
  model = whisper.load_model("base")
  for f in video_folder.glob("*"):
    result = model.transcribe(str(f))
    docs.append(Document(page_content=result["text"], metadata={"source": f.name}))
  return docs
def parse_audios():
  audio_folder = Path("data/audios")
  docs = []
  model = whisper.load_model("base")
  for f in audio_folder.glob("*"):
    result = model.transcribe(str(f))
    docs.append(Document(page_content=result["text"], metadata={"source": f.name}))
  return docs
if name == "main":
  all_docs = parse_pdfs() + parse_videos() + parse_audios()
  # Guardamos temporalmente como txt para debug
  Path("tmp").mkdir(exist_ok=True)
  for i, d in enumerate(all_docs):
    Path(f"tmp/doc_{i}.txt").write_text(d.page_content)
    print(f"Extraídos {len(all_docs)} documentos.")
