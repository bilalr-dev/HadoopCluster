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
            
            year_month = date[:7]
            print(f"{year_month}\t{income}")
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()




