import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user ="root", database = "hibernatedata")
mycursor = mydb.cursor()

mycursor.execute("INSERT INTO table1(student_name, title) Values('Baba1', 'student3')")
mydb.commit()