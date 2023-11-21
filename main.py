import sys

from prerequisite import prerequisite
from preprocess import preprocess
from visualize import visualize_length, visualize_wordcloud
import os

def get_filename(file_path):
  dirname, basename = os.path.split(file_path)
  name, ext = os.path.splitext(basename)
  return name

def get_output_path_without_ext(input_path):
  filename = get_filename(input_path)
  return os.path.join('./result', filename)

def main(path: str):
    try:
       os.path.isfile(path)
    except:
        raise Exception('File not found')
    df = prerequisite(path)
    filtered_conversations = preprocess(df)
    output_path = get_output_path_without_ext(path)
    visualize_length(filtered_conversations, output_path)
    visualize_wordcloud(filtered_conversations, output_path)

if __name__ == "__main__":
    main(sys.argv[1])
