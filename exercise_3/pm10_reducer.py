#!/usr/bin/env python3
import sys

def main():
    sensor_counts = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            sensor_id, count = line.split('\t')
            sensor_counts[sensor_id] = sensor_counts.get(sensor_id, 0) + int(count)
        except (ValueError, IndexError):
            continue
    
    sorted_sensors = sorted(sensor_counts.items(), key=lambda x: x[0])
    
    for sensor_id, count in sorted_sensors:
        print(f"{sensor_id}\t{count}")

if __name__ == "__main__":
    main()




