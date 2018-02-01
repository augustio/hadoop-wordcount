#!/usr/bin/env python

import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        wordLower = word.lower()
        if(len(wordLower) == 3 or len(wordLower) == 5):
            print('%s%s%d' % (wordLower, " ", 1))
