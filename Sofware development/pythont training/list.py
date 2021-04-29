'''HERE WILL BE DOING A QUICK REVISION ON PYTHON LIST DATA TYPE'''
Data=['Chidalu',13,'Apple','Orange','Pineapple','Pencil','Tables']; #python list definition
print(Data);

print(Data[2]); #application of slice operator

data=['money','watch','hand-bag']; #python list definition
datas=Data+data; #list concatenation
print(datas);

'''len()'''
lent=len(datas); #gives the lengthof a list
print(lent);
'''list repitition'''
print(Data*2); #list repition(prints the list twice

'''List built-in functions'''
dict={'name':'chidalu','age':14}; #python dictionary definition
a=list(dict); #converts the dictionary to a list
print(a);

b=max(a); #gives the maximum value in a list
print(b);

c=min(a); #gives the minimum value in a list
print(c);

data=['Bank','Address','Phone-Number','Credit-Number']; #python list definition
print(data.remove('Bank')); #removes the bank value in a list
print(data);
'''reshufulling a list'''
data.sort(); #reshuffles a list
print(data);
data.reverse(); #taks the value from the back to the top
print(data);

'''Appending to a list'''
data=[]; #python list declration
names=['Ade','Shola','Bola','Mathew','Franklin']; #python list definition
for i in (names):
    data.append(i); #append the values in the names list to the data list

print(data);
'''
data.remove('Bank'); #removes the bank in the list
data.append('name'); #appends the name to a list data
data.sort();# shufulles a list
data.reverse(); #reverses a list

+

*

len()

[]

[:]


'''

