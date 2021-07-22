import re
def check_character_groups(text):
    """check if the text passed has at least 
    2 groups of alphanumeric characters
    including letters, numbers, and underscores
    separated by one or more whitespace characters."""
    result = re.search(r"\w+\s", text)
    return result != None