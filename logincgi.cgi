#!/usr/bin/python2

import cgi
import mysql.connector as mysql
import commands
import webbrowser

print "Content-type:text/html"  #the type of content will be html
print ""

data=cgi.FieldStorage()
Name=data.getvalue('name')
Email=data.getvalue('email')
Username=data.getvalue('username')
Password=data.getvalue('pass')
Confpass=data.getvalue('confirmpass')
'''
print Name
print Email
print Username
print Password
print Confpass
'''

#commands.getoutput('systemctl start mariadb')
conn=mysql.connect(user='root',password='123',database='hadoop',host='127.0.0.1')
#print conn.is_connected()

cur=conn.cursor()
cur.execute('INSERT INTO user_det(FullName , Username , Password , Email  ) VALUES(%s,%s,%s,%s)',(Name,Username,Password,Email))
conn.commit()


