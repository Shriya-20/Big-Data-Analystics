#!/usr/bin/env python3
import sys
import os
import re

STOP_WORDS = {"is", "and", "are"}  # Define stop words

for line in sys.stdin:
    file_name = os.getenv('map_input_file', 'unknown.txt')  # Get file name
    doc_id = os.path.basename(file_name).split('.')[0]  # Extract DocID

    words = re.findall(r"\b\w+\b", line.lower())  # Extract words

    for word in words:
        if word not in STOP_WORDS:
            print(f"{word.capitalize()}\t{doc_id}")  # Capitalize words for consistency

