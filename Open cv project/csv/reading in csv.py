import csv

file=open('datas.csv','r'); #open file for reading
reader=csv.DictReader(file,delimiter=','); #create  a dict reader object

for i in reader:
    print(i['EMAIL'])
