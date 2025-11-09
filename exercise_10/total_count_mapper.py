#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        if len(parts) == 3:
            print("total\t1")

if __name__ == "__main__":
    main()




