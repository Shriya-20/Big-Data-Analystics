#!/usr/bin/env python3
import sys

current_word = None
total_count = 0

for line in sys.stdin:
    word, count = line.strip().split("\t")
    count = int(count)

    if current_word and current_word != word:
        print(f"{current_word}\t{total_count}")
        total_count = count
    else:
        total_count += count

    current_word = word

# Print last word count
if current_word:
    print(f"{current_word}\t{total_count}")

