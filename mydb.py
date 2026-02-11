import mysql.connector

database=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'lakSoft@1970'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE medical")

print("All Done")