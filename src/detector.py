def detect_suspicious_activity(log_line):
    keywords = ["failed", "error", "unauthorized", "attack"]
    for word in keywords:
        if word in log_line.lower():
            return True
    return False
