import sqlite3
conn=sqlite3.connect('SS3.db'); #create a database and connect to the database
c=conn.cursor(); #create a cursor object
c.execute('''CREATE TABLE information
            (NAMES text,AGE real,WEIGHT real,GRADE text,FOOD text,COURSE text)'''); #create a table named information
c.execute('''INSERT INTO information VALUES ('chidalu',14,45,'A','plantain and egg','computer engineer')'''); #insert into table_name values()

conn.commit(); #save database
conn.close(); #close database


