# Exercise 9: Word Count with In-Mapper Combiners

## Overview

Same as Exercise 1 (word count), but optimized using in-mapper combiners. Instead of emitting `word\t1` for every occurrence, the mapper counts words locally first, then emits `word\tcount`. This reduces network traffic.

**Input**: Text file  
**Output**: `(word, count)` pairs sorted alphabetically

## Example

**Input**:
```
Toy example
file for Hadoop.
Hadoop running
example.
```

**Output**:
```
example	2
file	1
for	1
hadoop	2
running	1
toy	1
```

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_9/wordcount_combiner_input.txt /user/$USER/exercises/input/exercise_9/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_9/wordcount_combiner_mapper.py \
  -reducer exercise_9/wordcount_combiner_reducer.py \
  -file exercise_9/wordcount_combiner_mapper.py \
  -file exercise_9/wordcount_combiner_reducer.py \
  -input "/user/$USER/exercises/input/exercise_9/*" \
  -output "/user/$USER/exercises/output/exercise_9"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_9/part-00000
```

## Files

- `wordcount_combiner_mapper.py` - Counts words locally in a dictionary, then emits `word\tcount`
- `wordcount_combiner_reducer.py` - Sums the pre-aggregated counts

**Why this is better**: The mapper does local aggregation before sending data over the network, reducing the amount of data shuffled between map and reduce tasks.
