#!/usr/bin/env python3
import sys

def main():
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
    
    all_users = set()
    for user1, user2 in friendships:
        all_users.add(user1)
        all_users.add(user2)
    
    user_friends = {}
    for user1, user2 in friendships:
        if user1 not in user_friends:
            user_friends[user1] = set()
        if user2 not in user_friends:
            user_friends[user2] = set()
        user_friends[user1].add(user2)
        user_friends[user2].add(user1)
    
    for user in all_users:
        if user not in user_friends:
            continue
        
        friends = user_friends[user]
        for other_user in all_users:
            if other_user == user:
                continue
            
            if other_user not in user_friends:
                continue
            
            other_friends = user_friends[other_user]
            common_friends = friends.intersection(other_friends)
            
            if common_friends:
                print(f"{user}\t{other_user}")

if __name__ == "__main__":
    main()




