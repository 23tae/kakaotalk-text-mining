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


def visualize_wordcloud(word_count, output_path):
    current_font_path = check_font_path()

    wc = WordCloud(
        font_path=current_font_path,
        width=1000,
        height=1000,
        background_color='white',
        max_words=100
    )

    wc.generate_from_frequencies(word_count)

    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(output_path + '_wordcloud.png')
