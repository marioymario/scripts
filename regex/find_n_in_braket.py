import re
log = "sdfgkhuerv ebvuhpvwervn, evuvbervibusdf[12355489]aeicufovb jgn fdvwrv::6"

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])