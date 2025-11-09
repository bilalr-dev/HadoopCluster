#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        
        if len(parts) == 3:
            question_id = parts[0].strip()
            timestamp = parts[1].strip()
            text = parts[2].strip()
            print(f"{question_id}\tQ\t{text}")
        elif len(parts) == 4:
            answer_id = parts[0].strip()
            question_id = parts[1].strip()
            timestamp = parts[2].strip()
            text = parts[3].strip()
            print(f"{question_id}\tA\t{answer_id}\t{text}")

if __name__ == "__main__":
    main()




