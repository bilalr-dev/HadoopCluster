# Exercise 29: User Selection

## Overview

Select users who like both "Commedia" and "Adventure" movies, and output only their Gender and YearOfBirth. This uses a MapReduce join to combine user records with their movie preferences.

**Input**: 
- Users file: `UserId,Name,Surname,Gender,YearOfBirth,City,Education`
- Likes file: `Userid,MovieGenre` (indicates user likes that genre)

**Output**: `Gender,YearOfBirth` for users who like both "Commedia" and "Adventure"

## Example

**Input** (users):
```
User#1,John,Smith,M,1934,NewYork,Bachelor
User#2,Paul,Jones,M,1956,Dallas,College
User#3,Jenny,Smith,F,1934,Philadelphia,Bachelor
```

**Input** (likes):
```
User#1,Commedia
User#1,Adventure
User#1,Drama
User#2,Commedia
User#2,Crime
User#3,Commedia
User#3,Horror
User#3,Adventure
```

**Output**:
```
M,1934
F,1934
```

User#1 likes both Commedia and Adventure → M,1934  
User#2 only likes Commedia → not selected  
User#3 likes both Commedia and Adventure → F,1934

## Running on Hadoop

Upload both files to HDFS:

```bash
hdfs dfs -put exercise_29/users.txt exercise_29/likes.txt /user/$USER/exercises/input/exercise_29/
```

Run the MapReduce jjob:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_29/user_selection_mapper.py \
  -reducer exercise_29/user_selection_reducer.py \
  -file exercise_29/user_selection_mapper.py \
  -file exercise_29/user_selection_reducer.py \
  -input "/user/$USER/exercises/input/exercise_29/*" \
  -output "/user/$USER/exercises/output/exercise_29"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_29/part-00000
```

## Files

- `user_selection_mapper.py` - Processes both users and likes, emits UserId as key
- `user_selection_reducer.py` - Joins users with likes, checks for both genres, outputs Gender,YearOfBirth
