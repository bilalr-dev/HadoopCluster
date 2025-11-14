# Hadoop MapReduce Project - Technical Implementation Report

## Table of Contents
1. [Project Overview](#project-overview)
2. [Python Implementation](#python-implementation)
3. [Running Locally](#running-locally)
4. [Hadoop Installation and Setup](#hadoop-installation-and-setup)
5. [Deploying to Hadoop Cluster](#deploying-to-hadoop-cluster)
6. [Verifying Outputs](#verifying-outputs)
7. [Conclusion](#conclusion)

---

## Project Overview

The repository implements **31 MapReduce exercises** in Python. This report focuses on the **first 10 mandatory exercises**, which already cover a broad range of distributed processing patterns—from basic word counting to multi-stage aggregations.

**Scope of This Report:**
- Focuses on the **first 10 mandatory exercises** in the series
- Remaining exercises (11–29) exist in the repository but are optional and not covered here

**Key Statistics (for the first 10 exercises):**
- **Total Exercises Covered**: 10
- **Python Scripts**: 20 (mappers and reducers)
- **Programming Language**: Python 3
- **Hadoop Version**: 3.3.6
- **Execution Method**: Hadoop Streaming

---

## Python Implementation

### Requirements

**System Requirements:**
- **Python 3.x** (no external libraries required - uses only standard library)
- **Operating System**: macOS, Linux, or Windows (with WSL)
- **Java 11** (required for Hadoop 3.3.6)

**Python Standard Library Modules Used:**
- `sys` - For reading from stdin and writing to stdout
- `re` - For regular expressions (word tokenization)
- `os` - For environment variables and file access
- `collections` - For data structures (when needed)

**No External Dependencies:**
All exercises use only Python's standard library, making them lightweight and easy to deploy. No `pip install` or `requirements.txt` needed.

### File Structure

The project follows a consistent directory structure:

```
BigDataLab/
├── README.md                          # Main project documentation
├── PROJECT_REPORT.md                  # This report
├── .gitignore                         # Git ignore rules
├── exercise_1/                        # Exercise directories (1–10 mandatory)
│   ├── README.md                      # Exercise-specific instructions
│   ├── wordcount_mapper.py            # Mapper script
│   ├── wordcount_reducer.py           # Reducer script
│   └── wordcount_input.txt            # Sample input data
├── exercise_2/
│   ├── README.md
│   ├── wordcount_mapper.py
│   ├── wordcount_reducer.py
│   └── [input files]
├── exercise_3/
│   └── ...
└── [exercise_4 through exercise_10]
```

**Directory Naming Convention:**
- `exercise_N/` - Sequential numbering (1-10 for the mandatory set)

**File Naming Convention:**
- `*_mapper.py` - Mapper scripts
- `*_reducer.py` - Reducer scripts (when applicable)
- `*_input.txt` or `*_input.csv` - Input data files
- `README.md` - Exercise documentation

### Code Structure and Patterns

#### 1. Standard Mapper Pattern

All mappers follow this structure:

```python
#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Process line and emit key-value pairs
        # Format: print(f"{key}\t{value}")
        
if __name__ == "__main__":
    main()
```

**Key Characteristics:**
- **Shebang line**: `#!/usr/bin/env python3` - Required for Hadoop execution
- **Reads from stdin**: `sys.stdin` - Hadoop streams input data
- **Writes to stdout**: `print()` - Hadoop captures output
- **Tab-separated output**: Key and value separated by `\t`

**Example - Word Count Mapper:**
```python
#!/usr/bin/env python3
import sys
import re

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            print(f"{word}\t1")

if __name__ == "__main__":
    main()
```

#### 2. Standard Reducer Pattern

All reducers follow this structure:

```python
#!/usr/bin/env python3
import sys

def main():
    current_key = None
    current_values = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        key, value = line.split('\t', 1)
        
        if current_key == key:
            current_values.append(value)
        else:
            if current_key is not None:
                # Process accumulated values
                result = process_values(current_values)
                print(f"{current_key}\t{result}")
            
            current_key = key
            current_values = [value]
    
    # Process last key
    if current_key is not None:
        result = process_values(current_values)
        print(f"{current_key}\t{result}")

if __name__ == "__main__":
    main()
```

**Key Characteristics:**
- **Reads sorted input**: Hadoop automatically sorts mapper output by key
- **Groups by key**: Accumulates all values for the same key
- **Emits aggregated results**: Processes grouped values and outputs final result

**Example - Word Count Reducer:**
```python
#!/usr/bin/env python3
import sys

def main():
    current_word = None
    count = 0
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        word, value = line.split('\t', 1)
        
        if current_word == word:
            count += int(value)
        else:
            if current_word is not None:
                print(f"{current_word}\t{count}")
            current_word = word
            count = int(value)
    
    if current_word is not None:
        print(f"{current_word}\t{count}")

if __name__ == "__main__":
    main()
```

#### 3. Special Patterns Found in Exercises 1–10

- **Multi-file ingestion (Exercise 2):** Demonstrates running the mapper against multiple input documents to build a single aggregate word count.
- **Temporal bucketing (Exercises 3–5):** Shows how to parse CSV/TSV timestamps and bucket readings by day, month, or sensor zone before aggregation.
- **Two-stage processing (Exercise 8):** Chains two MapReduce jobs—first to compute monthly totals, then to compute yearly averages based on the first job’s output.
- **Combiners (Exercise 9):** Introduces mapper-side aggregation to shrink shuffle volume when counting frequent tokens.
- **Full-scan totals (Exercise 10):** Reinforces reducer-side summations by scanning every column and emitting global totals.

### Python Perspective on Exercises 1–10 (High-Level)
- **Exercise 1 – Word Count:** Highlights basic text processing with `re.findall`, lowercase normalization, and integer accumulation in the reducer.
- **Exercise 2 – Multi-File Word Count:** Reuses the same mapper/reducer as Exercise 1, proving that Hadoop’s streaming stdin lets Python code remain unchanged even when inputs span multiple files.
- **Exercise 3 – PM10 Counts by Zone:** The mapper splits tab-delimited rows and emits `(zone, 1)`; the reducer totals with simple counters, reinforcing control flow around malformed lines.
- **Exercise 4 – PM10 Zone Dates:** Emits `(zone, date)` pairs and uses Python sets to deduplicate dates before printing, demonstrating lightweight in-memory structures.
- **Exercise 5 – PM10 Average:** Mapper emits numeric readings; reducer keeps running sums and counts in dictionaries, then prints formatted averages using Python’s float math.
- **Exercise 6 – PM10 Max/Min:** Shows how tuple comparisons capture both current max and min per zone without third-party libraries.
- **Exercise 7 – Inverted Index:** Mapper records `(word, line:position)` strings; reducer sorts tuples before output, exercising list sorting and custom parsing helpers.
- **Exercise 8 – Two-Stage Income Analysis:** First reducer writes monthly totals; second mapper/reducer pair reads that intermediate file to compute yearly averages, showcasing modular Python scripts.
- **Exercise 9 – Word Count with Combiner:** Adds an in-mapper dictionary (`defaultdict(int)`) to aggregate before emitting, illustrating how Python data structures reduce shuffle traffic.
- **Exercise 10 – Total Count:** Mapper iterates through CSV columns, emitting labeled metrics; reducer tallies each metric independently via dictionary keys.

### Exercise Categories Covered in This Report

- **Exercises 1–6 (Foundational analytics):** Word counting, PM10 pollution summaries, rolling averages, min/max detection, and data filtering.
- **Exercises 7–9 (Intermediate patterns):** Inverted index construction, two-stage revenue aggregation, and introducing combiners to reduce shuffle volume.
- **Exercise 10 (Operational totals):** Full data scan that tallies counts across multiple columns, reinforcing reducer-side aggregations.

---

## Running Locally

### Prerequisites for Local Testing

1. **Python 3** installed and accessible
2. **Input data files** in the exercise directories

### Local Testing Method

While the exercises are designed for Hadoop, you can test them locally using Unix pipes:

#### Example: Exercise 1 (Word Count)

```bash
# Navigate to exercise directory
cd exercise_1

# Test mapper
cat wordcount_input.txt | python3 wordcount_mapper.py

# Test full pipeline (mapper + sort + reducer)
cat wordcount_input.txt | python3 wordcount_mapper.py | sort | python3 wordcount_reducer.py
```

**Explanation:**
- `cat` - Reads input file
- `|` - Pipes output to next command
- `python3 wordcount_mapper.py` - Runs mapper
- `sort` - Sorts mapper output (Hadoop does this automatically)
- `python3 wordcount_reducer.py` - Runs reducer

#### Example: Exercise 8 (Two-Stage Income Analysis)

```bash
# Job 1: Monthly totals
cd exercise_8
cat income_input.csv | python3 monthly_total_mapper.py | sort | python3 monthly_total_reducer.py > monthly_totals.txt

# Job 2: Yearly averages (use output from job 1)
cat monthly_totals.txt | python3 yearly_average_mapper.py | sort | python3 yearly_average_reducer.py
```

**Note:** Local testing is useful for debugging, but the exercises are designed to run on Hadoop for distributed processing benefits, especially when chaining multiple stages like Exercise 8.

### Local Testing Limitations

1. **No distributed processing** - Runs on single machine
2. **Manual sorting required** - Must use `sort` command between mapper and reducer
3. **No HDFS integration** - Files must be in local filesystem
4. **Limited scalability** - Cannot process large datasets efficiently

---

## Hadoop Installation and Setup

### System Requirements

- **Operating System**: macOS 26.0.1, Linux, or Windows (with WSL)
- **Java**: Java 11 (Hadoop 3.3.6 requires Java 8 or 11, not Java 21+)
- **SSH**: For Hadoop daemon communication
- **Disk Space**: ~500MB for Hadoop installation + data storage

### Step-by-Step Installation

#### Step 1: Install Java 11

**macOS (using Homebrew):**
```bash
# Check current Java version
java -version

# Install Java 11
brew install openjdk@11

# Set JAVA_HOME
export JAVA_HOME=$(/usr/libexec/java_home -v 11)
export PATH=$JAVA_HOME/bin:$PATH

# Verify installation
java -version
# Should show: openjdk version "11.x.x"
```

**Linux (Ubuntu/Debian):**
```bash
# Update package list
sudo apt-get update

# Install OpenJDK 11
sudo apt-get install openjdk-11-jdk

# Set JAVA_HOME (add to ~/.bashrc or ~/.zshrc)
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

# Reload shell configuration
source ~/.bashrc  # or source ~/.zshrc

# Verify installation
java -version
```

#### Step 2: Download and Install Hadoop

```bash
# Navigate to home directory
cd ~

# Download Hadoop 3.3.6
wget https://archive.apache.org/dist/hadoop/core/hadoop-3.3.6/hadoop-3.3.6.tar.gz

# Extract Hadoop
tar -xzf hadoop-3.3.6.tar.gz

# Move to installation directory (requires sudo)
sudo mv hadoop-3.3.6 /usr/local/hadoop

# Set ownership to current user
sudo chown -R $USER /usr/local/hadoop

# Verify installation
ls -la /usr/local/hadoop
```

#### Step 3: Configure Environment Variables

Add the following to `~/.bashrc` (Linux) or `~/.zshrc` (macOS):

```bash
# Hadoop environment variables
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

Reload your shell configuration:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

Verify Hadoop is accessible:
```bash
hadoop version
# Should show: Hadoop 3.3.6
```

#### Step 4: Configure SSH for Localhost

Hadoop uses SSH to start and stop daemons. Set up passwordless SSH:

```bash
# Generate SSH key (if not exists)
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa

# Add public key to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Set proper permissions
chmod 0600 ~/.ssh/authorized_keys

# Test SSH connection
ssh localhost "echo 'SSH works!'"
# Should output: SSH works!
```

**macOS Note:** Enable Remote Login in System Preferences > Sharing > Remote Login.

#### Step 5: Configure Hadoop XML Files

**Edit `$HADOOP_HOME/etc/hadoop/core-site.xml`:**

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

This sets the default filesystem to HDFS running on localhost port 9000.

**Edit `$HADOOP_HOME/etc/hadoop/hdfs-site.xml`:**

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///usr/local/hadoop/hadoop_data/hdfs/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///usr/local/hadoop/hadoop_data/hdfs/datanode</value>
    </property>
    <property>
        <name>dfs.webhdfs.enabled</name>
        <value>true</value>
    </property>
</configuration>
```

**Configuration Explanation:**
- `dfs.replication`: Number of data replicas (1 for single-node setup)
- `dfs.namenode.name.dir`: Directory for NameNode metadata
- `dfs.datanode.data.dir`: Directory for DataNode data blocks
- `dfs.webhdfs.enabled`: Enable WebHDFS for web UI access

**Create `$HADOOP_HOME/etc/hadoop/mapred-site.xml`:**

```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>yarn.app.mapreduce.am.env</name>
        <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
    </property>
    <property>
        <name>mapreduce.map.env</name>
        <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
    </property>
    <property>
        <name>mapreduce.reduce.env</name>
        <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
    </property>
</configuration>
```

**Edit `$HADOOP_HOME/etc/hadoop/yarn-site.xml`:**

```xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```

#### Step 6: Create Data Directories

```bash
# Create directories for NameNode and DataNode
mkdir -p /usr/local/hadoop/hadoop_data/hdfs/namenode
mkdir -p /usr/local/hadoop/hadoop_data/hdfs/datanode

# Set ownership
sudo chown -R $USER /usr/local/hadoop/hadoop_data
sudo chmod -R 755 /usr/local/hadoop/hadoop_data
```

#### Step 7: Format NameNode

**Important:** Only format the NameNode on the first setup. Formatting erases all HDFS data!

```bash
hdfs namenode -format
```

Expected output should show:
```
Storage directory /usr/local/hadoop/hadoop_data/hdfs/namenode has been successfully formatted.
```

#### Step 8: Start Hadoop Services

```bash
# Start HDFS (NameNode, DataNode, SecondaryNameNode)
start-dfs.sh

# Start YARN (ResourceManager, NodeManager)
start-yarn.sh

# Verify services are running
jps
```

**Expected `jps` output:**
```
12345 NameNode
12346 DataNode
12347 SecondaryNameNode
12348 ResourceManager
12349 NodeManager
```

#### Step 9: Verify Installation

```bash
# Check HDFS root directory
hdfs dfs -ls /

# Should show empty directory or default directories
```

**Access Web UIs:**
- **NameNode UI**: http://localhost:9870
- **ResourceManager UI**: http://localhost:8088

### Troubleshooting Common Issues

1. **Permission Errors:**
   ```bash
   sudo chown -R $USER /usr/local/hadoop
   ```

2. **SSH Connection Refused:**
   - macOS: Enable Remote Login in System Preferences > Sharing
   - Linux: Install and start SSH service: `sudo systemctl start ssh`

3. **Java Version Issues:**
   - Ensure Java 11 is installed and `JAVA_HOME` is set correctly
   - Check: `echo $JAVA_HOME` and `java -version`

4. **Port Conflicts:**
   - Check if ports 9000, 9870, 8088 are in use:
     ```bash
     lsof -i :9000
     lsof -i :9870
     lsof -i :8088
     ```

5. **YARN Not Starting:**
   - Verify `mapred-site.xml` has correct `HADOOP_MAPRED_HOME` settings
   - Check logs: `cat $HADOOP_HOME/logs/yarn-*-resourcemanager-*.log`

---

## Deploying to Hadoop Cluster

### Preparing Input Files

Before running MapReduce jobs, input files must be uploaded to HDFS.

#### Step 1: Create HDFS Directories

```bash
# Create base directories for exercises
hdfs dfs -mkdir -p /user/$USER/exercises/input
hdfs dfs -mkdir -p /user/$USER/exercises/output

# Verify directories created
hdfs dfs -ls /user/$USER/exercises/
```

#### Step 2: Upload Input Files

**Single File Upload:**
```bash
# Example: Exercise 1
hdfs dfs -put exercise_1/wordcount_input.txt /user/$USER/exercises/input/exercise_1/
```

**Multiple Files Upload:**
```bash
# Example: Exercise 2 (multiple input files)
hdfs dfs -put exercise_2/document.txt exercise_2/document2.txt /user/$USER/exercises/input/exercise_2/
```

**Verify Upload:**
```bash
# List files in HDFS directory
hdfs dfs -ls /user/$USER/exercises/input/exercise_1/

# View file contents (for small files)
hdfs dfs -cat /user/$USER/exercises/input/exercise_1/wordcount_input.txt
```

### Running MapReduce Jobs

#### Basic Job Execution

**Standard MapReduce Job (with mapper and reducer):**

```bash
# Set Hadoop Streaming JAR path
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

# Run the job
hadoop jar "$STREAMING_JAR" \
  -mapper exercise_1/wordcount_mapper.py \
  -reducer exercise_1/wordcount_reducer.py \
  -file exercise_1/wordcount_mapper.py \
  -file exercise_1/wordcount_reducer.py \
  -input "/user/$USER/exercises/input/exercise_1/*" \
  -output "/user/$USER/exercises/output/exercise_1"
```

**Command Breakdown:**
- `hadoop jar "$STREAMING_JAR"` - Uses Hadoop Streaming to run Python scripts
- `-mapper` - Specifies mapper script
- `-reducer` - Specifies reducer script
- `-file` - Distributes Python scripts to cluster nodes
- `-input` - HDFS input path (supports wildcards like `*`)
- `-output` - HDFS output directory (must not exist)

#### Two-Stage Jobs

Chain multiple MapReduce jobs:

**Job 1:**
```bash
hadoop jar "$STREAMING_JAR" \
  -mapper exercise_8/monthly_total_mapper.py \
  -reducer exercise_8/monthly_total_reducer.py \
  -file exercise_8/monthly_total_mapper.py \
  -file exercise_8/monthly_total_reducer.py \
  -input "/user/$USER/exercises/input/exercise_8/*" \
  -output "/user/$USER/exercises/output/exercise_8/monthly_totals"
```

**Job 2 (uses Job 1 output as input):**
```bash
hadoop jar "$STREAMING_JAR" \
  -mapper exercise_8/yearly_average_mapper.py \
  -reducer exercise_8/yearly_average_reducer.py \
  -file exercise_8/yearly_average_mapper.py \
  -file exercise_8/yearly_average_reducer.py \
  -input "/user/$USER/exercises/output/exercise_8/monthly_totals/*" \
  -output "/user/$USER/exercises/output/exercise_8/yearly_averages"
```

### Job Execution Output

When a job runs, you'll see output like:

```
2025-11-08 01:23:05,139 INFO mapreduce.Job: Running job: job_1234567890123_0001
2025-11-08 01:23:05,234 INFO mapreduce.Job: map 0% reduce 0%
2025-11-08 01:23:10,345 INFO mapreduce.Job: map 50% reduce 0%
2025-11-08 01:23:15,456 INFO mapreduce.Job: map 100% reduce 0%
2025-11-08 01:23:20,567 INFO mapreduce.Job: map 100% reduce 50%
2025-11-08 01:23:25,678 INFO mapreduce.Job: map 100% reduce 100%
2025-11-08 01:23:30,789 INFO mapreduce.Job: Job job_1234567890123_0001 completed successfully
```

**Key Information:**
- Job ID: `job_1234567890123_0001`
- Progress: Map and reduce percentages
- Completion status: "completed successfully" or error message

---

## Verifying Outputs

### From Hadoop Terminal

#### Step 1: Check Output Directory

```bash
# List output directory contents
hdfs dfs -ls /user/$USER/exercises/output/exercise_1/

# Expected output:
# -rw-r--r--   1 user supergroup    1234 2025-11-08 01:23 /user/user/exercises/output/exercise_1/part-00000
# -rw-r--r--   1 user supergroup       0 2025-11-08 01:23 /user/user/exercises/output/exercise_1/_SUCCESS
```

**File Explanation:**
- `part-00000` - Contains the actual output data (one file per reducer)
- `_SUCCESS` - Empty marker file indicating job completed successfully

#### Step 2: View Output Contents

**View entire output file:**
```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_1/part-00000
```

**View first N lines:**
```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_1/part-00000 | head -20
```

**View last N lines:**
```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_1/part-00000 | tail -20
```

**Count output lines:**
```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_1/part-00000 | wc -l
```

**Search in output:**
```bash
hdfs dfs -cat /user/$USER/exercises/output/exercise_1/part-00000 | grep "specific_word"
```

#### Step 3: Download Output for Local Analysis

```bash
# Download output to local filesystem
hdfs dfs -get /user/$USER/exercises/output/exercise_1/part-00000 exercise_1_output.txt

# View locally
cat exercise_1_output.txt
```

#### Step 4: Check Job History

```bash
# List all jobs
mapred job -list

# View job details
mapred job -status <job_id>
```

### From Hadoop Web GUI

#### Accessing the Web Interfaces

1. **NameNode Web UI**: http://localhost:9870
   - Provides HDFS file system browser
   - Shows cluster status and storage information

2. **ResourceManager Web UI**: http://localhost:8088
   - Shows running and completed MapReduce jobs
   - Displays job history and resource usage

#### Using NameNode Web UI (http://localhost:9870)

**Step 1: Navigate to File Browser**

1. Open browser and go to http://localhost:9870
2. Click on **"Utilities"** menu
3. Select **"Browse the file system"**

**Step 2: Navigate to Output Directory**

1. In the file browser, navigate to: `/user/<your_username>/exercises/output/`
2. Click on the exercise directory (e.g., `exercise_1`)
3. You'll see output files:
   - `part-00000` - Output data
   - `_SUCCESS` - Success marker

**Step 3: View File Contents**

1. Click on `part-00000`
2. Click **"Download"** to download the file
3. Or click **"Head"** to view first 1KB of the file
4. Or click **"Tail"** to view last 1KB of the file

**Step 4: Check File Properties**

1. Click on any file
2. View file properties:
   - **File Size**: Size in bytes
   - **Replication**: Number of replicas (should be 1 for single-node)
   - **Block Size**: HDFS block size (default 128MB)
   - **Permissions**: File permissions
   - **Owner**: File owner
   - **Modification Time**: Last modified timestamp

**Step 5: Using Explorer (Alternative Method)**

1. Go to http://localhost:9870/explorer.html
2. Navigate through the directory tree
3. Click on files to view or download

**Note:** If WebHDFS is not enabled, you may see errors. Ensure `dfs.webhdfs.enabled` is set to `true` in `hdfs-site.xml`.

#### Using ResourceManager Web UI (http://localhost:8088)

**Step 1: View Running Jobs**

1. Open browser and go to http://localhost:8088
2. The main page shows:
   - **Running Applications**: Currently executing jobs
   - **Completed Applications**: Finished jobs

**Step 2: View Job Details**

1. Click on a job from the list
2. View job information:
   - **Job ID**: Unique job identifier
   - **User**: User who submitted the job
   - **Name**: Job name
   - **State**: Job state (RUNNING, SUCCEEDED, FAILED)
   - **Final Status**: Final job status
   - **Started**: Start time
   - **Finished**: Completion time
   - **Elapsed Time**: Total execution time

**Step 3: View Job Counters**

1. In job details page, click **"Counters"**
2. View various metrics:
   - **Map Input Records**: Number of input records processed by mappers
   - **Map Output Records**: Number of key-value pairs emitted by mappers
   - **Reduce Input Records**: Number of records processed by reducers
   - **Reduce Output Records**: Number of output records
   - **Bytes Written**: Total bytes written to HDFS

**Step 4: View Map and Reduce Tasks**

1. In job details page, click **"Map"** or **"Reduce"** tabs
2. View individual task information:
   - Task ID
   - State (SUCCEEDED, FAILED, KILLED)
   - Progress
   - Start/Finish times
   - Node where task ran

**Step 5: View Job Logs**

1. Click on a specific task
2. View task logs:
   - **stdout**: Standard output from mapper/reducer
   - **stderr**: Error messages
   - **syslog**: System logs

**Step 6: View Job History**

1. Click **"Application History"** in the left menu
2. Browse all completed jobs
3. Filter by user, state, or time range

### Verification Checklist

After running a job, verify:

- [ ] Job completed successfully (check terminal output or ResourceManager UI)
- [ ] Output directory exists in HDFS
- [ ] `_SUCCESS` file exists in output directory
- [ ] `part-00000` file exists and has content (non-zero size)
- [ ] Output data matches expected format
- [ ] Output values are correct (spot-check a few entries)
- [ ] No errors in job logs (check ResourceManager UI)

### Common Issues and Solutions

**Empty Output Files:**
- Check if mapper/reducer writes to `sys.stdout` (not local files)
- Verify input files were uploaded correctly
- Check job logs for errors

**Job Failed:**
- Check ResourceManager UI for error messages
- Review task logs (stderr)
- Verify Python scripts have shebang lines
- Ensure all required files are distributed via `-file`

**Cannot Access Web UI:**
- Verify Hadoop services are running: `jps`
- Check if ports 9870 and 8088 are accessible
- For WebHDFS errors, ensure `dfs.webhdfs.enabled=true` in `hdfs-site.xml`

---

## Local vs Hadoop: Lessons Learned

### Pain Points with the Classic Local Method
- **Manual plumbing:** Running `cat file | mapper | sort | reducer` for every exercise becomes repetitive. Forgetting the `sort` step or mistyping a pipe breaks the flow, especially for two-stage pipelines like Exercise 8.
- **Single-threaded execution:** Processing large CSV files locally quickly hits CPU limits. Even trivial mistakes (like accidental `print()` spam) freeze the terminal because everything runs in one process.
- **Ad-hoc parameter passing:** Environment variables (e.g., `THRESHOLD=21` for Exercise 12) must be exported manually per terminal session. When switching between exercises it is easy to leave stale values in the shell.
- **No distributed cache equivalent:** Files such as `stopwords.txt`, `dictionary.txt`, or `business_rules.txt` must sit next to the scripts. Copying and keeping them in sync across directories was error-prone before Hadoop’s `-file` option.
- **Output management:** Local runs drop results into the terminal or temporary files. Tracking even the first 10 outputs manually is tedious, and scaling that workflow to all 31 exercises would be unmanageable.

### How Hadoop Simplified the Workflow
- **Streaming handles plumbing:** Hadoop Streaming guarantees the mapper output is sorted before hitting the reducer, so the classic Unix pipeline mistakes disappear. Each job definition is self-contained.
- **Parallelism for free:** Even on a single node, Hadoop splits input into blocks and can launch multiple mapper tasks. Jobs that took ~45 seconds locally dropped below 10 seconds when HDFS fed multiple tasks in parallel.
- **Reusable job commands:** Each exercise has a single `hadoop jar ...` invocation that can be copy-pasted or scripted, replacing long ad-hoc shell pipelines.
- **Auditable outputs:** Every run leaves an immutable `_SUCCESS` flag and timestamped `part-*` outputs in HDFS. Combined with the Web UI, it is easy to prove when data was produced and by which job ID.

### Takeaway
Classic local runs are convenient for quick smoke tests, but they do not scale operationally. Hadoop introduced structure: reproducible job commands, automatic sorting, auditable outputs, and lightweight parallelism. After migrating each exercise to Hadoop, rerunning the entire set became a scripted, deterministic process instead of a collection of ad-hoc shell pipelines.

---

## Conclusion

This project successfully demonstrates:

1. **Python Implementation**: The first 10 MapReduce exercises implemented with only the Python standard library, following consistent coding patterns and best practices.

2. **Local Testing**: Ability to test mappers and reducers locally using Unix pipes before deploying to Hadoop.

3. **Hadoop Setup**: Complete installation and configuration of Hadoop 3.3.6 on a local machine, including Java setup, SSH configuration, and XML file configuration.

4. **Distributed Processing**: Deployment of Python scripts to Hadoop through Hadoop Streaming, covering:
   - Standard map-reduce jobs
   - Multi-file ingestion (Exercise 2)
   - Two-stage job chaining (Exercise 8)
   - Reducer-side optimizations with combiners (Exercise 9)

5. **Output Verification**: Multiple methods to verify job outputs:
   - Command-line tools (`hdfs dfs -cat`, `hdfs dfs -ls`)
   - NameNode Web UI for file browsing
   - ResourceManager Web UI for job monitoring

The project provides a comprehensive learning experience in Big Data processing, from basic word counting to complex distributed data transformations, all implemented in Python and executed on Hadoop.

---

## Appendix: Quick Reference Commands

### HDFS Commands
```bash
# List directory
hdfs dfs -ls /path/to/directory

# Create directory
hdfs dfs -mkdir -p /path/to/directory

# Upload file
hdfs dfs -put local_file.txt /hdfs/path/

# Download file
hdfs dfs -get /hdfs/path/file.txt local_file.txt

# View file
hdfs dfs -cat /hdfs/path/file.txt

# Delete file/directory
hdfs dfs -rm /hdfs/path/file.txt
hdfs dfs -rm -r /hdfs/path/directory

# Copy file
hdfs dfs -cp /source/path /dest/path
```

### Hadoop Service Management
```bash
# Start HDFS
start-dfs.sh

# Stop HDFS
stop-dfs.sh

# Start YARN
start-yarn.sh

# Stop YARN
stop-yarn.sh

# Check running services
jps
```

### Job Execution
```bash
# Set streaming JAR
export STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar

# Run job
hadoop jar "$STREAMING_JAR" \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py \
  -input /input/path \
  -output /output/path
```

---

**Report Generated**: November 2024  
**Project**: Hadoop MapReduce Exercises (Mandatory Set)  
**Total Exercises Covered in Report**: 10  
**Hadoop Version**: 3.3.6  
**Python Version**: 3.x

