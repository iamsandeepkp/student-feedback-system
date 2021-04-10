#!/usr/bin/python3
import cgi 
import mysql.connector
db=mysql.connector.connect(host='localhost',port=3306,database='sfs',user='root',password='root')
cur=db.cursor()
form=cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('passw')

cur.execute("select * from login where id='{}'".format(username))
myresult = cur.fetchall()
print("""
	<html>
	<head>
		<title>VERIFY LOGIN</title>
	</head>
	<body>
	""")
if len(myresult) == 0:
	print("""
		<center>
		<p><h1>USERNAME NOT FOUND</h1></p>
		<p><a href="index.py">GO HOME</a></p>
		</center>
		""")

else:
	cur.execute("select passw from login where id='{}'".format(username))
	myresult1=cur.fetchall()
	actual=str(myresult1[0][0])
	splitter=actual.split("'")
	myresult1=splitter[1]

	cur.execute("select md5('{}')".format(password))
	myresult2=cur.fetchall()
	if myresult1 == myresult2[0][0]:
		print("""
			<center>
			<h1>WELCOME USER</h1>

			</center>
			""")
	else:
		print("""
			<center>
			<p><h1>INCORRECT PASSWORD</h1></p>
			<p><a href="index.py">GO HOME</a></p>
			</center>
			""")

print("""
	</body>
	</html>
	""")