# Exercise 1: Word Count

## Overview

This counts how many times each word appears in a text file. The classic "Hello World" of MapReduce.

**Input**: Text file  
**Output**: Each word with its count, sorted alphabetically

## Example

**Input**:
```
Test of the word count program
The word program is the Hadoop hello word program
Example document for hadoop word count
```

**Output**:
```
count	2
document	1
example	1
for	1
hadoop	2
hello	1
is	1
of	1
program	3
test	1
the	3
word	4
```

## Running on Hadoop

First, upload your input file to HDFS:

```bash
# Upload input file to HDFS
hdfs dfs -put exercise_1/wordcount_input.txt /user/$USER/exercises/input/exercise_1/
```

Then run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_1/wordcount_mapper.py \
  -reducer exercise_1/wordcount_reducer.py \
  -file exercise_1/wordcount_mapper.py \
  -file exercise_1/wordcount_reducer.py \
  -input "/user/$USER/exercises/input/exercise_1/*" \
  -output "/user/$USER/exercises/output/exercise_1"
```

Check the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_1/part-00000
```

## Files

- `wordcount_mapper.py` - Reads each line, splits into words, converts to lowercase, and emits each word
- `wordcount_reducer.py` - Counts how many times each word appears and outputs the results
