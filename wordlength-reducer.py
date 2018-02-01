#!/usr/bin/env python

import sys
import collections

c_3 = 0
c_5 = 0

for line in sys.stdin:
    word, c = line.strip().split(" ", 1)
    if(len(word) == 5):
        c_5 += 1
    else:
        c_3 += 1

print("Five character words (length = 5): " + str(c_5))
print("Three character words (length = 3): " + str(c_3))
