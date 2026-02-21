from detector import detect_suspicious_activity
from logger import read_logs

LOG_FILE = "../logs/sample.log"

def main():
    logs = read_logs(LOG_FILE)

    print("🔍 Analyzing Logs...\n")

    for line in logs:
        if detect_suspicious_activity(line):
            print("⚠️ ALERT:", line.strip())

if __name__ == "__main__":
    main()
