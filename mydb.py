# install mysql on your computer
# install mysql
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector
database =  mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
)
#prepare a cursor object
cursorObject = database.cursor()

#creating a database
cursorObject.execute("CREATE DATABASE elderco ")

print("All done")