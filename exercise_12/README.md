# Exercise 12: Select Outliers

## Overview

This filters records where PM10 pollution is below a threshold. This is a map-only job, so no reducer is needed.

**Input**: Files with format `sensorId,date\tPM10_value` (can be CSV or TXT)  
**Output**: Records with PM10 < threshold (in original format)

## Example

**Input** (multiple files):
```
s1,2016-01-01	20.5
s2,2016-01-01	60.2
s1,2016-01-02	30.1
s2,2016-01-02	20.4
```

The threshold is 21

**Output**:
```
s1,2016-01-01	20.5
s2,2016-01-02	20.4
```

Only records with PM10 < 21 are kept.

## Running on Hadoop

Upload the input files to HDFS:

```bash
hdfs dfs -put exercise_12/select_outliers_file*.csv exercise_12/select_outliers_file*.txt /user/$USER/exercises/input/exercise_12/
```

Run the job (map-only, no reducer):

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_12/select_outliers_mapper.py \
  -file exercise_12/select_outliers_mapper.py \
  -cmdenv THRESHOLD=21 \
  -input "/user/$USER/exercises/input/exercise_12/*" \
  -output "/user/$USER/exercises/output/exercise_12"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_12/part-00000
```

**Important:** Make sure to change `THRESHOLD=21` to your desired threshold value.

## Files

- `select_outliers_mapper.py` - Filters records with PM10 < threshold
- Input files can be CSV or TXT - format is the same
