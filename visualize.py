import matplotlib.pyplot as plt
from wordcloud import WordCloud

def visualize_length(filtered_conversations, output_path):
  message_lengths = [len(message) for message in filtered_conversations]

  plt.hist(message_lengths, bins=20, edgecolor='black')
  plt.xlabel('Message Length')
  plt.ylabel('Frequency')
  plt.title('Distribution of Message Lengths')
  plt.savefig(output_path + '_length.png')

def visualize_wordcloud(filtered_conversations, output_path):
  all_words = [word for message in filtered_conversations for word in message]
  text = ' '.join(all_words)
  wordcloud = WordCloud(
    font_path='/Library/Fonts/Arial Unicode.ttf',
    width=800, height=400, background_color='white').generate(text)
  
  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.savefig(output_path + '_wordcloud.png')