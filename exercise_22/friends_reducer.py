#!/usr/bin/env python3
import sys

def main():
    friends = []
    
    for line in sys.stdin:
        line = line.strip()
        if line:
            friends.append(line)
    
    if friends:
        print(' '.join(sorted(friends)))

if __name__ == "__main__":
    main()




