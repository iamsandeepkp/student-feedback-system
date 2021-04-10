#!/usr/bin/python3
import cgi 
import sys
import mysql.connector

db=mysql.connector.connect(host='localhost',port=3306,database='sfs',user='root',password='root')
cur=db.cursor()

form=cgi.FieldStorage()

course_code = form.getvalue('course_code')
username = form.getvalue('id')

cur.execute("select sem,sem_year from course_table where id='{}' and course_code='{}'".format(username,course_code))
myresult = cur.fetchall()

print("""
	<html>
	<head>
		<title>VERIFY GET DATA</title>
			
			
	</head>
	<body>
	<div id="header">
	<center>Tezpur University Student Feedback System</center>
	</div>
		
	<form action="showdata.py" method="post">	
		<input type="hidden" name="sem_year" value="{}">
		<input type="hidden" name="course_code" value="{}">
		SELECT SEMESTER :- <select name="selected_sem">
	""".format(myresult[0][1],course_code))
for x in myresult:
	print("""<option value="{}">{}</option>""".format(x[0],x[0]))

print("""
		</select>
		<p><input type="submit" value="SUBMIT"></p>
		
	</form>
	</body>
	</html>
	""")



