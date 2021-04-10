import mysql.connector

db=mysql.connector.connect(host='localhost',port=3306,database='sfs',user='root',password='root')
cur=db.cursor()

username=input("ENTER USER ID : ")
#course_code=input("ENTER COURSE CODE : ")

#print("select sem,sem_year from course_table where id='{}' and course_code='{}'".format(username,course_code))
#cur.execute("select sem,sem_year from course_table where id='{}' and course_code='{}'".format(username,course_code))
cur.execute("select sem,sem_year from course_table where id='{}' and course_code='CS504'".format(username))
myresult = cur.fetchall()
#if len(myresult) == 0:
#	print("EMPTY")
#else:
#	print("RECORDS PRESENT")
#print(type(myresult))
print(myresult[0][1])
#print(type(myresult))
#print(myresult[1][0])
#print(len(myresult))
#for x in myresult:
#	print(x[0])

