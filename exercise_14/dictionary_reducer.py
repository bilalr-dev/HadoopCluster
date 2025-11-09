#!/usr/bin/env python3
import sys

def main():
    distinct_words = set()
    
    for line in sys.stdin:
        line = line.strip()
        if line:
            distinct_words.add(line)
    
    sorted_words = sorted(distinct_words)
    
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()




