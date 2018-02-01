#!/usr/bin/env python

import sys
import collections

counters = collections.Counter()

for line in sys.stdin:
    word, freq = line.strip().split(" ", 1)
    for key in list(freq):
       if key == "1":
            counters[word] += int(key)
        

for c in counters.most_common(100):
    print(str(c[0]) + " " + str(c[1]))
