#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split('\t')
        if len(parts) != 2:
            continue
        
        try:
            date = parts[0]
            income = float(parts[1])
            print(f"{date}\t{income}")
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()

