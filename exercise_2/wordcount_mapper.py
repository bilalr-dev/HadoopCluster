#!/usr/bin/env python3
import sys
import re

def main():
    line_number = 0
    
    for line in sys.stdin:
        line_number += 1
        line = line.strip()
        
        if not line:
            continue
        
        words = re.findall(r'\b\w+\b', line.lower())
        
        for word_pos, word in enumerate(words, start=1):
            print(f"{word}\t{line_number}:{word_pos}:1")

if __name__ == "__main__":
    main()
