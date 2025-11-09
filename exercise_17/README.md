# Exercise 17: Maximum Temperature per Date

## Overview

Find the maximum temperature for each date, combining data from two files with different formats. The mapper automatically detects which format each line uses.

**Input**: Two files with different formats:
- File 1: `sensorID,date,hour,temperature`
- File 2: `date,hour,temperature,sensorID`

**Output**: `date\ttemperature` - maximum temperature per date

## Example

**Input File 1**:
```
s1,2016-01-01,14:00,20.5
s2,2016-01-01,14:00,30.2
s1,2016-01-02,14:10,11.5
```

**Input File 2**:
```
2016-01-01,14:00,20.1,s3
2016-01-01,14:00,10.2,s4
2016-01-02,14:15,31.5,s3
```

**Output**:
```
2016-01-01	30.2
2016-01-02	31.5
```

For 2016-01-01, the max is 30.2 (from file 1). For 2016-01-02, the max is 31.5 (from file 2).

## Running on Hadoop

Upload both input files to HDFS:

```bash
hdfs dfs -put exercise_17/temperature_file*.csv /user/$USER/exercises/input/exercise_17/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_17/max_temperature_mapper.py \
  -reducer exercise_17/max_temperature_reducer.py \
  -file exercise_17/max_temperature_mapper.py \
  -file exercise_17/max_temperature_reducer.py \
  -input "/user/$USER/exercises/input/exercise_17/*" \
  -output "/user/$USER/exercises/output/exercise_17"
```

Check the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_17/part-00000
```

## Files

- `max_temperature_mapper.py` - Detects file format automatically and extracts date and temperature
- `max_temperature_reducer.py` - Finds maximum temperature per date
