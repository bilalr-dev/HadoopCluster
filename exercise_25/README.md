# Exercise 25: Compute Potential Friends List for Each User

## Overview

Compute potential friends for every user - people who have at least one friend in common with them. This processes all users, not just one specific user.

**Input**: File with format `Username1,Username2` (mutual friendship pairs)  
**Output**: One line per user showing their potential friends in format `Username: potential_friend1 potential_friend2 ...`

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

**Output**:
```
User1: User2 User3 User4 User5
User2: User1 User3 User4 User6
User3: User1 User2 User4 User5
User4: User1 User2 User3 User5
User5: User1 User3 User4
User6: User2
```

Each user gets a line with all their potential friends (people who share at least one common friend).

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_25/potential_friends_all_input.txt /user/$USER/exercises/input/exercise_25/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_25/potential_friends_all_mapper.py \
  -reducer exercise_25/potential_friends_all_reducer.py \
  -file exercise_25/potential_friends_all_mapper.py \
  -file exercise_25/potential_friends_all_reducer.py \
  -input "/user/$USER/exercises/input/exercise_25/*" \
  -output "/user/$USER/exercises/output/exercise_25"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_25/part-00000
```

## Files

- `potential_friends_all_mapper.py` - Finds potential friends for all users
- `potential_friends_all_reducer.py` - Groups potential friends by user and outputs results
