#!/usr/bin/env python3
import sys

def main():
    year_data = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            year, total_str = line.split('\t')
            total = float(total_str)
            
            if year not in year_data:
                year_data[year] = {'sum': 0, 'count': 0}
            
            year_data[year]['sum'] += total
            year_data[year]['count'] += 1
        except (ValueError, IndexError):
            continue
    
    sorted_years = sorted(year_data.items(), key=lambda x: x[0])
    
    for year, data in sorted_years:
        if data['count'] > 0:
            average = data['sum'] / data['count']
            print(f"{year}\t{average:.1f}")

if __name__ == "__main__":
    main()




