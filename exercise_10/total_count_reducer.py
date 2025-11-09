#!/usr/bin/env python3
import sys

def main():
    total = 0
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            key, count_str = line.split('\t')
            if key == "total":
                total += int(count_str)
        except (ValueError, IndexError):
            continue
    
    print(total)

if __name__ == "__main__":
    main()




