#!/usr/bin/env python3
import sys
import re

def process_line(line):
    line = line.strip()
    if not line:
        return
    
    parts = line.split(',')
    
    if len(parts) == 7:
        user_id = parts[0].strip()
        name = parts[1].strip()
        surname = parts[2].strip()
        gender = parts[3].strip()
        year_of_birth = parts[4].strip()
        city = parts[5].strip()
        education = parts[6].strip()
        print(f"{user_id}\tU\t{gender}\t{year_of_birth}")
    elif len(parts) == 2:
        user_id = parts[0].strip()
        movie_genre = parts[1].strip()
        print(f"{user_id}\tL\t{movie_genre}")
    elif len(parts) > 7:
        potential_split = re.search(r'^(User#[^,]+(?:,[^,]+){5},[^,]+)(User#)', line)
        if potential_split:
            first_part = potential_split.group(1)
            remaining = potential_split.group(2) + line[len(potential_split.group(0)):]
            process_line(first_part)
            process_line(remaining)
        else:
            potential_split = re.search(r'^(User#[^,]+(?:,[^,]+){5},[^,]+)(User#[^,]+,[^,]+)', line)
            if potential_split:
                first_part = potential_split.group(1)
                remaining = potential_split.group(2)
                process_line(first_part)
                process_line(remaining)

def main():
    buffer = ""
    
    for chunk in sys.stdin:
        buffer += chunk
        while '\n' in buffer:
            line, buffer = buffer.split('\n', 1)
            process_line(line)
    
    if buffer.strip():
        process_line(buffer)

if __name__ == "__main__":
    main()

