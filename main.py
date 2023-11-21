import sys

from check_validity import check_file_and_directory
from prerequisite import prerequisite
from preprocess import preprocess
from visualize import visualize_length, visualize_wordcloud

output_dir = './result'

def main(path: str):
    output_path = check_file_and_directory(path, output_dir)
    df = prerequisite(path)
    filtered_conversations = preprocess(df)
    visualize_length(filtered_conversations, output_path)
    visualize_wordcloud(filtered_conversations, output_path)

if __name__ == "__main__":
    main(sys.argv[1])
