import pandas as pd
from nltk import download, data


def prerequisite(file_path: str) -> pd.DataFrame:
    try: data.find('tokenizers/punkt')
    except: download('punkt', download_dir='./venv/nltk_data')

    try: data.find('corpora/stopwords')
    except: download('stopwords', download_dir='./venv/nltk_data')

    df = pd.read_csv(file_path)
    return df
