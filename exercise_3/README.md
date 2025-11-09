# Exercise 3: PM10 Pollution Analysis

## Overview

Count how many days each sensor recorded PM10 pollution above 50 μg/m³. Only sensors that have at least one day above the threshold are included in the output.

**Input**: File with format `sensorId,date\tPM10_value`  
**Output**: `(sensorId, count)` - how many days above threshold for each sensor

## Example

**Input**:
```
s1,2016-01-01	20.5
s2,2016-01-01	30.1
s1,2016-01-02	60.2
s2,2016-01-02	20.4
s1,2016-01-03	55.5
s2,2016-01-03	52.5
```

**Output**:
```
s1	2
s2	1
```

Sensor s1 had 2 days above 50 (60.2 and 55.5), and s2 had 1 day (52.5).

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_3/pm10_input.txt /user/$USER/exercises/input/exercise_3/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_3/pm10_mapper.py \
  -reducer exercise_3/pm10_reducer.py \
  -file exercise_3/pm10_mapper.py \
  -file exercise_3/pm10_reducer.py \
  -input "/user/$USER/exercises/input/exercise_3/*" \
  -output "/user/$USER/exercises/output/exercise_3"
```

Check the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_3/part-00000
```

## Files

- `pm10_mapper.py` - Filters records where PM10 > 50, emits `sensorId\t1`
- `pm10_reducer.py` - Counts how many days each sensor exceeded the threshold

The threshold is 50 μg/m³ (hardcoded in the mapper)
