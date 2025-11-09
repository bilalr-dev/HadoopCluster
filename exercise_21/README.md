# Exercise 21: Stopword Elimination

## Overview

Removes stopwords from sentences using a stopwords list. The mapper loads the stopwords file and filters them out from each sentence. This is a map-only job, so no reducer is needed.

**Input**: 
- Large file with sentences (one per line)
- Small stopwords file (one word per line)

**Output**: Sentences with stopwords removed

## Example

**Input** (sentences):
```
This is the first sentence and it contains some stopwords
Second sentence with a stopword here and another here
```

**Stopwords file**:
```
a
an
and
the
```

**Output**:
```
This is first sentence it contains some stopwords
Second sentence with stopword here another here
```

Words "a", "an", "and", and "the" are removed (case-insensitive).

## Running on Hadoop

Upload both files to HDFS:

```bash
hdfs dfs -put exercise_21/sentences_input.txt exercise_21/stopwords.txt /user/$USER/exercises/input/exercise_21/
```

Run the job (map-only):

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper "exercise_21/stopword_mapper.py exercise_21/stopwords.txt" \
  -file exercise_21/stopword_mapper.py \
  -file exercise_21/stopwords.txt \
  -input "/user/$USER/exercises/input/exercise_21/sentences_input.txt" \
  -output "/user/$USER/exercises/output/exercise_21"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_21/part-00000
```

## Files

- `stopword_mapper.py` - Loads stopwords and removes them from sentences
- `sentences_input.txt` - Input sentences (one per line)
- `stopwords.txt` - List of stopwords (one per line)
