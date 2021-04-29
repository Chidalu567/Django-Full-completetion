'''We will be doing a quick revision on dictionary data type in python'''
customer_data={'Name':['Prince','Chidalu','Fortune','Ebuka','Jeff','Voscan','Ugo'],
                'ID':['001','002','003','004','005','006','007'],
                'Item':['Piano','Laptop','Software','Phone','Software','Computers','Software'],
                'Amount':[100000,700000,300000,500000,300000,500000,300000],
                'Address':['no-2-chris-idowu-street','no-2-chris-idowu-street','no-2-chris-idowu-street','no-2-chris-idowu-street','no-2-chris-idowu-street','no-2-chris-idowu-street','no-2-chris-idowu-street']
               }; #python dictionary definition
print(customer_data);
data={'name':'chidalu','Age':15,'Id':'001','Code':'Python'}; #python dictionary definition
new_data={'Church':'Redeem'}; #python dictionary declaration
print('----------------');
print(data.items()); #groups each key and its value therefore we can loop using for loop
#for key,value in data.items():
#
#
'''Built-in functions in dictionary'''
copied=data.copy(); #copy a dictionary into another
print(copied);
print(copied.keys()); #gives the keys in a dictionary
print(copied.values()); #gives the values in a dictionary
print(copied.get('name')); #get the value of a key
'''More'''
print(customer_data.keys());
print(customer_data.values());
print(customer_data.get('Amount'));
a=str(customer_data.get('Amount'));
print(a);


