# Exercise 2: Word Count (Multiple Files)

## Overview

Same as Exercise 1, but this time we're counting words across multiple files in a folder. The code is identical - Hadoop automatically handles multiple input files.

**Input**: Folder containing multiple text files  
**Output**: Word counts across all files, sorted alphabetically

## Example

**Input Files**:

File 1:
```
Test of the word count program
The word program is the Hadoop hello word program
```

File 2:
```
Second file
Hadoop Hadoop Hadoop
Spark
```

**Output** (combined counts from both files):
```
file	1
hadoop	4
program	2
second	1
spark	1
test	1
word	3
...
```

## Running on Hadoop

Upload your input files to HDFS:

```bash
# Upload multiple files
hdfs dfs -put exercise_2/*.txt /user/$USER/exercises/input/exercise_2/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_2/wordcount_mapper.py \
  -reducer exercise_2/wordcount_reducer.py \
  -file exercise_2/wordcount_mapper.py \
  -file exercise_2/wordcount_reducer.py \
  -input "/user/$USER/exercises/input/exercise_2/*" \
  -output "/user/$USER/exercises/output/exercise_2"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_2/part-00000
```

## Files

- `wordcount_mapper.py` - Same as Exercise 1
- `wordcount_reducer.py` - Same as Exercise 1
