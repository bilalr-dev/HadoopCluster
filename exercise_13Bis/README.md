# Exercise 13 Bis: Top 2 Most Profitable Dates

## Overview

Find the top 2 dates with the highest daily income. If there's a tie, the first 2 dates among those with the highest income are selected.

**Input**: CSV file with format `date\tdaily_income`  
**Output**: `date\tincome` - the top 2 most profitable dates

## Example

**Input**:
```
2015-11-01	1000
2015-11-02	1305
2015-12-01	500
2015-12-02	1305
2016-01-01	345
2016-01-02	1145
```

**Output**:
```
2015-11-02	1305
2015-12-02	1305
```

Both dates have income 1305, which is the highest. The reducer selects the first 2 dates with this value.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_13Bis/top_profitable_dates_input.csv /user/$USER/exercises/input/exercise_13Bis/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_13Bis/top_profitable_dates_mapper.py \
  -reducer exercise_13Bis/top_profitable_dates_reducer.py \
  -file exercise_13Bis/top_profitable_dates_mapper.py \
  -file exercise_13Bis/top_profitable_dates_reducer.py \
  -input "/user/$USER/exercises/input/exercise_13Bis/*" \
  -output "/user/$USER/exercises/output/exercise_13Bis"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_13Bis/part-00000
```

## Files

- `top_profitable_dates_mapper.py` - Parses input, emits `date\tincome`
- `top_profitable_dates_reducer.py` - Sorts by income (descending), selects top 2 dates

**Tie-breaking**: If multiple dates have the same income, they're sorted by income (descending) then by date (ascending), and the first 2 are selected.
