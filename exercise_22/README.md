# Exercise 22: Friends of a Specific User

## Overview

Finds all friends of a specific user from a friendship pairs file. Each pair `A,B` represents mutual friendship (A is friend of B and vice versa).

**Input**: File with format `Username1,Username2` (one pair per line)  
**Output**: Single line with space-separated list of friends for the target user

## Example

**Input**:
```
User1,User2
User1,User3
User1,User4
User2,User5
```

**Target user**: User2

**Output**:
```
User1 User5
```

User2 appears in pairs with User1 and User5, so those are the friends.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_22/friends_input.txt /user/$USER/exercises/input/exercise_22/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_22/friends_mapper.py \
  -reducer exercise_22/friends_reducer.py \
  -file exercise_22/friends_mapper.py \
  -file exercise_22/friends_reducer.py \
  -cmdenv TARGET_USER=User2 \
  -input "/user/$USER/exercises/input/exercise_22/*" \
  -output "/user/$USER/exercises/output/exercise_22"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_22/part-00000
```

**Important:** Make sure to change `TARGET_USER=User2` to the username you want to find friends for.

## Files

- `friends_mapper.py` - Finds friends of the target user (requires TARGET_USER environment variable)
- `friends_reducer.py` - Collects all friends and outputs as space-separated list
