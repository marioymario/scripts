import csv
## this is a list of lists
hosts = [["workstation.local", "192.168.25.46"],
        ["webserver.cloud", "10.2.5.6"]]
## let's open the file in write mode
## width block that we saw before so 
## we don't forget to close it.

with open('host.csv', 'w')as hosts_csv: 

## call the writer function of the CSV 
## module with this file as a parameter.
    
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
## writer now an instance of the csv.wrtiter class

## write rows or write row, we have all the data so we do rows
"""

import csv
hosts = [["workstation.local", "192.168.25.46"],
        ["webserver.cloud", "10.2.5.6"]]
with open('host.csv', 'w')as hosts_csv: 
     writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

"""

