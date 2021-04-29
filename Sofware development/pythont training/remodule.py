import re

file=open('data.txt','r'); #open file for reading
data=file.read(); #read content of file
file.close(); #close file

''' Matching numbers '''
pattern=re.compile(r'\d{2,4}.\d{2,4}.\d{2,4}.\d*'); #pattern to search for
matches=pattern.finditer(data); #search for match in data
for match in matches:
    print(match);

'''Matching names'''
pattern=re.compile(r'[a-zA-Z](r|rs|s).[A-Za-z]\w*'); #pattern to searchfor
matches=pattern.finditer(data); #search for match in data
for match in matches:
    print(match);

'''Matching Urls'''

pattern=re.compile(r'https.{2,3}[a-zA-Z]\w{2,3}.*'); #pattern to search for
matches=pattern.finditer(data); #search for pattern in data
for match in matches:
     print(match);