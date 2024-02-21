import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='mysql',
)

#prepare a cursor object using cursor() method

cursorObject = dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE elderco")

print("all done")