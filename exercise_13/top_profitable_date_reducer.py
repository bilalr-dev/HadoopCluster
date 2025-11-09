#!/usr/bin/env python3
import sys

def main():
    max_income = float('-inf')
    top_date = None
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            date, income_str = line.split('\t')
            income = float(income_str)
            
            if income > max_income:
                max_income = income
                top_date = date
        except (ValueError, IndexError):
            continue
    
    if top_date is not None:
        print(f"{top_date}\t{int(max_income)}")

if __name__ == "__main__":
    main()




