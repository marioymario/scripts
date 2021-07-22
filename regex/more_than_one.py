import re
"""the function checks if the text passed
includes the letter a upper or lower case
more than one."""
def repeating_letter_a(text):
	result = re.search(r"[aA][^aA][*aA]",  text)
	return result != None


