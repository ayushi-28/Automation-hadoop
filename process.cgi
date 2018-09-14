#!/usr/bin/python2

import  cgi,cgitb
import  commands,time
import os
cgitb.enable()


print "Content-type:text/html"
print ""


#  taking data from apache and storing into web variable 
web=cgi.FieldStorage()
fileitem =web['file']
#print fileitem

print "<pre>"
fl= fileitem.filename
print fl

#print commands.getoutput("sudo cp "+fl+" /myuploads")

x,y=commands.getstatusoutput("sudo find / -name "+fl) 
print x
print y
time.sleep(4)

choic=web.getvalue('choice')
print choic

folder=web.getvalue('folder')
print folder

word=web.getvalue('word')

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/hadoop-daemon.sh start namenode')
time.sleep(5)

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/hadoop-daemon.sh start datanode')
time.sleep(5)

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/yarn-daemon.sh start resourcemanager')
time.sleep(5)

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/yarn-daemon.sh start nodemanager')
time.sleep(5)

print commands.getoutput("/usr/bin/sudo /hadoop2/bin/hdfs dfsadmin -safemode leave")

print commands.getoutput("/usr/bin/sudo /hadoop2/bin/hdfs dfs -put "+y+" /confidential")


if choic=="grep":
	print commands.getoutput("/usr/bin/sudo /hadoop2/bin/yarn jar  /hadoop2/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar "+choic+"  /confidential/"+fl+" /"+folder+" "+word)
	time.sleep(60)
	print commands.getoutput("/usr/bin/sudo  /hadoop2/bin/hdfs dfs -cat /"+folder+"/part-r-00000")
        time.sleep(3)
        commands.getoutput('/usr/bin/sudo /hadoop2/bin/hdfs dfs -rm /confidential/'+fl)
        time.sleep(4)

elif choic=="sudoku":
	print commands.getoutput("/usr/bin/sudo mkdir /"+folder)
	print commands.getoutput("/usr/bin/sudo /hadoop2/bin/yarn jar  /hadoop2/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar "+choic+" "+"/"+y+" >> "+"/"+folder+"/"+fl)
	time.sleep(8)
	print commands.getoutput("/usr/bin/sudo cat /"+folder+"/"+fl)
	

else: 
	print commands.getoutput("/usr/bin/sudo /hadoop2/bin/yarn jar  /hadoop2/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar "+choic+"  /confidential/"+fl+" /"+folder)
	time.sleep(60)
	print commands.getoutput("/usr/bin/sudo  /hadoop2/bin/hdfs dfs -cat /"+folder+"/part-r-00000")
	time.sleep(6)
	#print commands.getoutput('/usr/bin/sudo /hadoop2/bin/hdfs dfs -rm /confidential/'+fl)
	#time.sleep(4)

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/hadoop-daemon.sh stop namenode')
time.sleep(7)

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/hadoop-daemon.sh stop datanode')
time.sleep(7)

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/yarn-daemon.sh stop resourcemanager')
time.sleep(7)

print commands.getoutput('/usr/bin/sudo /hadoop2/sbin/yarn-daemon.sh stop nodemanager')
time.sleep(7)

print "</pre>"
