# Exercise 5: PM10 Average

## Overview

Calculate the average PM10 pollution value for each sensor across all dates.

**Input**: CSV file with format `sensorId,date,PM10_value`  
**Output**: `(sensorId, average)` - average PM10 per sensor

## Example

**Input**:
```
s1,2016-01-01,20.5
s2,2016-01-01,30.1
s1,2016-01-02,60.2
s2,2016-01-02,20.4
s1,2016-01-03,55.5
s2,2016-01-03,52.5
```

**Output**:
```
s1	45.4
s2	34.3
```

Sensor s1: (20.5 + 60.2 + 55.5) / 3 = 45.4  
Sensor s2: (30.1 + 20.4 + 52.5) / 3 = 34.3

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_5/pm10_average_input.txt /user/$USER/exercises/input/exercise_5/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_5/pm10_average_mapper.py \
  -reducer exercise_5/pm10_average_reducer.py \
  -file exercise_5/pm10_average_mapper.py \
  -file exercise_5/pm10_average_reducer.py \
  -input "/user/$USER/exercises/input/exercise_5/*" \
  -output "/user/$USER/exercises/output/exercise_5"
```

Check the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_5/part-00000
```

## Files

- `pm10_average_mapper.py` - Parses CSV, extracts sensor ID and PM10 value
- `pm10_average_reducer.py` - Calculates average PM10 for each sensor
