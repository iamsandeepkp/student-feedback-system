import getpass
import sys
import telnetlib

HOST = "agnigarh.tezu.ernet.in"
user = input("Enter your remote account: ")
#print(user)
password = getpass.getpass()
#print(password)
tn = telnetlib.Telnet(HOST,23,10)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write("ls\n")
tn.write("exit\n")

print(tn.read_all())