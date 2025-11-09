# Exercise 27: Categorization Rules

## Overview

Assign users to categories based on business rules. Each user record is matched against rules, and if a rule applies, the user is assigned to that category. If no rule matches, the category is "Unknown".

**Input**: 
- Large file with user records: `UserId,Name,Surname,Gender,YearOfBirth,City,Education`
- Business rules file: `Gender=<value> andYearOfBirth=<value> -> Category`

**Output**: User records with assigned category appended

## Example

**Input** (users):
```
User#1,John,Smith,M,1934,NewYork,Bachelor
User#2,Paul,Jones,M,1956,Dallas,College
User#3,Jenny,Smith,F,1934,Philadelphia,Bachelor
User#4,Laura,White,F,1926,NewYork,Doctorate
```

**Business rules**:
```
Gender=M andYearOfBirth=1934 -> Category#1
Gender=M andYearOfBirth=1956 -> Category#3
Gender=F andYearOfBirth=1934 -> Category#2
Gender=F andYearOfBirth=1956 -> Category#3
```

**Output**:
```
User#1,John,Smith,M,1934,NewYork,Bachelor,Category#1
User#2,Paul,Jones,M,1956,Dallas,College,Category#3
User#3,Jenny,Smith,F,1934,Philadelphia,Bachelor,Category#2
User#4,Laura,White,F,1926,NewYork,Doctorate,Unknown
```

User#4 doesn't match any rule, so gets "Unknown".

## Running on Hadoop

Upload both files to HDFS:

```bash
hdfs dfs -put exercise_27/users.txt exercise_27/business_rules.txt /user/$USER/exercises/input/exercise_27/
```

Run the job (map-only):

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper "exercise_27/categorization_mapper.py exercise_27/business_rules.txt" \
  -file exercise_27/categorization_mapper.py \
  -file exercise_27/business_rules.txt \
  -input "/user/$USER/exercises/input/exercise_27/users.txt" \
  -output "/user/$USER/exercises/output/exercise_27"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_27/part-00000
```

## Files

- `categorization_mapper.py` - Loads business rules and categorizes users
- `users.txt` - User records file
- `business_rules.txt` - Business rules file
