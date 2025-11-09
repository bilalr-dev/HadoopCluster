# Hadoop MapReduce Exercises

A collection of 31 MapReduce exercises implemented in Python for learning Hadoop distributed computing. Each exercise demonstrates different MapReduce patterns and use cases, from basic word counting to complex data processing tasks.

## Overview

This repository contains MapReduce exercises covering:

- **Basic Operations**: Word count, filtering, aggregation, and statistics
- **Intermediate Operations**: Inverted indexes, combiners, joins, and multi-stage jobs
- **Advanced Operations**: Dictionary lookups, business rule categorization, and complex data transformations

## Prerequisites

- Hadoop 3.3.6 (or compatible version)
- Python 3
- HDFS configured and running

## Structure

Each exercise is organized in its own directory (`exercise_1/`, `exercise_2/`, etc.) containing:

- `*_mapper.py` - Map function implementation
- `*_reducer.py` - Reduce function implementation (when applicable)
- `*_input.txt` or `*_input.csv` - Sample input data
- `README.md` - Exercise-specific documentation with Hadoop execution instructions

## Quick Start

1. **Start Hadoop services**:
   ```bash
   start-dfs.sh
   start-yarn.sh
   ```

2. **Navigate to an exercise directory** (e.g., `exercise_1/`)

3. **Follow the exercise README** for specific instructions on:
   - Uploading input files to HDFS
   - Running the MapReduce job
   - Viewing results

## Example: Running Exercise 1 (Word Count)

```bash
# Upload input to HDFS
hdfs dfs -put exercise_1/wordcount_input.txt /user/$USER/exercises/input/exercise_1/

# Run MapReduce job
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_1/wordcount_mapper.py \
  -reducer exercise_1/wordcount_reducer.py \
  -file exercise_1/wordcount_mapper.py \
  -file exercise_1/wordcount_reducer.py \
  -input "/user/$USER/exercises/input/exercise_1/*" \
  -output "/user/$USER/exercises/output/exercise_1"

# View results
hdfs dfs -cat /user/$USER/exercises/output/exercise_1/part-00000
```

## Exercises

- **Exercise 1**: Word Count
- **Exercise 2**: Word Count (Multiple Files)
- **Exercise 3**: PM10 Pollution Count
- **Exercise 4**: PM10 Zone Dates
- **Exercise 5**: PM10 Average
- **Exercise 6**: PM10 Max/Min
- **Exercise 7**: Inverted Index
- **Exercise 8**: Income Analysis (Two-Stage)
- **Exercise 9**: Word Count with Combiners
- **Exercise 10**: Total Count
- **Exercise 11**: PM10 Average (CSV)
- **Exercise 12**: Select Outliers
- **Exercise 13**: Top Profitable Date
- **Exercise 13Bis**: Top Profitable Dates
- **Exercise 14**: Dictionary Lookup
- **Exercise 15**: Dictionary Integer Conversion
- **Exercise 17**: Max Temperature
- **Exercise 18**: Temperature Filter
- **Exercise 19**: Temperature Filter (Multiple Files)
- **Exercise 20**: Temperature Split
- **Exercise 20Bis**: Temperature Split (Single File)
- **Exercise 21**: Stopword Removal
- **Exercise 22**: Friends Count
- **Exercise 23**: Potential Friends
- **Exercise 23Bis**: Potential Friends (Alternative)
- **Exercise 24**: Friends List
- **Exercise 25**: Potential Friends (All)
- **Exercise 26**: Word to Integer Conversion
- **Exercise 27**: User Categorization
- **Exercise 28**: Question-Answer Join
- **Exercise 29**: User Selection

## Notes

- All Python scripts include shebang lines (`#!/usr/bin/env python3`) for Hadoop execution
- Some exercises require environment variables (e.g., `THRESHOLD`) passed via `-cmdenv`
- Some exercises use distributed cache (`-file`) for auxiliary files like dictionaries or business rules
- Map-only jobs (no reducer) are indicated in their respective README files

## License

This project is for educational purposes.

