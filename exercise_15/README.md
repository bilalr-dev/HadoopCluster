# Exercise 15: Dictionary – Mapping Word to Integer

## Overview

Create a dictionary that maps each distinct word to a unique integer. Words are sorted alphabetically and assigned integers starting from 1.

**Input**: Text file  
**Output**: `(word, integer)` pairs sorted alphabetically by word

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
example	1
file	2
for	3
hadoop	4
running	5
toy	6
```

Each word gets a unique integer. Words are sorted alphabetically first, then numbered sequentially.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_15/dictionary_integer_input.txt /user/$USER/exercises/input/exercise_15/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_15/dictionary_integer_mapper.py \
  -reducer exercise_15/dictionary_integer_reducer.py \
  -file exercise_15/dictionary_integer_mapper.py \
  -file exercise_15/dictionary_integer_reducer.py \
  -input "/user/$USER/exercises/input/exercise_15/*" \
  -output "/user/$USER/exercises/output/exercise_15"
```

Check the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_15/part-00000
```

## Files

- `dictionary_integer_mapper.py` - Extracts words, converts to lowercase, emits each word
- `dictionary_integer_reducer.py` - Collects distinct words, assigns integers starting from 1
