#!/usr/bin/env python3
import sys
import os

def main():
    threshold = None
    
    if len(sys.argv) > 1:
        threshold = float(sys.argv[1])
    elif 'THRESHOLD' in os.environ:
        threshold = float(os.environ['THRESHOLD'])
    else:
        sys.stderr.write("Error: Threshold not provided. Use: python3 select_outliers_mapper.py <threshold>\n")
        sys.exit(1)
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split('\t')
        if len(parts) != 2:
            continue
        
        try:
            sensor_date = parts[0]
            pm10_str = parts[1].split()[0]
            pm10_value = float(pm10_str)
            
            if pm10_value < threshold:
                print(line)
        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()
