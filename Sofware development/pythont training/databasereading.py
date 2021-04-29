import sqlite3
conn=sqlite3.connect('SS3.db'); #connect to the database
c=conn.cursor(); #create a cursor object
c.execute("SELECT *from information where AGE=14"); # select *from table_name header=row_value
a=c.fetchone(); #Read one row
print(a);
print(a[0]); #slice operator
