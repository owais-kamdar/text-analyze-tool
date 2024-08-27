import sys
import collections
import string

def analyze_text(file_path, top_n=10):
    """
    Analyze a text file, counting word occurrences and identifying the most common words.

    Args:
        file_path (str): The path to the text file to analyze.
        top_n (int): Number of top common words to display.

    Returns:
        dict: A dictionary with basic statistics and common words.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
            # Remove punctuation using str.translate
            translator = str.maketrans('', '', string.punctuation)
            text = text.translate(translator)
            words = text.split()
            total_words = len(words)
            word_counts = collections.Counter(words)
            unique_words = len(word_counts)
            common_words = word_counts.most_common(top_n)
            
            return {
                "total_words": total_words,
                "unique_words": unique_words,
                "common_words": common_words
            }
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path> [<top_n>]")
        sys.exit(1)

    file_path = sys.argv[1]
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    stats = analyze_text(file_path, top_n)

    print(f"Total words: {stats['total_words']}")
    print(f"Unique words: {stats['unique_words']}")
    print("Most common words:")
    for word, count in stats['common_words']:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
