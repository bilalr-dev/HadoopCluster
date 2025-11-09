#!/usr/bin/env python3
import sys

def main():
    current_user_id = None
    user_info = None
    liked_genres = set()
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            parts = line.split('\t')
            if len(parts) < 3:
                continue
            
            user_id = parts[0]
            record_type = parts[1]
            
            if user_id != current_user_id:
                if current_user_id is not None and user_info:
                    gender, year_of_birth = user_info
                    if "Commedia" in liked_genres and "Adventure" in liked_genres:
                        print(f"{gender},{year_of_birth}")
                
                current_user_id = user_id
                user_info = None
                liked_genres = set()
            
            if record_type == "U":
                gender = parts[2]
                year_of_birth = parts[3]
                user_info = (gender, year_of_birth)
            elif record_type == "L":
                genre = parts[2]
                liked_genres.add(genre)
        except (ValueError, IndexError):
            continue
    
    if current_user_id is not None and user_info:
        gender, year_of_birth = user_info
        if "Commedia" in liked_genres and "Adventure" in liked_genres:
            print(f"{gender},{year_of_birth}")

if __name__ == "__main__":
    main()


