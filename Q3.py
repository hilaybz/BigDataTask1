#!/usr/bin/env python
"""reducer.py"""

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    # dictionary of words to number 
    counts = {}

    # groupby expects the data to be sorted by key (Hadoop guarantees that)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            counts[current_word] = total_count
        except ValueError:
            pass

    # get top 3 words by count (descending)
    top3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]

    # print only the top 3
    for word, total_count in top3:
        print("%s%s%d" % (word, separator, total_count))

if __name__ == "__main__":
    main()
