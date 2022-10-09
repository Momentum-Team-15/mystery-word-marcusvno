# -*- coding: utf-8 -*-
# import string (used for translate method)
import re
from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has','he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were', 'will', 'with' # noqa
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as target:
        # read the target file and convert to string
        txt_string = target.read()

        # removes punctuation from string using translate. Has issues with em/en-dashes # noqa
        # txt_string = txt_string.translate(str.maketrans('', '', string.punctuation)).casefold() # noqa

        # remove punctuation but first keeps words with apostrophes together (to avoid orphaned 's') and then replaces remaining punctuation with spaces (to deal with dashes) # noqa
        txt_string = txt_string.replace("'", "")
        txt_string = re.sub(r'[^\w\s]', ' ', txt_string)

        # strip string of whitespace and lowercases text
        txt_string = txt_string.strip().casefold()

        # transforms string into list to be counted and sorted
        txt_list = txt_string.split()

        # creates new list removing all the STOP_WORDS
        new_list = [word for word in txt_list if word not in STOP_WORDS]

        # creates dictionary and counts frequency of unique words
        counts = Counter(new_list)

        # creates new dictionary with descending order of value
        count_ordered = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)) # noqa

        # Formats print statement to reqs
        for key, value in count_ordered.items():
            counter_mark = ''
            i = 0
            while i < value:
                counter_mark += '*'
                i += 1
            print(f'{key} |'.rjust(20), value, counter_mark)


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
