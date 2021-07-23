import re 
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
# including the notation marks

print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
# will catch the .?!

# re.split(r"the|a", "One sentence. Another one? And the last one!")
# ['One sentence. Ano', 'r one? And ', ' l', 'st one!']

### this one hides an email address
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "hevia, mario"))