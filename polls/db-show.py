import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="enle")

mycursor = mydb.cursor()
# mycursor.execute("create database enle")



mycursor.execute("drop enle")
for db in mycursor:
    print(db)


# mycursor.execute("create table rahman(name varchar(29),age int(2))")

