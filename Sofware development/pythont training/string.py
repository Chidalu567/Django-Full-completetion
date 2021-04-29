'''We Will be looking at python string data type'''

sentence1='This is how i like to code in python'; #python string
if sentence1.isalpha: #returns true if string isalpha
    print('true');

string='12345'; #python string definition
if string.isdigit: #returns true if string is digit
    print('True');

string='123 is basic counting for kids'; #python string
if string.isalnum: #retruns true if string is alphanumeric
    print('String is alpha numeric');

string=' '; #python string
if string.isspace: #Returns ture if string is a space
    print('String is a space');

string='THIS IS ABOUT me';
if string.isupper: #reutrns true if string is uppercased
    print('String is uppercase');

string='this is about me';
if string.islower: #returns true if string is lowercased
    print('String is lowercase');
    print(len(string)); #gives the length of a string

string='123.45'; #python string definition
if string.isdecimal: #Returns if string is a decimal or float
    print('String is a float number');

string='The Chairman Of The University Of Lagos State'; #python string definition
if string.istitle: #returns true if string is titlecased
    print('String is titlecased');

string='ade father is a daddy'; #string defintion
string2=string.capitalize(); #capitalize the string
print(string2);

string='ade father is a man'; #python string definition
string2=string.upper(); #convert string to uppercase
print(string2);
string3=string2.lower(); #convert string to lower case
print(string3);


'''Main Built-in functions in python string data type'''

string='this is a string'; #python string definition
string2=string.encode('utf-8'); #encodethe string in byte format
'''The byte-format is used when sending message to another computer cmd'''
print(string2);

string3=string2.decode('utf-8'); #decode string frombyte-format to string format
print(string3);

Text='This is from me to you'; #python string definition
if Text.endswith('you',13): #returns true if string endswith('you')
    print('String endswith you');
if Text.startswith('This',0): #returns true if string startswith('This')
    print('String startswith This');

'''Less used built-in functions'''
random_string='hello,hello,i,love,me,hello,i,love,God,hello , ,e ,'; #python string defintion
arranged_string=random_string.replace(',',' '); #replace , with space
print(arranged_string);
print(arranged_string.find('love')); #gives the index position of a word in a string
 #also search for a word in a string





