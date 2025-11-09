#!/usr/bin/env python3
import sys

def main():
    current_user = None
    friends = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            user, friend = line.split('\t', 1)
            
            if user != current_user:
                if current_user is not None:
                    print(f"{current_user}: {' '.join(sorted(friends))}")
                current_user = user
                friends = [friend]
            else:
                friends.append(friend)
        except (ValueError, IndexError):
            continue
    
    if current_user is not None:
        print(f"{current_user}: {' '.join(sorted(friends))}")

if __name__ == "__main__":
    main()

