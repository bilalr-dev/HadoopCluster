#!/usr/bin/env python3
import sys

def main():
    zone_dates = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            zone_id, date = line.split('\t')
            if zone_id not in zone_dates:
                zone_dates[zone_id] = []
            zone_dates[zone_id].append(date)
        except (ValueError, IndexError):
            continue
    
    sorted_zones = sorted(zone_dates.items(), key=lambda x: x[0])
    
    for zone_id, dates in sorted_zones:
        dates_str = ', '.join(dates)
        print(f"{zone_id}\t[{dates_str}]")

if __name__ == "__main__":
    main()

