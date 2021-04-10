#!/usr/bin/python3
import cgi 
import getpass
import sys
import telnetlib
import mysql.connector

db=mysql.connector.connect(host='localhost',port=3306,database='sfs',user='root',password='root')
cur=db.cursor()

form=cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('passw')

HOST = "192.168.125.6"

cur.execute("select roll from login where id='{}'".format(username))
myresult = cur.fetchall()

try:
	tn = telnetlib.Telnet(HOST,23, 10)

	tn.read_until(b"login: ")
	tn.write(username.encode('ascii') + b"\n")
	tn.read_until(b"Password: ")
	tn.write(password.encode('ascii') + b"\n")

	tn.write(b"ls\n")
	
	tn.write(b"exit\n")

	tn.read_all().decode('ascii')
	tn.close()

	x=1
except:
	x=-1

print("""
	<html>
	<head>
		<title>VERIFY LOGIN</title>
		
		<style>
        body {background-color: powderblue;}
		#header
		{
		background-color:DodgerBlue;
		text-align: center;
		vertical-align: middle;
		letter-spacing: 3px;
		word-spacing: 10px;
		height: 100px;
		width: 100%;
		font-size: 50px;
        </style>
		
	</head>
	<body>
	""")

if x==1:
	print("""
		<div id="header">
		<center>Tezpur University Student Feedback System</center>
		</div>
		<center>
		<h1>WELCOME {}</h1>
		</center>
		""".format(username))

	cur.execute("select distinct course_code from course_table where id='{}'".format(username))
	myresult = cur.fetchall()
	if len(myresult) == 0:
		print("""			
			<center>
				<h1>NO COURSES HAVE BEEN FOUND UNDER THIS USER</h1>
				<p><a href="index.py">GO HOME</a></p>
			</center>
			""")
	else:
		print("""
			<form method="post" action="getdata.py">
				<input type="hidden" name="id" value="{}">
				COURSE CODE : <select name="course_code">
			""".format(username))
	
		for cc in myresult:
			print("""
				<option value="{}">{}</option>
				""".format(cc[0],cc[0]))

		print("""
			</select>
			<p><input type="submit" value="SUBMIT HERE"></p>
			</form>
			""")
		
else:
	print("""
		<div id="header">
		<center>Tezpur University Student Feedback System</center>
		</div>
		<center>
		<p><h1>INCORRECT USERNAME OR PASSWORD</h1></p>
		<p><a href="index.py">GO HOME</a></p>
		</center>
		""")
	
print("""
	</body>
	</html>
	""")


