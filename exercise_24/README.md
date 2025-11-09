# Exercise 24: Compute Friends List for Each User

## Overview

Compute the complete list of friends for every user from friendship pairs. Each pair `A,B` represents mutual friendship.

**Input**: File with format `Username1,Username2` (one pair per line)  
**Output**: One line per user showing their friends list in format `Username: friend1 friend2 ...`

## Example

**Input**:
```
User1,User2
User1,User3
User1,User4
User2,User5
```

**Output**:
```
User1: User2 User3 User4
User2: User1 User5
User3: User1
User4: User1
User5: User2
```

Each user gets a line with all their friends listed.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_24/friends_list_input.txt /user/$USER/exercises/input/exercise_24/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_24/friends_list_mapper.py \
  -reducer exercise_24/friends_list_reducer.py \
  -file exercise_24/friends_list_mapper.py \
  -file exercise_24/friends_list_reducer.py \
  -input "/user/$USER/exercises/input/exercise_24/*" \
  -output "/user/$USER/exercises/output/exercise_24"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_24/part-00000
```

## Files

- `friends_list_mapper.py` - Emits bidirectional friendships (for pair A,B, emits both A->B and B->A)
- `friends_list_reducer.py` - Groups friends by user and outputs in format `User: friend1 friend2 ...`
