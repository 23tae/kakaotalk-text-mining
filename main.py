import sys
import pandas as pd

from check_validity import check_file_and_directory
from preprocess import preprocess
from visualize import visualize_wordcloud

output_dir = './result'


def main(path: str):
    output_path = check_file_and_directory(path, output_dir)
    df = pd.read_csv(path)
    word_count = preprocess(df)
    visualize_wordcloud(word_count, output_path)


if __name__ == "__main__":
    main(sys.argv[1])
