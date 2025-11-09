# Hadoop MapReduce Exercises

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Hadoop](https://img.shields.io/badge/Apache%20Hadoop-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=white)

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

## Installation

### For macOS and Linux

#### Step 1: Install Java 11

Hadoop 3.3.6 requires Java 8 or 11 (not Java 21+).

**macOS (using Homebrew):**
```bash
# Install Java 11
brew install openjdk@11

# Set JAVA_HOME
export JAVA_HOME=$(/usr/libexec/java_home -v 11)
export PATH=$JAVA_HOME/bin:$PATH

# Verify installation
java -version
```

**Linux (Ubuntu/Debian):**
```bash
# Install OpenJDK 11
sudo apt-get update
sudo apt-get install openjdk-11-jdk

# Set JAVA_HOME (add to ~/.bashrc or ~/.zshrc)
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

# Verify installation
java -version
```

#### Step 2: Download and Install Hadoop

```bash
# Download Hadoop 3.3.6
cd ~
wget https://archive.apache.org/dist/hadoop/core/hadoop-3.3.6/hadoop-3.3.6.tar.gz

# Extract Hadoop
tar -xzf hadoop-3.3.6.tar.gz

# Move to installation directory
sudo mv hadoop-3.3.6 /usr/local/hadoop

# Set ownership
sudo chown -R $USER /usr/local/hadoop
```

#### Step 3: Configure Environment Variables

Add the following to `~/.bashrc` (Linux) or `~/.zshrc` (macOS):

```bash
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

#### Step 4: Configure SSH for Localhost

Hadoop uses SSH to start and stop daemons. Set up passwordless SSH:

```bash
# Generate SSH key (if not exists)
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa

# Add to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Set permissions
chmod 0600 ~/.ssh/authorized_keys

# Test SSH
ssh localhost "echo 'SSH works!'"
```

**Note for macOS**: Enable Remote Login in System Preferences > Sharing > Remote Login.

#### Step 5: Configure Hadoop Files

**Edit `$HADOOP_HOME/etc/hadoop/core-site.xml`:**
```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

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

```bash
hdfs namenode -format
```

#### Step 8: Start Hadoop Services

```bash
# Start HDFS (NameNode, DataNode, SecondaryNameNode)
start-dfs.sh

# Start YARN (ResourceManager, NodeManager)
start-yarn.sh

# Verify services are running
jps
# Should show: NameNode, DataNode, SecondaryNameNode, ResourceManager, NodeManager
```

#### Step 9: Verify Installation

```bash
# Check HDFS
hdfs dfs -ls /

# Access web UIs
# NameNode: http://localhost:9870
# ResourceManager: http://localhost:8088
```

### For Windows

#### Option 1: Using WSL (Windows Subsystem for Linux) - Recommended

1. **Install WSL 2**:
   ```powershell
   wsl --install
   ```

2. **Install Ubuntu** from Microsoft Store

3. **Follow the macOS/Linux installation steps above** inside the WSL Ubuntu terminal

#### Option 2: Native Windows Installation

1. **Install Java 11**:
   - Download from [Oracle](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html) or [Adoptium](https://adoptium.net/)
   - Set `JAVA_HOME` environment variable to Java installation path
   - Add `%JAVA_HOME%\bin` to PATH

2. **Install Hadoop**:
   - Download Hadoop 3.3.6 from [Apache Hadoop](https://archive.apache.org/dist/hadoop/core/hadoop-3.3.6/)
   - Extract to `C:\hadoop` (or your preferred location)
   - Set `HADOOP_HOME` environment variable

3. **Install SSH**:
   - Use [OpenSSH for Windows](https://github.com/PowerShell/Win32-OpenSSH) or [Cygwin](https://www.cygwin.com/)
   - Configure passwordless SSH for localhost

4. **Configure Hadoop**:
   - Edit configuration files in `%HADOOP_HOME%\etc\hadoop\`
   - Use Windows-style paths (e.g., `file:///C:/hadoop/hadoop_data/hdfs/namenode`)

5. **Start Hadoop**:
   ```cmd
   %HADOOP_HOME%\sbin\start-dfs.cmd
   %HADOOP_HOME%\sbin\start-yarn.cmd
   ```

**Note**: Native Windows installation can be more complex. WSL is recommended for easier setup and better compatibility.

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

