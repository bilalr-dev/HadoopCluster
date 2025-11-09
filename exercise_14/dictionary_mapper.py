#!/usr/bin/env python3
import sys
import re

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        words = re.findall(r'\b\w+\b', line.lower())
        
        for word in words:
            print(word)

if __name__ == "__main__":
    main()




