import csv

file_for_reading=open('data.csv','r'); #Open file for writing
reader=csv.DictReader(file_for_reading,delimiter=','); #create a reader object

field_names=['First name','Last name','Email']; #python list definition
file_for_writing=open('new_datass.csv','w'); #open file for writing


writer=csv.DictWriter(file_for_writing,field_names,delimiter=','); #create a dictwriter object
writer.writeheader(); #this writes the field_names as header
for i in reader:
    writer.writerow(i); #write data to csv
