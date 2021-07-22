import re
def rearrange(name):
    """function that has two capture groups
    one for after and anotherone before the comma
    if not, if result is none if does not match the result and will return as is.
    if captured it return a rearranged version of the string"""
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
            return name
    else: return "{} {}".format(result[2], result[1])


