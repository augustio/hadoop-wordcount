#!/usr/bin/env pytho

import sys

for line in sys.stdin:
    words_temp = line.strip().split()
    words = dict()

    for word in words_temp:
        word = word.lower()
        if word in words:
            words[word].append(1)
        else:
            words[word] = [1]
    for key in words:
        print(str(key) + " " + str(words[key]))
