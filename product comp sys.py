import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='shiset16sam@',database='product')

mycursor=mycon.cursor()

mycursor.execute("select * from mobile")
myresult = mycursor.fetchall()
print(myresult)

   
print("Which of the following Category do want to select ?")
print("Select 1 for MOBILE")
print("Select 2 for TABLET")
print("Select 3 for LAPTOP")
print("Select 4 for TV")
print("Select 5 for CAMERA")
N = int(input("Enter the Category Code to select :"))
if N == 1:
   mycursor.execute("select * from MOBILE")
   for i in mycursor():
      print(i)
   print()
elif N == 2:
   mycursor.execute("select * from TABLET")
   print()
elif N == 3:
   mycursor.execute("select * from LAPTOP")
   print()
elif N == 4:
   mycursor.execute("select * from TV")
   print()
elif N == 5:
   mycursor.execute("select * from CAMERA")
   print()
else:
   print()

