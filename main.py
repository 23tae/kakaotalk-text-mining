import sys

from prerequisite import prerequisite
from preprocess import preprocess
from visualize import visualize_length, visualize_wordcloud

def main(path: str):
    df = prerequisite(path)
    filtered_conversations = preprocess(df)
    visualize_length(filtered_conversations)
    visualize_wordcloud(filtered_conversations)

if __name__ == "__main__":
    main(sys.argv[1])
