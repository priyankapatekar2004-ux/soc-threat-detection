SOC Threat Detection System

Description:
This project is a simple Security Operations Center (SOC) threat detection tool developed using Python. It analyzes system log files and identifies suspicious activities such as failed login attempts, unauthorized access attempts, and possible attack indicators.

The program scans log entries and checks for specific keywords related to security threats. If suspicious activity is detected, the system generates an alert message.

Features:

* Reads and analyzes log files
* Detects failed login attempts
* Identifies unauthorized access
* Generates alerts for suspicious activity
* Simple and lightweight log analysis tool

Project Files:

* main.py : Main program that runs the log analysis
* detector.py : Detects suspicious keywords in log entries
* logger.py : Reads the log file
* sample.log : Sample log file used for testing

Requirements:

* Python 3.x
* No external libraries required

How to Run:

1. Navigate to the src folder.
2. Run the following command:

python main.py

Example Log Entries:
User login successful
Failed password attempt
Unauthorized access detected
System running normally

Example Output:
Analyzing Logs...
ALERT: Failed password attempt
ALERT: Unauthorized access detected

Purpose:
This project demonstrates basic SOC log monitoring and threat detection concepts used in cybersecurity.

Author:
Cybersecurity Student / SOC Analyst Enthusiast

