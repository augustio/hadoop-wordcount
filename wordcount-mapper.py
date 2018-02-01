#!/usr/bin/env python

import sys

for line in sys.stdin:
    words = line.strip().split()

    for word in words:
        word_lower = word.lower()
        print('%s%s%d' % (word_lower, "\t", 1))
