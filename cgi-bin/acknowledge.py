import cgi 
import sys
import mysql.connector

db=mysql.connector.connect(host='localhost',port=3306,database='sfs',user='root',password='root')
cur=db.cursor()

form2=cgi.FieldStorage()
course_code=form2.getvalue('course_code')
sem_year=form2.getvalue('selected_year')
attendance=form2.getvalue('attendance')
weekly_duration=form2.getvalue('weekly_duration')
last_SGPA=form2.getvalue('last_SGPA')


prereq_knowledge=form2.getvalue('prereq_knowledge')
course_relevance=form2.getvalue('course_relevance')
logically_sequenced=form2.getvalue('logically_sequenced')
course_relevance_society=form2.getvalue('course_relevance_society')
outcomes_fulfilled=form2.getvalue('outcomes_fulfilled')
employability_suitability=form2.getvalue('employability_suitability')
knowledge_upgradation=form2.getvalue('knowledge_upgradation')
tut_class_relevance=form2.getvalue('tut_class_relevance')
course_content_appropriate=form2.getvalue('course_content_appropriate')
course_team_learning=form2.getvalue('course_team_learning')

cur.execute("insert into course_and_content values('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(course_code,sem_year,attendance,weekly_duration,last_SGPA,prereq_knowledge,course_relevance,logically_sequenced,course_relevance_society,outcomes_fulfilled,employability_suitability,knowledge_upgradation,tut_class_relevance,course_content_appropriate,course_team_learning))
db.commit()

print("""
	<html>
	<head>
		<title>ACK</title>
		
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
	
	<div id="header">
	<center>Tezpur University Student Feedback System</center>
	</div>
	<center>
	<p><h1>Thank you!</h1></p>
	<p><h1>Your feedback is successfully submitted.</h1></p>
	<p><a href="index.py">GO HOME</a></p>
	</center>
	</body>
	</html>
	""")