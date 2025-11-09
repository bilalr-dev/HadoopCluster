#!/usr/bin/env python3
import sys
import re

def main():
    word_counts = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        words = re.findall(r'\b\w+\b', line.lower())
        
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    for word, count in sorted(word_counts.items()):
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()




