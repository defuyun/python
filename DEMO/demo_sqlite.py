#!/usr/bin/python

import sqlite3
import os

sql = 'test.db'

firstflag = False if os.path.exists(sql) else True

dbh = sqlite3.connect(sql)
cursor = dbh.cursor()

if firstflag:
	cursor.execute('create table user(\
					id varchar(20) primary key,\
					name varchar(20),\
					password varchar(30));')

cursor.execute('insert into user(id,name) values (\'1\',\'Cake\');')
cursor.execute('insert into user(id,name) values (\'2\',\'Cakes\');')
cursor.execute('insert into user(id,name) values (\'3\',\'More Cakes\');')

print cursor.rowcount # gives how many item (rows)

cursor.execute('select * from user where id=\'1\' or id=\'2\'')
print cursor.fetchall() # [(u'1', u'Cake', None), (u'2', u'Cakes', None)]