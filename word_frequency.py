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
    
    # Make a list of the words
    word_list = clean_text.split(" ")
    
    # Go through the word list and count the "right" words in a dictionary
    word_freq = {}
    for word in word_list:
        if not word in STOP_WORDS:
            if word_freq.get(word) == None:
                word_freq[word] = 1
            else:
                word_freq[word] = word_freq[word] + 1
    print(word_freq)

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
