import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]\: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    else: return"{} ({})".format(result[1], result[2])

