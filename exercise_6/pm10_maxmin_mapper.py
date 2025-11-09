#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        if len(parts) != 3:
            continue
        
        try:
            sensor_id = parts[0]
            pm10_value = float(parts[2])
            print(f"{sensor_id}\t{pm10_value}")
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()


