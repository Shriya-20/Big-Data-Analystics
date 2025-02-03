#!/usr/bin/env python3
import sys

current_word = None
doc_set = set()  # Use a set to store unique document IDs

for line in sys.stdin:
    word, doc_id = line.strip().split("\t")

    if current_word and current_word != word:
        print(f"{current_word}\t{','.join(sorted(doc_set))}")  # Print previous word's docs
        doc_set.clear()

    current_word = word
    doc_set.add(doc_id)

# Print last word's document list
if current_word:
    print(f"{current_word}\t{','.join(sorted(doc_set))}")

