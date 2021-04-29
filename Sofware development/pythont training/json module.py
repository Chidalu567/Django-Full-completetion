import json
import os

#storing data in json file
#this is the data to be stored in json file
data={
    'NAMES':['chidalu','philip','fortune'],
    'AGE':[14,12,13],
    'CLASS':['SS1','SS2','SS3']
}; #python dictionary definition

#storing file in json format with decoration(indent)
jsondata=json.dumps(data,indent=3); #dump data in json file with indent of 2
print(jsondata);

#storing file in json format with decoration (separators)
jsondata2=json.dumps(data,separators=('-','='));
''' the - separates the key from value and =  separates the value from adjacent keys'''
print(jsondata2);

file=open('decoratedjson.json','w'); #open file for writing
json.dump(jsondata,file); #dump json data in file
json.dump(jsondata2,file); #dump json data in file
file.close(); #close file

file=open('decoratedjson.json','r'); #open file foe reading
data=file.read(); #read file content
file.close(); #close file
