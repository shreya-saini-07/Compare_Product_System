
q1=input("do you want to add filter for rom? (y/n) ")
if q1=='y':
   ram=int(input("Enter the RAM : "))
   mycursor.execute("select * from mobile where (ROM = 'rom') ")

rom=int(input("Enter the ROM : "))

mycursor.execute("select * from mobile where (BRAND = 'brand') ")
mycursor.execute("select * from mobile where (BRAND = 'brand') ")


def filter():

   fil=input("do you want to add filters (y/n) : ")
   if fil=='y':
      print("to add filter for brand select 1")
      print("to add filter for rom select 2")
      print("to add filter for ram select 3")
      print("to add filter for price select 4")
      L=[]
      N=int(input("how many filters do you want to add : "))
      for i in N:
         x=int(input("Enter category : "))
         L.append(x)
      for i in L:
         if i==1:
            brand=input("Enter the brand : ")   
         if i==2:
            rom=input("Enter the ROM : ")
         if i==3:
            ram=input("Enter the RAM : ")
         if i==4:
            min_price=int(input("Enter the minimum price limit : "))
            max_price=int(input("Enter the maximum price limit : "))
            
         
filter()


