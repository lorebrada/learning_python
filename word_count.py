from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding= 'utf-8')
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    else:
        # count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('python_txt/alice.txt')
count_words(path)
