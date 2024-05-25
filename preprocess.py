import re
from konlpy.tag import Okt
from collections import Counter


def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', text)
    return result


def preprocess(df) -> Counter:
    df['Message'] = df['Message'].apply(lambda x: text_cleaning(x))
    message_corpus = ''.join(df['Message'])

    tagger = Okt()
    message_nouns = tagger.nouns(message_corpus)
    word_count = Counter(message_nouns)

    return word_count
