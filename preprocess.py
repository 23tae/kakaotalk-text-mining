from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def preprocess(df) -> list:
    conversation_data = df['Message'].astype(str)

    tokenized_conversations = [word_tokenize(
        message) for message in conversation_data]

    stop_words = set(line.strip() for line in open('./korean_stopwords.txt'))
    filtered_conversations = [
        [word for word in message if word not in stop_words]
        for message in tokenized_conversations
    ]

    stemmer = PorterStemmer()
    stemmed_conversations = [
        [stemmer.stem(word) for word in message]
        for message in filtered_conversations
    ]

    df['Processed_Message'] = [' '.join(message)
                               for message in stemmed_conversations]
    return filtered_conversations
