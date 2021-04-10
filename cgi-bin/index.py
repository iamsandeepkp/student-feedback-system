#!C:\Users\greet\AppData\Local\Programs\Python\Python37\python.exe
import cgi

print("""
	<html>
	<head>
		<title>LOGIN</title>
		
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
	<h1>LOGIN HERE</h1>
	</center>
	<form method="post" action="verify_login_2.py">
	
	<fieldset><legend>Enter your monk server credentials:</legend>
	<p>USERNAME : <input type="text" name="username" required><p>
	<p>PASSWORD : <input type="password" name="passw" required></p>
	<p><input type="submit" value="LOGIN" ></p>
	</fieldset>
	
	</form>
	</body>
	</html>
	""")