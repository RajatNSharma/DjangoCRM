import mysql.connector
import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='...',
    passwd='.......',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Name")

print("All Done!")
