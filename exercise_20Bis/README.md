# Exercise 20 Bis: Split Temperature Readings (Modified Output)

## Overview

Similar to Exercise 20, but with different output formats:
- High temperatures (> 30.0): Output only the temperature value
- Normal temperatures (<= 30.0): Output the full line

This is a map-only job, so no reducer is needed.

**Input**: File with format `sensorID,date,hour,temperature`  
**Output**: Different formats based on temperature category

## Example

**Input**:
```
s1,2016-01-01,14:00,20.5
s2,2016-01-01,14:00,30.2
s1,2016-01-02,14:10,11.5
s2,2016-01-02,14:10,41.5
```

**Output**:
```
high-temp	30.2
high-temp	41.5
normal-temp	s1,2016-01-01,14:00,20.5
normal-temp	s1,2016-01-02,14:10,11.5
```

High temps show only the value, normal temps show the full line.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_20Bis/temperature_split_input.csv /user/$USER/exercises/input/exercise_20Bis/
```

Run the job (map-only):

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_20Bis/temperature_split_mapper.py \
  -file exercise_20Bis/temperature_split_mapper.py \
  -input "/user/$USER/exercises/input/exercise_20Bis/*" \
  -output "/user/$USER/exercises/output/exercise_20Bis"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_20Bis/part-00000
```

## Files

- `temperature_split_mapper.py` - Routes to "high-temp" (temperature only) or "normal-temp" (full line)
- `split_output.py` - Helper script for local testing

**Difference from Exercise 20**: High-temp outputs only temperature value, normal-temp outputs full line.
