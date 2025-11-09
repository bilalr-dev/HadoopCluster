#!/usr/bin/env python3
import sys
import os

def main():
    if 'TARGET_USER' not in os.environ:
        sys.stderr.write("Error: TARGET_USER environment variable not provided. Use: TARGET_USER=username python3 potential_friends_mapper.py\n")
        sys.exit(1)
    
    target_user = os.environ['TARGET_USER']
    
    friendships = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        if len(parts) != 2:
            continue
        
        user1 = parts[0].strip()
        user2 = parts[1].strip()
        friendships.append((user1, user2))
    
    target_friends = set()
    for user1, user2 in friendships:
        if user1 == target_user:
            target_friends.add(user2)
            print(f"direct\t{user2}")
        elif user2 == target_user:
            target_friends.add(user1)
            print(f"direct\t{user1}")
    
    all_users = set()
    for user1, user2 in friendships:
        all_users.add(user1)
        all_users.add(user2)
    
    for user in all_users:
        if user == target_user:
            continue
        
        user_friends = set()
        for user1, user2 in friendships:
            if user1 == user:
                user_friends.add(user2)
            elif user2 == user:
                user_friends.add(user1)
        
        common_friends = target_friends.intersection(user_friends)
        if common_friends:
            print(f"potential\t{user}")

if __name__ == "__main__":
    main()




