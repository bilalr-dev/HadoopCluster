#!/usr/bin/env python3
import sys

def parse_position(position_str):
    parts = position_str.split(':')
    return (int(parts[0]), int(parts[1]))

def main():
    word_data = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            word, position_str = line.split('\t', 1)
            position = parse_position(position_str)
            
            if word in word_data:
                first_pos, count = word_data[word]
                if position < first_pos:
                    first_pos = position
                word_data[word] = (first_pos, count + 1)
            else:
                word_data[word] = (position, 1)
                
        except (ValueError, IndexError):
            continue
    
    sorted_words = sorted(word_data.items(), key=lambda x: x[0])
    
    for word, (position, count) in sorted_words:
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
