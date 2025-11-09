# Exercise 14: Dictionary

## Overview

Create a dictionary of all distinct words from a text file. Each word appears only once, converted to lowercase, and sorted alphabetically.

**Input**: Text file  
**Output**: List of distinct words, one per line, sorted alphabetically

## Example

**Input**:
```
The wind blew softly, softly over the hills, and the hills echoed the wind.
Trees swayed, swayed gently, their leaves whispering, whispering secrets of the day.
```

**Output** (first few lines):
```
again
air
all
and
appeared
birds
blew
breathe
...
wind
with
wrapping
```

All distinct words, lowercase, sorted. Total of 63 distinct words in the example.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_14/dictionary_input.txt /user/$USER/exercises/input/exercise_14/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_14/dictionary_mapper.py \
  -reducer exercise_14/dictionary_reducer.py \
  -file exercise_14/dictionary_mapper.py \
  -file exercise_14/dictionary_reducer.py \
  -input "/user/$USER/exercises/input/exercise_14/*" \
  -output "/user/$USER/exercises/output/exercise_14"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_14/part-00000
```

## Files

- `dictionary_mapper.py` - Extracts words, converts to lowercase, emits each word
- `dictionary_reducer.py` - Removes duplicates and outputs distinct words sorted alphabetically
