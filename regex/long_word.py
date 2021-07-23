import re
def long_word(text):
    pattern = r"\w{7,}"
    result = re.findall(pattern, text)
    return result

