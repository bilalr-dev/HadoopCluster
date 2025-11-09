#!/usr/bin/env python3
import sys
import os

def main():
    potential_friends = set()
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            category, user = line.split('\t', 1)
            if category == "potential":
                potential_friends.add(user)
        except (ValueError, IndexError):
            continue
    
    if potential_friends:
        print(' '.join(sorted(potential_friends)))

if __name__ == "__main__":
    main()
