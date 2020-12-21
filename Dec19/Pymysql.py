import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='csv')

cursor = conn.cursor()
eid = int(input("Enter ID : "))
sql = "DELETE FROM Student WHERE id = '%s'"
val = (eid,)

try:
    cursor.execute(sql, val)
    conn.commit()
    print("Record Updated")

except Exception as ob:
    print("Error", ob)


