#!/usr/bin/env python3
import sys

def main():
    current_user = None
    potential_friends = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            user, potential_friend = line.split('\t', 1)
            
            if user != current_user:
                if current_user is not None and potential_friends:
                    print(f"{current_user}: {' '.join(sorted(potential_friends))}")
                current_user = user
                potential_friends = [potential_friend]
            else:
                potential_friends.append(potential_friend)
        except (ValueError, IndexError):
            continue
    
    if current_user is not None and potential_friends:
        print(f"{current_user}: {' '.join(sorted(potential_friends))}")

if __name__ == "__main__":
    main()


