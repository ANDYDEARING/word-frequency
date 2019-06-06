STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    # Reads in the file while building a dictionary
    with open(file) as source_file:
        source_str = source_file.read()

    # clean the string for just letters and spaces and check for \n
    clean_text = ""
    alphabet_and_space = "abcdefghijklmnopqrstuvwxyz "
    # bug patch: these can make double spaces so I'll have to clean this later
    source_str = source_str.replace("\n", " ")
    source_str = source_str.replace("-", " ")
    # AREA FOR IMPROVEMENT: I would like this to be able to replace any non-alpha
    #  character with a space

    # add only letters and spaces to clean_text
    for character in source_str:
        if character.lower() in alphabet_and_space:
            clean_text += character.lower()
    
    # Make a list of the words
    word_list = clean_text.split(" ")

    # Go through the word list and count the "go" words in a dictionary
    word_freq = {}
    for word in word_list:
        # here's the cleaner from above to handle empty string words
        if (not word in STOP_WORDS) and (word != ""):
            if word_freq.get(word) == None:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    
    # Sorts alphabetically first to match spec and converts them to a list of tuples
    def get_word(word_tup):
        """Given a tuple, returns the first value"""
        return word_tup[0]
    word_freq_tuples = sorted(word_freq.items(), key=get_word)

    # Sorts the list of tuples by word frequency and takes the top ten words
    def get_frequency_value(word_tup):
        """Given a tuple, returns the second value"""
        return word_tup[1]
    top_ten = sorted(word_freq_tuples, key=get_frequency_value, reverse=True)[:10]

    # Prints the results in the "bar graph" format
    # find the length of the longest word
    longest_word_length = 0
    for word_tuple in top_ten:
        if len(word_tuple[0]) > longest_word_length:
            longest_word_length = len(word_tuple[0])

    # find the length of the string of the longest number
    longest_number_length = len(str(top_ten[0][1]))

    # print each line formatted with * for each use
    # AREA FOR IMPROVEMENT: I would like to be able to do this more 
    # cleanly with string functions
    # for final_tup in top_ten:
    #     # empty the string for a new line
    #     full_line = ""
    #     # add space so each word ends at the same place
    #     full_line += (" " * (longest_word_length - len(
    #         final_tup[0]))) + final_tup[0]
    #     # add the word, a pipe, and the frequency
    #     full_line += " | " + str(final_tup[1])
    #     # add white space so the 'bar' starts at the same place 
    #     # and make the bar with an '*' for each time it was used
    #     full_line += (" " * (1 + longest_number_length - len(
    #         str(final_tup[1])))) + ("*" * final_tup[1])
    #     # print the fully formed line
    #     print(full_line)
    
    # IMPROVED VERSION
    word_padding = longest_word_length + 1
    bar_padding = len(str(top_ten[0][1])) + 1
    for final_tup in top_ten:
        full_line = ""
        full_line = ("{:>"+str(word_padding)+"}").format(
            final_tup[0]) + " | " + ("{:<"+str(bar_padding)+"}").format(final_tup[1]) + " " + ("*"*final_tup[1])
        print(full_line)

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
