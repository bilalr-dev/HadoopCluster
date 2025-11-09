# Exercise 4: PM10 Pollution Analysis Per City Zone

## Overview

For each city zone, list all the dates when PM10 pollution was above 50 μg/m³. Only zones with at least one day above the threshold are included.

**Input**: File with format `zoneId,date\tPM10_value`  
**Output**: `(zoneId, [date1, date2, ...])` - list of dates for each zone

## Example

**Input**:
```
zone1,2016-01-01	20.5
zone2,2016-01-01	30.1
zone1,2016-01-02	60.2
zone2,2016-01-02	20.4
zone1,2016-01-03	55.5
zone2,2016-01-03	52.5
```

**Output**:
```
zone1	[2016-01-02, 2016-01-03]
zone2	[2016-01-03]
```

Zone1 had high pollution on 2 dates, zone2 on 1 date.

## Running on Hadoop

Upload the input file to HDFS:

```bash
hdfs dfs -put exercise_4/pm10_zone_input.txt /user/$USER/exercises/input/exercise_4/
```

Run the MapReduce job:

```bash
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

hadoop jar "$STREAMING_JAR" \
  -mapper exercise_4/pm10_zone_mapper.py \
  -reducer exercise_4/pm10_zone_reducer.py \
  -file exercise_4/pm10_zone_mapper.py \
  -file exercise_4/pm10_zone_reducer.py \
  -input "/user/$USER/exercises/input/exercise_4/*" \
  -output "/user/$USER/exercises/output/exercise_4"
```

View the results:

```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_4/part-00000
```

## Files

- `pm10_zone_mapper.py` - Filters PM10 > 50, emits `zoneId\tdate`
- `pm10_zone_reducer.py` - Collects all dates per zone into a list

The threshold is 50 μg/m³ (hardcoded in mapper)
