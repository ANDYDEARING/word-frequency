STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    # Reads in the file while building a dictionary 
    with open(file) as source_file:
        source_str = str((source_file.readline()))
    # clean the string for just letters and spaces
    clean_text = ""
    alphabet_and_space = "abcdefghijklmnopqrstuvwxyz "
    for character in source_str:
        if character.lower() in alphabet_and_space:
            clean_text += character.lower()
    print(clean_text)
    # Sorts the dictionary by word frequency

    # Prints the results in the "bar graph" format


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
