#!/usr/bin/python2

import cgi
import mysql.connector as mysql
import commands

print "Content-type:text/html"  #the type of content will be html
print ""

data=cgi.FieldStorage()
eid=data.getvalue('emailid')
passwd=data.getvalue('passw')

commands.getoutput('systemctl start mariadb')
conn=mysql.connect(user='root',password='123',database='hadoop',host='127.0.0.1')

cur=conn.cursor()
cur.execute('Select * from user_det;')
results = cur.fetchall()
