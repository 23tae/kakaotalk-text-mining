import matplotlib.pyplot as plt
from wordcloud import WordCloud
import platform
from check_validity import check_file_existence


def check_font_path():
    system_name = platform.system()
    if system_name == 'Darwin':
        font_path = '/Library/Fonts/Arial Unicode.ttf'
    elif system_name == 'Windows':
        font_path = 'C:\\Windows\\Fonts\\malgun.ttf'
    elif system_name == 'Linux':
        font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
    else:
        raise Exception('Unknown system name')
    check_file_existence(font_path)
    return font_path


def visualize_length(filtered_conversations, output_path):
    message_lengths = [len(message) for message in filtered_conversations]

    plt.hist(message_lengths, bins=20, edgecolor='black')
    plt.xlabel('Message Length')
    plt.ylabel('Frequency')
    plt.title('Distribution of Message Lengths')
    plt.savefig(output_path + '_length.png')


def visualize_wordcloud(filtered_conversations, output_path):
    all_words = [
        word for message in filtered_conversations for word in message]
    text = ' '.join(all_words)
    current_font_path = check_font_path()
    wordcloud = WordCloud(
        font_path=current_font_path,
        width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_path + '_wordcloud.png')
