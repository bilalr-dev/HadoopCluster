#!/usr/bin/env python3
import sys

def main():
    month_totals = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            year_month, income_str = line.split('\t')
            income = float(income_str)
            month_totals[year_month] = month_totals.get(year_month, 0) + income
        except (ValueError, IndexError):
            continue
    
    sorted_months = sorted(month_totals.items(), key=lambda x: x[0])
    
    for year_month, total in sorted_months:
        print(f"{year_month}\t{int(total)}")

if __name__ == "__main__":
    main()




