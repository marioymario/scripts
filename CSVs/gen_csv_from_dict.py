import csv
import os

user = [
    {"name": "sol mansi", "username": "solm", "department": "IT infraextructure"},
    {"name": "Lio Nelson", "username": "leo", "department": "User Experience REaserch"},
    {"name": "charlie grey", "username": "greyc", "department": "Development"}
    ]
keys = ["name", "username", "department"] # def keys

with open('by_dept.csv', 'w')as by_department:
    writer = csv.DictWriter(by_department, keys)
    writer.writeheader() # method1, create first line csv
    writer.writerows(user) # method 2 will turn the list of dict on lines
