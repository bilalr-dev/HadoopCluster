# Exercise 19: Filter Temperature Readings (<= 30.0)

## Overview

Filter temperature readings to keep only those with temperature less than or equal to 30.0. This is a map-only job, so no reducer is needed.

**Input**: Files with format `sensorID,date,hour,temperature`  
**Output**: Lines with temperature <= 30.0 (in original format)

## Example

**Input** (multiple files):
```
s1,2016-01-01,14:00,20.5
s2,2016-01-01,14:00,30.2
s1,2016-01-02,14:10,11.5
s2,2016-01-02,14:10,30.2
```

**Output**:
```
s1,2016-01-01,14:00,20.5
s1,2016-01-02,14:10,11.5
```

Only temperatures <= 30.0 are kept. Values like 30.2 are filtered out.

## Running on Hadoop

Upload the input files to HDFS:

```bash
hdfs dfs -put exercise_19/temperature_filter_file*.csv /user/$USER/exercises/input/exercise_19/
```

Run the job (map-only, no reducer):

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_19/temperature_filter_mapper.py \
  -file exercise_19/temperature_filter_mapper.py \
  -input "/user/$USER/exercises/input/exercise_19/*" \
  -output "/user/$USER/exercises/output/exercise_19"
```

Check the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_19/part-00000
```

## Files

- `temperature_filter_mapper.py` - Filters lines with temperature <= 30.0

The threshold is 30.0 (hardcoded in mapper). Only temperatures <= 30.0 are included.
