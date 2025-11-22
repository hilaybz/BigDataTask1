#!/usr/bin/env python
"""mapper.py"""

import sys

def read_input(file):
    for line in file:
        yield line.split()

def clean_word(word):
    # convert to lowercase
    word = word.lower()
    # strip trailing commas and dots
    return word.rstrip(',.')
    
def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            cleaned = clean_word(word)
            if cleaned:  # avoid empty strings
                print('%s%s%d' % (cleaned, separator, 1))

if __name__ == "__main__":
    main()
