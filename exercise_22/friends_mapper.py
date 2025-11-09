#!/usr/bin/env python3
import sys
import os

def main():
    if 'TARGET_USER' not in os.environ:
        sys.stderr.write("Error: TARGET_USER environment variable not provided. Use: TARGET_USER=username python3 friends_mapper.py\n")
        sys.exit(1)
    
    target_user = os.environ['TARGET_USER']
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        if len(parts) != 2:
            continue
        
        user1 = parts[0].strip()
        user2 = parts[1].strip()
        
        if user1 == target_user:
            print(user2)
        elif user2 == target_user:
            print(user1)

if __name__ == "__main__":
    main()

