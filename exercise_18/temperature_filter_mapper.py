#!/usr/bin/env python3
import sys

THRESHOLD = 30.0

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(',')
        if len(parts) != 4:
            continue
        
        try:
            sensor_id = parts[0]
            date = parts[1]
            hour = parts[2]
            temperature = float(parts[3])
            
            if temperature > THRESHOLD:
                print(line)
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()




