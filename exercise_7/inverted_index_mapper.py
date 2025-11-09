#!/usr/bin/env python3
import sys
import re

STOP_WORDS = {'and', 'or', 'not'}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split('\t', 1)
        if len(parts) != 2:
            continue
        
        sentence_id = parts[0]
        sentence = parts[1].lower()
        
        words = re.findall(r'\b\w+\b', sentence)
        
        for word in words:
            if word not in STOP_WORDS:
                print(f"{word}\t{sentence_id}")

if __name__ == "__main__":
    main()




