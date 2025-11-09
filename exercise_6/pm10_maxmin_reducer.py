#!/usr/bin/env python3
import sys

def main():
    sensor_values = {}
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            sensor_id, pm10_str = line.split('\t')
            pm10_value = float(pm10_str)
            
            if sensor_id not in sensor_values:
                sensor_values[sensor_id] = []
            sensor_values[sensor_id].append(pm10_value)
        except (ValueError, IndexError):
            continue
    
    sorted_sensors = sorted(sensor_values.items(), key=lambda x: x[0])
    
    for sensor_id, values in sorted_sensors:
        max_value = max(values)
        min_value = min(values)
        print(f"{sensor_id}\tmax={max_value}_min={min_value}")

if __name__ == "__main__":
    main()




