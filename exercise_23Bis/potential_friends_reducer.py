#!/usr/bin/env python3
import sys
import os

def main():
    direct_friends = set()
    potential_friends = set()
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            category, user = line.split('\t', 1)
            if category == "direct":
                direct_friends.add(user)
            elif category == "potential":
                potential_friends.add(user)
        except (ValueError, IndexError):
            continue
    
    result = potential_friends.difference(direct_friends)
    
    if result:
        print(' '.join(sorted(result)))

if __name__ == "__main__":
    main()




