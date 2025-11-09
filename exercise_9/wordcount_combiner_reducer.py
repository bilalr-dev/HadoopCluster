#!/usr/bin/env python3
import sys

def main():
    word_counts = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            word, count_str = line.split('\t')
            count = int(count_str)
            word_counts[word] = word_counts.get(word, 0) + count
        except (ValueError, IndexError):
            continue
    
    sorted_words = sorted(word_counts.items(), key=lambda x: x[0])
    
    for word, count in sorted_words:
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()




