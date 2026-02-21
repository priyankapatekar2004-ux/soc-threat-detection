def read_logs(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        return []
