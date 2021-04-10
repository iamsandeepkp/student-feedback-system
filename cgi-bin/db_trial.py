import mysql.connector
db=mysql.connector.connect(host='localhost',port=3306,database='sfs',user='root',password='root')
cur=db.cursor()

cur.execute("select passw from login where id='hello_csm17'")
myresult1=cur.fetchall()
actual=str(myresult1[0][0])
#print(actual)
#print(type(actual))
splitter=actual.split("'")
myresult1=splitter[1]
print(myresult1)
cur.execute("select md5('HELLO')")
myresult2=cur.fetchall()
#print(type(myresult2))
#print(myresult2[0][0])

#cur.execute("select md5('hello')")
#myresult=cur.fetchall()
#print(len(myresult))
#print(myresult1[0][0])
#print(myresult2[0][0])
if(myresult1==myresult2[0][0]):
	print("PASSWORD MATCHED")
else:
	print("NOT MATCHED")