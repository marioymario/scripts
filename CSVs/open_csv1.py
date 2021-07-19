import csv
f = open('csv_file.txt')
csv_f = csv.reader(f) ## an instance of the csv reader class
## now ititrerate and parse to get the info

for row in csv_f:
    name, phone, role = row
    print("NAME: {}, PHONE: {}, ROLE: {}".format(name, phone, role))

f.close()