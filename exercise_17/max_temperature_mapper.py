#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        
        if len(parts) == 4:
            try:
                if parts[0].startswith('s'):
                    sensor_id, date, hour, temperature = parts
                    temp_value = float(temperature)
                    print(f"{date}\t{temp_value}")
                else:
                    date, hour, temperature, sensor_id = parts
                    temp_value = float(temperature)
                    print(f"{date}\t{temp_value}")
            except (ValueError, IndexError):
                continue

if __name__ == "__main__":
    main()




