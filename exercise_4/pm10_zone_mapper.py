#!/usr/bin/env python3
import sys

THRESHOLD = 50.0

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split('\t')
        if len(parts) != 2:
            continue
        
        zone_date = parts[0]
        pm10_str = parts[1].split()[0]
        
        try:
            pm10_value = float(pm10_str)
            if pm10_value > THRESHOLD:
                zone_id, date = zone_date.split(',')
                print(f"{zone_id}\t{date}")
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()




