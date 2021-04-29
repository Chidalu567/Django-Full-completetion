'''We Will Be Doing A quick revision on tuple data type in python'''
chemicals=('Fluorine','Chlorine','Boron','Iodine'); #python tuple definition

#operations in tuple
new=('Neon','Hydrogen-gas'); #python tuple definition
new_tuple=chemicals+new; #tuple concatenation
print(new_tuple);
print(new_tuple[2:5]); #slice operator
print(len(new_tuple)); #gives the length of the tuple
print(new_tuple*2); #repeats the tuple twice

'''Built-in functions in tuple'''
print(max(new_tuple)); #gives the max value in a tuple
print(min(new_tuple)); #gives the min value in a tuple
data=['Electro-Negativity','Gas']; #python list definition
print(tuple(data));#converts a list to a tuple