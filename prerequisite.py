import pandas as pd
from nltk import download

def prerequisite(file_path: str) -> pd.DataFrame:
  download('punkt')
  download('stopwords')

  # 데이터 불러오기
  df = pd.read_csv(file_path)
  return df