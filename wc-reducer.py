#!/usr/bin/env python

import sys
import collections

current_word = None
current_count = 0
word = None
counters = collections.Counter()

for line in sys.stdin:
    word, count = line.strip().split("\t", 1)

    try:
        count = int(count)
    except ValueError:
        continue

    counters[word] += int(count)

for count in counters.most_common(100):
    print(str(count[0]) + " " + str(count[1]))
