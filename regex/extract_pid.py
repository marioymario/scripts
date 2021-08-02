#!/usr/bin/env python3
import re
import sys

"""it display the date, time, and process id that's inside the square brackets. 
   it read each line of the syslog and pass the contents to the show_time_of_pid 
   function, and return this format: Jul 6 14:01:23 pid:29440."""

if len(sys.argv) !=2:
    print("USAGE:")
    print("{} <your requested log file".format(sys.argv[0]))
    sys.exit()

logfile =  sys.argv[1]
with open(logfile) as f:
    for line in f:
        pattern = r'^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]'
        result = re.search(pattern, line)
        if result is None:
            print(None)
        else: print("{} pid:{}".format(result[1],result[2]))


      