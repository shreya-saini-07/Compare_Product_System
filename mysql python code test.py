import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shiset16sam@")

mycursor=mycon.cursor()

mycursor.execute("create database if not exists STUDENT_int")
