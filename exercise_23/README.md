# Exercise 23: Potential Friends of a Specific User

## Overview

Find potential friends of a specific user - people who have at least one friend in common with the target user. This includes direct friends who also share common friends.

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

User2's direct friends: User1, User3, User4, User5  
- User1 shares User3, User4 with User2 → potential friend
- User3 shares User1 with User2 → potential friend
- User4 shares User1 with User2 → potential friend
- User6 shares User5 with User2 → potential friend

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_23/potential_friends_input.txt /user/$USER/exercises/input/exercise_23/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_23/potential_friends_mapper.py \
  -reducer exercise_23/potential_friends_reducer.py \
  -file exercise_23/potential_friends_mapper.py \
  -file exercise_23/potential_friends_reducer.py \
  -cmdenv TARGET_USER=User2 \
  -input "/user/$USER/exercises/input/exercise_23/*" \
  -output "/user/$USER/exercises/output/exercise_23"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_23/part-00000
```

**Important:** Make sure to change `TARGET_USER=User2` to the username you want to find potential friends for.

## Files

- `potential_friends_mapper.py` - Identifies users who share at least one friend with target (requires TARGET_USER)
- `potential_friends_reducer.py` - Collects potential friends and outputs as space-separated list
