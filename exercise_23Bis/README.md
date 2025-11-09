# Exercise 23 Bis: Potential Friends of a Specific User (Alternative)

## Overview

Same as Exercise 23 - find potential friends of a specific user (people with at least one friend in common). This is an alternative implementation.

**Input**: File with format `Username1,Username2` (mutual friendship pairs)  
**Output**: Single line with space-separated list of potential friends

## Example

**Input**:
```
User1,User2
User1,User3
User1,User4
User2,User3
User2,User4
User2,User5
User5,User6
```

**Target user**: User2

**Output**:
```
User1 User3 User4 User6
```

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_23Bis/potential_friends_input.txt /user/$USER/exercises/input/exercise_23Bis/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_23Bis/potential_friends_mapper.py \
  -reducer exercise_23Bis/potential_friends_reducer.py \
  -file exercise_23Bis/potential_friends_mapper.py \
  -file exercise_23Bis/potential_friends_reducer.py \
  -cmdenv TARGET_USER=User2 \
  -input "/user/$USER/exercises/input/exercise_23Bis/*" \
  -output "/user/$USER/exercises/output/exercise_23Bis"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_23Bis/part-00000
```

**Important:** Make sure to change `TARGET_USER=User2` to the username you want.

## Files

- `potential_friends_mapper.py` - Alternative implementation for finding potential friends
- `potential_friends_reducer.py` - Collects and outputs potential friends
