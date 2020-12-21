import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='csv')
cursor = conn.cursor()


def insert():
    sql = (
        "INSERT INTO STUDENT(id, name, city)"
        "VALUES (%s, %s, %s)"
    )
    eid = int(input("Enter ID : "))
    ename = input("Enter Name : ")
    ecity = input("Enter City : ")
    data = (eid, ename, ecity)

    try:
        cursor.execute(sql, data)

        conn.commit()

    except Exception as ob:
        print("Error", ob)

    print("Data inserted")
    menu()


def update():
    eid = int(input("Enter ID : "))
    ename = input("Enter Name : ")
    sql = '''UPDATE Student SET name = %s WHERE id = %s '''
    val = (ename, eid)

    try:
        cursor.execute(sql, val)
        conn.commit()
        print("Record Updated")

    except Exception as ob:
        print("Error", ob)

    menu()


def delete():
    eid = int(input("Enter ID : "))
    sql = "DELETE FROM Student WHERE id = '%s'"
    val = (eid,)
    try:
        cursor.execute(sql,val)
        conn.commit()
        print("Record Deleted")

    except Exception as ob:
        print("Error", ob)

    menu()


def display():
    print("Content Of The Table :")
    cursor.execute("SELECT * from Student")
    print(cursor.fetchall())

    menu()


def qu():
    print("Exiting Program!!  Bye !! ")
    conn.close()


def menu():
    print("Choose Options To Perform To A Table : ")
    print("1.Insert")
    print("2.Update")
    print("3.Delete")
    print("4.Display")
    print("5.Exit")
    print("Enter Your Choice :")
    choice = int(input())
    if choice == 1:
        insert()
    elif choice == 2:
        update()
    elif choice == 3:
        delete()
    elif choice == 4:
        display()
    elif choice == 5:
        qu()
    else:
        print("Invalid Choice")
        menu()


menu()
