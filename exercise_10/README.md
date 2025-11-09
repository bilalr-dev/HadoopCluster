# Exercise 10: Total Count

## Overview

Count the total number of records in a collection of CSV files. Simple but useful for data validation.

**Input**: CSV files with format `sensorId,date,PM10_value`  
**Output**: A single number - the total count of records

## Example

**Input**:
```
s1,2016-01-01,20.5
s2,2016-01-01,60.2
s1,2016-01-02,30.1
s2,2016-01-02,20.4
s1,2016-01-03,55.5
s2,2016-01-03,52.5
```

**Output**:
```
6
```

There are 6 records total.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_10/total_count_input.csv /user/$USER/exercises/input/exercise_10/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_10/total_count_mapper.py \
  -reducer exercise_10/total_count_reducer.py \
  -file exercise_10/total_count_mapper.py \
  -file exercise_10/total_count_reducer.py \
  -input "/user/$USER/exercises/input/exercise_10/*" \
  -output "/user/$USER/exercises/output/exercise_10"
```

Check the result:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_10/part-00000
```

## Files

- `total_count_mapper.py` - Validates CSV format (3 fields), emits `total\t1` for each valid record
- `total_count_reducer.py` - Sums all the counts to get the total
