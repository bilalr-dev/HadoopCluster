# Exercise 20: Split Temperature Readings

## Overview

Split temperature readings into two categories based on a threshold (30.0):
- High temperatures (> 30.0) go to "high-temp" category
- Normal temperatures (<= 30.0) go to "normal-temp" category

This is a map-only job, so no reducer is needed.

**Input**: Files with format `sensorID,date,hour,temperature`  
**Output**: Records categorized as "high-temp" or "normal-temp"

## Example

**Input**:
```
s1,2016-01-01,14:00,20.5
s2,2016-01-01,14:00,30.2
s1,2016-01-02,14:10,11.5
s2,2016-01-02,14:10,30.2
```

**Output** (in Hadoop, you'll see categorized output):
```
high-temp	s2,2016-01-01,14:00,30.2
high-temp	s2,2016-01-02,14:10,30.2
normal-temp	s1,2016-01-01,14:00,20.5
normal-temp	s1,2016-01-02,14:10,11.5
```

## Running on Hadoop

Upload the input files to HDFS:

```bash
hdfs dfs -put exercise_20/temperature_split_file*.csv /user/$USER/exercises/input/exercise_20/
```

Run the job (map-only):

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_20/temperature_split_mapper.py \
  -file exercise_20/temperature_split_mapper.py \
  -input "/user/$USER/exercises/input/exercise_20/*" \
  -output "/user/$USER/exercises/output/exercise_20"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_20/part-00000
```

## Files

- `temperature_split_mapper.py` - Routes lines to "high-temp" or "normal-temp" based on temperature
- `split_output.py` - Helper script for local testing (splits output into separate files)

The threshold is 30.0 (hardcoded in mapper)
