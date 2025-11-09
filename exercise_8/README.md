# Exercise 8: Total Income and Average Monthly Income

## Overview

This exercise requires two MapReduce jobs:

1. **First job**: Calculate total income for each month
2. **Second job**: Calculate average monthly income per year (using the output from job 1)

**Input**: CSV file with format `date\tdaily_income`  
**Output**: 
- Job 1: `(year-month, total)` - monthly totals
- Job 2: `(year, average)` - yearly averages

## Example

**Input**:
```
2015-11-01	1000
2015-11-02	1305
2015-12-01	500
2015-12-02	750
2016-01-01	345
2016-01-02	1145
2016-02-03	200
2016-02-04	500
```

**Monthly Totals** (Job 1 output):
```
2015-11	2305
2015-12	1250
2016-01	1490
2016-02	700
```

**Yearly Averages** (Job 2 output):
```
2015	1777.5
2016	1095.0
```

2015 average: (2305 + 1250) / 2 = 1777.5  
2016 average: (1490 + 700) / 2 = 1095.0

## Running on Hadoop

### Job 1: Monthly Totals

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_8/income_input.csv /user/$USER/exercises/input/exercise_8/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_8/monthly_total_mapper.py \
  -reducer exercise_8/monthly_total_reducer.py \
  -file exercise_8/monthly_total_mapper.py \
  -file exercise_8/monthly_total_reducer.py \
  -input "/user/$USER/exercises/input/exercise_8/*" \
  -output "/user/$USER/exercises/output/exercise_8/monthly_totals"
```

### Job 2: Yearly Averages

Use the output from Job 1 as input:

```bash
hadoop jar "$STREAMING_JAR" \
  -mapper exercise_8/yearly_average_mapper.py \
  -reducer exercise_8/yearly_average_reducer.py \
  -file exercise_8/yearly_average_mapper.py \
  -file exercise_8/yearly_average_reducer.py \
  -input "/user/$USER/exercises/output/exercise_8/monthly_totals/*" \
  -output "/user/$USER/exercises/output/exercise_8/yearly_averages"
```

View the results:

```bash
# Monthly totals
hdfs dfs -cat /user/$USER/exercises/output/exercise_8/monthly_totals/part-00000

# Yearly averages
hdfs dfs -cat /user/$USER/exercises/output/exercise_8/yearly_averages/part-00000
```

## Files

- `monthly_total_mapper.py` - Extracts year-month from date, emits `year-month\tincome`
- `monthly_total_reducer.py` - Sums income per month
- `yearly_average_mapper.py` - Reads monthly totals, extracts year
- `yearly_average_reducer.py` - Calculates average monthly income per year
