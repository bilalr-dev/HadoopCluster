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
            year_month = parts[0]
            total = float(parts[1])
            
            if total > 0:
                year = year_month[:4]
                print(f"{year}\t{total}")
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()




