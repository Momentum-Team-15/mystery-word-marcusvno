# -*- coding: utf-8 -*-
import string
from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has','he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were', 'will', 'with' # noqa
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as target:
        txt_string = target.read()
        txt_string = txt_string.strip()
        txt_string = txt_string.translate(str.maketrans('', '', string.punctuation)).casefold() # noqa
        txt_list = txt_string.split()

        new_list = [word for word in txt_list if word not in STOP_WORDS]
        counts = Counter(new_list)
        count_ordered = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)) # noqa
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
