import mysql.connector

try:
    con = mysql.connector.connect(host='localhost', database='csv', user='root', password='root')
    cursor = con.cursor()
    cursor.execute("select * from student")
except:
    print("Error Occurred")
