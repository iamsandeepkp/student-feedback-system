#!/usr/bin/python3
import cgi

print("""
	<html>
	<head>
		<title>LOGIN</title>
	</head>
	<body>
	<center>
	<h1>LOGIN HERE</h1>
	</center>
	<form method="post" action="verify_login_2.py">
	<p>USERNAME : <input type="text" name="username" required><p>
	<p>PASSWORD : <input type="password" name="passw" required></p>
	<p><input type="submit" value="LOGIN" ></p>
	</form>
	</body>
	</html>
	""")