#!/usr/bin/python3
import cgi 
import sys
import mysql.connector

db=mysql.connector.connect(host='localhost',port=3306,database='sfs',user='root',password='root')
cur=db.cursor()

form2=cgi.FieldStorage()

selected_sem=form2.getvalue('selected_sem')
selected_year=form2.getvalue('sem_year')
course_code=form2.getvalue('course_code')

def printer():
	print("""
		<option value="5" selected>Strongly agree</option>
					<option value="4">Agree</option>
					<option value="3">Neutral</option>
					<option value="2">Disagree</option>
					<option value="1"Strongly disagree</option>
			</select>
		""")
print("""
	<html>
	<head>
		<title>SHOW DATA</title>
		
		
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
	
	<form action="acknowledge.py" method="post">
		<fieldset>
			<legend>Details of learner</legend>
			<p>Percentage of classes attended : <select name="attendance">
				<option value="5" selected>85-100</option>
				<option value="4">70-84</option>
				<option value="3">55-69</option>
				<option value="2">30-54</option>
				<option value="1">Below 30</option>
			</select>
			</p>
			<p>
			Duration spent for self-study of this course (Weekly) : <select name="weekly_duration" >
				<option value="5" selected>8-10 h</option>
				<option value="4">6-8 h</option>
				<option value="3">4-6 h</option>
				<option value="2">2-4 h</option>
				<option value="1">0-2 h</option>
			</select>
			</p>
			<p>
			SGPA in last semester : <select name="last_SGPA">
				<option value="5" selected>9 and above</option>
				<option value="4">8-9</option>
				<option value="3">7-8</option>
				<option value="2">6-7</option>
				<option value="1">Below 6</option>
			</select>
			</p>
		</fieldset>
		<center><h1>Students Feedback</h1></center>
		<fieldset>
			<legend>Course and Course Content</legend>
			<p>
				Your prerequisite knowledge was sufficient for understanding this course: <select name="prereq_knowledge">
					<option value="5" selected>Strongly agree</option>
					<option value="4">Agree</option>
					<option value="3">Neutral</option>
					<option value="2">Disagree</option>
					<option value="1"Strongly disagree</option>
			</select>
			</p>
			<p>
				The course was relevant in relation to the program of study : <select name="course_relevance">
					<option value="5" selected>Strongly agree</option>
					<option value="4">Agree</option>
					<option value="3">Neutral</option>
					<option value="2">Disagree</option>
					<option value="1"Strongly disagree</option>
			</select>
			</p>
			<p>
				Topics/ units were logically sequenced in the syllabus : <select name="logically_sequenced">
					<option value="5" selected>Strongly agree</option>
					<option value="4">Agree</option>
					<option value="3">Neutral</option>
					<option value="2">Disagree</option>
					<option value="1"Strongly disagree</option>
			</select>
			</p>
			<p>
				The course is relevant to the society and real life application : <select name="course_relevance_society">
					<option value="5" selected>Strongly agree</option>
					<option value="4">Agree</option>
					<option value="3">Neutral</option>
					<option value="2">Disagree</option>
					<option value="1"Strongly disagree</option>
			</select>
			</p>
			<p>
				Course contents fulfilled the targeted outcomes (course outcome) : <select name="outcomes_fulfilled">
					<option value="5" selected>Strongly agree</option>
					<option value="4">Agree</option>
					<option value="3">Neutral</option>
					<option value="2">Disagree</option>
					<option value="1"Strongly disagree</option>
			</select>
			</p>
			<p>
				The course is suitable in terms of employability : <select name="employability_suitability">
					<option value="5" selected>Strongly agree</option>
					<option value="4">Agree</option>
					<option value="3">Neutral</option>
					<option value="2">Disagree</option>
					<option value="1"Strongly disagree</option>
			</select>	
			</p>
			<p>
				The course fulfills the expectations in knowledge up-gradation : <select name="knowledge_upgradation">
		""")
printer()
print("""
	</p>
	<p>
		Tutorial classes were more relevant for the course: <select name="tut_class_relevance">
	""")
printer()
print("""
	</p>
	<p>
		Course contents were appropriate to credit assigned : <select name ="course_content_appropriate">
	""")
printer()
print("""
	</p>
	<p>
		Course is having the scope for team based learning : <select name ="course_team_learning">
	""")
printer()
print("""
	</p>
	""")
print("""</fieldset>""")

print("""
	<fieldset>
	<legend>Course Instructor</legend>
	<p>
		Lesson plan was followed meticulously : <select name ="lesson_plan_followed">
	""")
printer()
print("""
	</p>
	<p>
		Predefined outcomes of the course were achieved : <select name ="course_outcome_achieved">
	""")
printer()
print("""
	</p>
	<p>
		Instructor was well prepared for classes : <select name ="instructor_well_preped">
	""")
printer()
print("""
	</p>
	<p>
		Instructor has clarity in communication of subject matter : <select name ="instructor_comm_clarity">
	""")
printer()
print("""
	</p>
	<p>
		Instructor is accessible and approachable outside the class : <select name ="instructor_accessibility">
	""")
printer()
print("""
	</p>
	<p>
		Instructor maintains regularity and punctuality in class as per Time-table : <select name ="intstructor_reg_punct">
	""")
printer()
print("""
	</p>
	<p>
		Instructor encouraged questions and discussions during class : <select name ="quest_encouraged">
	""")
printer()
print("""
	</p>
	<p>
		Instructor followed fair and un-biased evaluation process : <select name ="fair_ev_proc">
	""")
printer()
print("""
	</p>
	<p>
		Instructor encourages to think creatively and search for additional materials : <select name ="enc_think_creatively">
	""")
printer()
print("""
	</p>
	<p>
		Instructor regularity discusses the performance of test, assignments & examinations : <select name ="disc_performance">
	""")
printer()
print("""	
	</p>
	""")
print("""</fieldset>""")

print("""
	<input type="hidden" name="course_code" value="{}">
	<input type="hidden" name="selected_year" value="{}">
	<p><input type="submit" value="SUBMIT"></p>
	</form>
	</body>
	</html>
	""".format(course_code,selected_year))