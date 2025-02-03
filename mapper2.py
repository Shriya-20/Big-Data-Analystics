#!/usr/bin/env python3
import sys
import re

# Define stop words to ignore
STOP_WORDS = {"is", "the", "a", "and", "with", "this"}

for line in sys.stdin:
    words = re.findall(r"\b\w+\b", line.lower())  # Extract words (case insensitive)

    for word in words:
        if word not in STOP_WORDS:
            print(f"{word.capitalize()}\t1")  # Capitalize for consistent output

