# Exercise 28: Mapping Question-Answer(s)

## Overview

Joins questions with their answers to create question-answer pairs. Questions and answers are matched by QuestionId.

**Input**: 
- Questions file: `QuestionId,Timestamp,TextOfTheQuestion`
- Answers file: `AnswerId,QuestionId,Timestamp,TextOfTheAnswer`

**Output**: Question-answer pairs in format `QuestionId,TextOfTheQuestion,AnswerId,TextOfTheAnswer`

## Example

**Input** (questions):
```
Q1,2015-01-01,What is ..?
Q2,2015-01-03,Who invented ..
```

**Input** (answers):
```
A1,Q1,2015-01-02,It is ..
A2,Q2,2015-01-03,John Smith
A3,Q1,2015-01-05,I think it is ..
```

**Output**:
```
Q1,What is ..?,A1,It is ..
Q1,What is ..?,A3,I think it is ..
Q2,Who invented ..,A2,John Smith
```

Q1 has 2 answers, so it produces 2 output lines. Q2 has 1 answer.

## Running on Hadoop

Upload both files to HDFS:

```bash
hdfs dfs -put exercise_28/questions.txt exercise_28/answers.txt /user/$USER/exercises/input/exercise_28/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_28/question_answer_mapper.py \
  -reducer exercise_28/question_answer_reducer.py \
  -file exercise_28/question_answer_mapper.py \
  -file exercise_28/question_answer_reducer.py \
  -input "/user/$USER/exercises/input/exercise_28/*" \
  -output "/user/$USER/exercises/output/exercise_28"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_28/part-00000
```

## Files

- `question_answer_mapper.py` - Processes both questions and answers, emits QuestionId as key
- `question_answer_reducer.py` - Joins questions with answers by QuestionId
