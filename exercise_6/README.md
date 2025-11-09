# Exercise 6: PM10 Max and Min

## Overview

Find the highest and lowest PM10 pollution values for each sensor across all dates.

**Input**: CSV file with format `sensorId,date,PM10_value`  
**Output**: `(sensorId, max=X_min=Y)` - maximum and minimum values per sensor

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
s1	max=60.2_min=20.5
s2	max=52.5_min=20.4
```

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_6/pm10_maxmin_input.txt /user/$USER/exercises/input/exercise_6/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_6/pm10_maxmin_mapper.py \
  -reducer exercise_6/pm10_maxmin_reducer.py \
  -file exercise_6/pm10_maxmin_mapper.py \
  -file exercise_6/pm10_maxmin_reducer.py \
  -input "/user/$USER/exercises/input/exercise_6/*" \
  -output "/user/$USER/exercises/output/exercise_6"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_6/part-00000
```

## Files

- `pm10_maxmin_mapper.py` - Parses CSV, extracts sensor ID and PM10 value
- `pm10_maxmin_reducer.py` - Finds the maximum and minimum PM10 for each sensor
