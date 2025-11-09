# Exercise 13: Top 1 Most Profitable Date

## Overview

Find the single date with the highest daily income. If multiple dates have the same maximum income, the first one encountered is selected.

**Input**: CSV file with format `date\tdaily_income`  
**Output**: `date\tincome` - the most profitable date

## Example

**Input**:
```
2015-11-01	1000
2015-11-02	1305
2015-12-01	500
2015-12-02	750
2016-01-01	345
2016-01-02	1145
```

**Output**:
```
2015-11-02	1305
```

2015-11-02 has the highest income (1305).

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_13/top_profitable_date_input.csv /user/$USER/exercises/input/exercise_13/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_13/top_profitable_date_mapper.py \
  -reducer exercise_13/top_profitable_date_reducer.py \
  -file exercise_13/top_profitable_date_mapper.py \
  -file exercise_13/top_profitable_date_reducer.py \
  -input "/user/$USER/exercises/input/exercise_13/*" \
  -output "/user/$USER/exercises/output/exercise_13"
```

Check the result:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_13/part-00000
```

## Files

- `top_profitable_date_mapper.py` - Parses input, emits `date\tincome`
- `top_profitable_date_reducer.py` - Finds the maximum income and outputs that date
