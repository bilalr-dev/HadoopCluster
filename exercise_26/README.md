# Exercise 26: Word to Integer Conversion

## Overview

Converts words in a text file to integers using a dictionary mapping. Words found in the dictionary are replaced with their corresponding integer. Words not in the dictionary remain unchanged.

**Input**: 
- Large file with words (one line per line of text)
- Dictionary file with format `Word\tInteger` (one mapping per line)

**Output**: Text file with words replaced by integers where possible

## Example

**Input** (words file):
```
TEST CONVERTION WORD TO INTEGER
SECOND LINE TEST WORD TO INTEGER
```

**Dictionary**:
```
CONVERTION	1
INTEGER	2
LINE	3
SECOND	4
TEST	5
TO	6
WORD	7
```

**Output**:
```
5 1 7 6 2
4 3 5 7 6 2
```

Each word is looked up in the dictionary and replaced if found.

## Running on Hadoop

Upload both files to HDFS:

```bash
hdfs dfs -put exercise_26/words_input.txt exercise_26/dictionary.txt /user/$USER/exercises/input/exercise_26/
```

Run the job (map-only):

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper "exercise_26/word_to_integer_mapper.py exercise_26/dictionary.txt" \
  -file exercise_26/word_to_integer_mapper.py \
  -file exercise_26/dictionary.txt \
  -input "/user/$USER/exercises/input/exercise_26/words_input.txt" \
  -output "/user/$USER/exercises/output/exercise_26"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_26/part-00000
```

## Files

- `word_to_integer_mapper.py` - Loads dictionary and converts words to integers
- `words_input.txt` - Input file with words
- `dictionary.txt` - Dictionary with word-to-integer mappings (tab-separated)
