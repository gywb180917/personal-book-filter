import json
from pathlib import Path

def load_books(file_path):
   text = Path(file_path).read_text(encoding="utf-8")
   return json.loads(text)