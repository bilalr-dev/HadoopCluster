#!/usr/bin/env python3
import sys

def main():
    date_temps = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            date, temp_str = line.split('\t')
            temp_value = float(temp_str)
            
            if date not in date_temps:
                date_temps[date] = temp_value
            else:
                if temp_value > date_temps[date]:
                    date_temps[date] = temp_value
        except (ValueError, IndexError):
            continue
    
    sorted_dates = sorted(date_temps.items(), key=lambda x: x[0])
    
    for date, max_temp in sorted_dates:
        print(f"{date}\t{max_temp}")

if __name__ == "__main__":
    main()




