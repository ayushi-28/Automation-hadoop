#!/usr/bin/python

import commands
import time
import cgi,cgitb;
import os
cgitb.enable()

print "Content-type:text/html"
print ""


#  taking data from apache and storing into web variable 
web=cgi.FieldStorage()

#getting cluster name
nam=web.getvalue('namee')

#  getting size of cluster
size=web.getvalue('sz')

# checking shutdown permission
shut=web.getvalue('shut')

#checking hadoop version
version=web.getvalue('version')


cont=[]
ip=[]

start=os.system('sudo systemctl start docker')

time.sleep(8)

if start==0:
	if version=='1':

		print "<h1>"
		print  'Launching version1 cluster:  '+nam+' '
		print '</h1>'
		print '<pre>'
		print "Launching Containers..."
		for i in range(int(size)):
			cont_id=commands.getoutput('sudo docker run -itd centos6:hadoopv1 /bin/sh')
			cont.append(cont_id)


		print cont
	
		print " List of all IP's :"
		print "</br>"
		for i in cont:
			ips=commands.getoutput('sudo docker exec '+i+' hostname -i')
			ip.append(ips)
	
		print ip


		print commands.getoutput('sudo docker cp /root/Desktop/docnamenode/hdfs-site.xml '+cont[0]+':/etc/hadoop/ ')
		print commands.getoutput('sudo docker cp /root/Desktop/docnamenode/core-site.xml '+cont[0]+':/etc/hadoop/ ')
		print commands.getoutput('sudo docker exec '+cont[0]+' hadoop namenode -format')
		time.sleep(8)
		print commands.getoutput('sudo docker exec '+cont[0]+' hadoop-daemon.sh start namenode' )
		time.sleep(2)
        	print commands.getoutput('sudo docker exec '+cont[0]+' jps')


		for i in range(1,int(size)):
			print commands.getoutput('sudo docker cp /root/Desktop/docdatanode/hdfs-site.xml '+cont[i]+':/etc/hadoop/' )
			print commands.getoutput('sudo docker cp /root/Desktop/docdatanode/core-site.xml '+cont[i]+':/etc/hadoop/' )
			print commands.getoutput('sudo docker exec '+cont[i]+' hadoop-daemon.sh start datanode')
			time.sleep(1)
			print commands.getoutput('sudo docker exec '+cont[i]+' jps')
		
		if shut=='yes':
			print 'Shutting down and removing containers...'
			for i in range(0,int(size)):
				print commands.getoutput('sudo docker kill '+cont[i])
				print commands.getoutput('sudo docker rm '+cont[i])
	

			print 'ALL containers has been shut down and removed..!!!'
		else:
			print 'Cluster is up!!Enjoy our services'

		print '</pre>'
		
	else:

		print "<h1>"
     		print  'Launching version2 cluster:  '+nam+' '
        	print '</h1>'
        	print '<pre>'
     		print "Launching Containers..."
        	for i in range(int(size)):
                	cont_id=commands.getoutput('sudo docker run -itd centos6:hadoopv2  /bin/sh')
                	cont.append(cont_id)


        	print cont

       		print " List of all IP's :"
        	print "</br>"
        	for i in cont:
                	ips=commands.getoutput('sudo docker exec '+i+' hostname -i')
                	ip.append(ips)

        	print ip


        	print commands.getoutput('sudo docker cp /root/Desktop/docnamenode/v2/hdfs-site.xml '+cont[0]+':/hadoop2/etc/hadoop/ ')
        	print commands.getoutput('sudo docker cp /root/Desktop/docnamenode/v2/core-site.xml '+cont[0]+':/hadoop2/etc/hadoop/ ')
       	 	print commands.getoutput('sudo docker exec '+cont[0]+' /bin/bash -c "/hadoop2/bin/hdfs namenode -format"')
        	print commands.getoutput('sudo docker exec '+cont[0]+' /bin/bash -c "/hadoop2/sbin/hadoop-daemon.sh start namenode" ' )
       		time.sleep(2)
        	print commands.getoutput('sudo docker exec '+cont[0]+' jps')


        	for i in range(1,int(size)):
                	print commands.getoutput('sudo docker cp /root/Desktop/docdatanode/v2/hdfs-site.xml '+cont[i]+':/hadoop2/etc/hadoop/' )
			print commands.getoutput('sudo docker cp /root/Desktop/docdatanode/v2/core-site.xml '+cont[i]+':/hadoop2/etc/hadoop/' )
                	print commands.getoutput('sudo docker exec '+cont[i]+' /bin/bash -c "/hadoop2/sbin/hadoop-daemon.sh start datanode" ')
                	time.sleep(1)
        	        print commands.getoutput('sudo docker exec '+cont[i]+' /bin/bash -c jps')
	
                if shut=='yes':
                        print 'Shutting down and removing containers...'
                        for i in range(0,int(size)):
                                print commands.getoutput('sudo docker kill '+cont[i])
                                print commands.getoutput('sudo docker rm '+cont[i])


                        print 'ALL containers has been shut down and removed..!!!'
                else:
                        print 'Cluster is up!!Enjoy our services'

                print '</pre>'

else:
	print '	OOps!!!There was some error starting  docker services!!'
	print 'Try again after some time!!'

			
