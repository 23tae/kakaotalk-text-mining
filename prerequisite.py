import pandas as pd
from nltk import download, data

def prerequisite(file_path: str) -> pd.DataFrame:
  if not data.find('tokenizers/punkt'):
    download('punkt')

  if not data.find('corpora/stopwords'):
      download('stopwords')

  df = pd.read_csv(file_path)
  return df