# Exercise 7: Inverted Index

## Overview

Build an inverted index that shows which sentences contain each word. Stop words ("and", "or", "not") are excluded.

**Input**: Text file with format `sentenceId\tsentence`  
**Output**: `(word, [sentenceId1, sentenceId2, ...])` - each word with the list of sentences containing it

## Example

**Input**:
```
Sentence#1	Hadoop or Spark
Sentence#2	Hadoop or Spark and Java
Sentence#3	Hadoop and Big Data
```

**Output**:
```
big	[Sentence#3]
data	[Sentence#3]
hadoop	[Sentence#1, Sentence#2, Sentence#3]
java	[Sentence#2]
spark	[Sentence#1, Sentence#2]
```

Notice that "and" and "or" are filtered out as stop words.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_7/inverted_index_input.txt /user/$USER/exercises/input/exercise_7/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_7/inverted_index_mapper.py \
  -reducer exercise_7/inverted_index_reducer.py \
  -file exercise_7/inverted_index_mapper.py \
  -file exercise_7/inverted_index_reducer.py \
  -input "/user/$USER/exercises/input/exercise_7/*" \
  -output "/user/$USER/exercises/output/exercise_7"
```

Check the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_7/part-00000
```

## Files

- `inverted_index_mapper.py` - Extracts words, filters stop words, emits `word\tsentenceId`
- `inverted_index_reducer.py` - Groups sentence IDs by word

**Stop words**: "and", "or", "not" are excluded from the index
