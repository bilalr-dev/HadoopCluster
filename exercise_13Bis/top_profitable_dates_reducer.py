#!/usr/bin/env python3
import sys

def main():
    date_income_pairs = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            date, income_str = line.split('\t')
            income = float(income_str)
            date_income_pairs.append((date, income))
        except (ValueError, IndexError):
            continue
    
    if date_income_pairs:
        sorted_pairs = sorted(date_income_pairs, key=lambda x: (-x[1], x[0]))
        
        for i in range(min(2, len(sorted_pairs))):
            date, income = sorted_pairs[i]
            print(f"{date}\t{int(income)}")

if __name__ == "__main__":
    main()

