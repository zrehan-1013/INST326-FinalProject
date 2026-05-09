# INST326-FinalProject
Cyber Security Log Analyzer

## Project Overview
A cyber security log analyzer that cleans and formats log files to show log events such as failed login attempts, brute force actvity, and suspicous IPs

# Features

- Reads log files from the command line
- Parses log entries into Python objects
- Counts successful login attempts
- Counts failed login attempts
- Detects suspicious IP addresses based on repeated failed logins
- Generates a formatted report


# Project Files

- `main.py`
  - Main entry point for the program

- `log_model.py`
  - Contains the `LogEntry` class

- `parser.py`
  - Reads and parses log files

- `analyzer.py`
  - Analyzes logs and detects suspicious activity

- `report.py`
  - Generates the output report

- `log.txt`
  - Sample log file used for testing

# How to Run the Program
```bash
chmod +x main.py 
python3 main.py log.txt 
```

## Example Output

```bash
-- Log Report --
Total successful logins: 5
Total failed logins: 11
Suspicious IPs: 3
Flagged IP addresses:
- 192.168.1.15
- 172.16.0.8
- 192.168.1.30
```



