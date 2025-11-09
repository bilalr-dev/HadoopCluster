#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        if len(parts) != 2:
            continue
        
        user1 = parts[0].strip()
        user2 = parts[1].strip()
        
        print(f"{user1}\t{user2}")
        print(f"{user2}\t{user1}")

if __name__ == "__main__":
    main()




