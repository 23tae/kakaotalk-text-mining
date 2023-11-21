from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess(df) -> list:
  conversation_data = df['Message'].astype(str)

  tokenized_conversations = [word_tokenize(message) for message in conversation_data]

  stop_words = set(stopwords.words('english'))  # You may need to adjust the language
  filtered_conversations = [
      [word.lower() for word in message if word.isalnum() and word.lower() not in stop_words]
      for message in tokenized_conversations
  ]

  stemmer = PorterStemmer()
  stemmed_conversations = [
      [stemmer.stem(word) for word in message]
      for message in filtered_conversations
  ]

  df['Processed_Message'] = [' '.join(message) for message in stemmed_conversations]
  return filtered_conversations