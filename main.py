import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shiset16sam@",
    database="product1")

mycursor=mycon.cursor()


# DISPLAY WHOLE TABLE
def mobile():
   mycursor.execute("select * from mobile")
   print ("\nPRODUCT : MOBILE\n\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10}".format("ID","BRAND","MODEL","RAM_GB","ROM_GB","DISPLAY_SIZE","CAMERA","PRICE"))
   print("-"*137)
   for v in mycursor: 
      ID,BRAND,MODEL,RAM_GB,ROM_GB,DISPLAY_SIZE,CAMERA,PRICE=v
      print ("{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10}".format(ID,BRAND,MODEL,RAM_GB,ROM_GB,DISPLAY_SIZE,CAMERA,PRICE))
   
def tablet():
   mycursor.execute("select * from tablet")
   print ("\nPRODUCT : TABLET\n\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID","BRAND","MODEL","PRICE","SCREEN_SIZE","ROM","RESOLUTION","OS","PROCESSOR"))
   print("-"*155)
   for v in mycursor: 
      ID,BRAND,MODEL,PRICE,SCREEN_SIZE,ROM,RESOLUTION,OS,PROCESSOR= v
      print ("{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format(ID,BRAND,MODEL,PRICE,SCREEN_SIZE,ROM,RESOLUTION,OS,PROCESSOR))

def laptop():
   mycursor.execute("select * from laptop")
   print ("\nPRODUCT : LAPTOP\n\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID","BRAND","MODEL","RAM_GB","DISK_GB","DISPLAY_SIZE","PROCESSOR","GRAPHICS","PRICE","RATINGS"))
   for v in mycursor:
      ID,BRAND,MODEL,RAM_GB,DISK_GB,DISPLAY_SIZE,PROCESSOR,GRAPHICS,PRICE,RATINGS= v
      print ("{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format(ID,BRAND,MODEL,RAM_GB,DISK_GB,DISPLAY_SIZE,PROCESSOR,GRAPHICS,PRICE,RATINGS))

def camera():
   mycursor.execute("select * from camera")
   print ("\nPRODUCT : CAMERA\n\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("ID","BRAND","PRICE","MODEL","TYPE","DIMENSIONS","EFFECTIVE_PIXELS","MODEL_NUMBER","DISPLAY_RESOLUTION","DIGITAL_ZOOM"))
   for v in mycursor:
      ID,BRAND,PRICE,MODEL,TYPE,DIMENSIONS,EFFECTIVE_PIXELS,MODEL_NUMBER,DISPLAY_RESOLUTION,DIGITAL_ZOOM= v
      print ("{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format(ID,BRAND,PRICE,MODEL,TYPE,DIMENSIONS,EFFECTIVE_PIXELS,MODEL_NUMBER,DISPLAY_RESOLUTION,DIGITAL_ZOOM))

def television():
   mycursor.execute("select * from television")
   print ("\nPRODUCT : TELEVISION\n\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID","BRAND","MODEL","RESOLUTION","DISPLAY_SIZE","PRICE","WEIGHT_kg","OS"))
   for v in mycursor:
      ID,BRAND,MODEL,RESOLUTION,DISPLAY_SIZE,PRICE,WEIGHT_kg,OS= v
      print ("{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format(ID,BRAND,MODEL,RESOLUTION,DISPLAY_SIZE,PRICE,WEIGHT_kg,OS))


# DISPLAY WITH PROPER FORMATING

def mob_result_disp(data1):
   
   ID,BRAND,MODEL,RAM_GB,ROM_GB,DISPLAY_SIZE,CAMERA,PRICE=data1
   print ("{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10}".format(ID,BRAND,MODEL,RAM_GB,ROM_GB,DISPLAY_SIZE,CAMERA,PRICE))


def tab_result_disp(data1):
   
   ID,BRAND,MODEL,PRICE,SCREEN_SIZE,ROM,RESOLUTION,OS,PROCESSOR=data1
   print ("{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format(ID,BRAND,MODEL,PRICE,SCREEN_SIZE,ROM,RESOLUTION,OS,PROCESSOR))

def lap_result_disp(data1):

   ID,BRAND,MODEL,RAM_GB,DISK_GB,DISPLAY_SIZE,PROCESSOR,GRAPHICS,PRICE,RATINGS=data1
   print ("{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format(ID,BRAND,MODEL,RAM_GB,DISK_GB,DISPLAY_SIZE,PROCESSOR,GRAPHICS,PRICE,RATINGS))

def cam_result_disp(data1):
   ID,BRAND,PRICE,MODEL,TYPE,DIMENSIONS,EFFECTIVE_PIXELS,MODEL_NUMBER,DISPLAY_RESOLUTION,DIGITAL_ZOOM=data1
   print ("{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format(ID,BRAND,PRICE,MODEL,TYPE,DIMENSIONS,EFFECTIVE_PIXELS,MODEL_NUMBER,DISPLAY_RESOLUTION,DIGITAL_ZOOM))
   

def tel_result_disp(data1):
   ID,BRAND,MODEL,RESOLUTION,DISPLAY_SIZE,PRICE,WEIGHT_kg,OS=data1
   print ("{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format(ID,BRAND,MODEL,RESOLUTION,DISPLAY_SIZE,PRICE,WEIGHT_kg,OS))



#---------------MOBILE-----------------------------------
def filter_mob():

   print("\nTo add filter for BRAND, Select 1")
   print("To add filter for ROM, Select 2")
   print("To add filter for RAM, Select 3")
   print("To add filter for PRICE, Select 4")
   L=[]
   N=int(input("\nHow Many filters do you want to add (1,2,3,4): "))
   for i in range(N):
      x=int(input("Enter Filter to Add : "))
      L.append(x)
         
   for i in L:
         
      if i==1:
         brand=input("\nEnter BRAND Name : ")
         query="select * from mobile where BRAND='%s'" %(brand.lower())
         mycursor.execute(query)
         data=mycursor.fetchall()
         print ("\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10} ".format("ID","BRAND","MODEL","RAM_GB","ROM_GB","DISPLAY_SIZE","CAMERA","PRICE"))
         for row in data:
            mob_result_disp(row)
               
      elif i==2:
         rom=input("\nEnter ROM Size : ")
         query="select * from mobile where ROM_GB='%s'" %(rom.lower())
         mycursor.execute(query)
         data=mycursor.fetchall()
         print ("\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10} ".format("ID","BRAND","MODEL","RAM_GB","ROM_GB","DISPLAY_SIZE","CAMERA","PRICE"))
         for row in data:
            mob_result_disp(row)
               
      elif i==3:
         ram=input("\nEnter RAM Size : ")
         query="select * from mobile where RAM_GB='%s'" %(ram.lower())
         mycursor.execute(query)
         data=mycursor.fetchall()
         print ("\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10} ".format("ID","BRAND","MODEL","RAM_GB","ROM_GB","DISPLAY_SIZE","CAMERA","PRICE"))
         for row in data:
            mob_result_disp(row)
               
      elif i==4:
         min_price=int(input("\nEnter Minimum PRICE : "))
         max_price=int(input("Enter Maximum PRICE : "))
         query="select * from mobile where PRICE between '%s' and '%s'" %(min_price, max_price)
         mycursor.execute(query)
         data=mycursor.fetchall()
         print(data)
         if len(data)==0:
            print("No match found")
         else:
            print ("\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10} ".format("ID","BRAND","MODEL","RAM_GB","ROM_GB","DISPLAY_SIZE","CAMERA","PRICE"))
            for row in data:
               mob_result_disp(row)



#---------------TABLET-----------------------------------

def filter_tab():


   print("\nTo add filter for BRAND select 1")
   print("To add filter for SCREEN Size select 2")
   print("To add filter for STORAGE Size select 3")
   print("To add filter for PRICE select 4")
   L=[]
   N=int(input("\nHow many filters do you want to add : "))
   for i in range(N):
         
      x=int(input("Enter Filter to Add : "))
      L.append(x)
         
   for i in L:
         
      if i==1:
         brand=input("\nEnter Brand : ")
         query="select * from tablet where BRAND='%s'" %(brand.lower())
         mycursor.execute(query)
         data=mycursor.fetchall()
         print ("\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID","BRAND","MODEL","PRICE","SCREEN_SIZE","ROM","RESOLUTION","OS","PROCESSOR"))
         for row in data:
            tab_result_disp(row)
               
      elif i==2:
         scr_size=input("\nEnter Screen Size : ")
         query="select * from tablet where SCREEN_SIZE='%s'" %(scr_size)
         mycursor.execute(query)
         data=mycursor.fetchall()
         print ("\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID","BRAND","MODEL","PRICE","SCREEN_SIZE","ROM","RESOLUTION","OS","PROCESSOR"))
         for row in data:
            tab_result_disp(row)
               
      elif i==3:
         storage=input("\nEnter Storage Size : ")
         query="select * from tablet where ROM='%s'" %(storage)
         mycursor.execute(query)
         data=mycursor.fetchall()
         print ("\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID","BRAND","MODEL","PRICE","SCREEN_SIZE","ROM","RESOLUTION","OS","PROCESSOR"))
         for row in data:
            tab_result_disp(row)
               
      elif i==4:
         min_price=int(input("\nEnter minimum price limit : "))
         max_price=int(input("Enter maximum price limit : "))
         query="select * from tablet where PRICE between '%s' and '%s'" %(min_price,max_price)
         mycursor.execute(query)
         data=mycursor.fetchall()
         print ("\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID","BRAND","MODEL","PRICE","SCREEN_SIZE","ROM","RESOLUTION","OS","PROCESSOR"))
         for row in data:
            tab_result_disp(row)



#---------------LAPTOP-----------------------------------

               

def filter_lap():

      print("\nTo add filter for BRAND select 1")
      print("To add filter for SCREEN Size select 2")
      print("To add filter for STORGAE Size select 3")
      print("To add filter for PRICE select 4")
      L=[]
      N=int(input("\nHow many filters do you want to add : "))
      for i in range(N):
         
         x=int(input("Enter Filter to Add : "))
         L.append(x)
         
      for i in L:
         
         if i==1:
            brand=input("\nEnter Brand : ")
            query="select * from laptop where brand='%s'" %(brand.lower())
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID","BRAND","MODEL","RAM_GB","DISK_GB","DISPLAY_SIZE","PROCESSOR","GRAPHICS","PRICE","RATINGS"))
            for row in data:
               lap_result_disp(row)
               
         elif i==2:
            scr_size=input("\nEnter Screen Size : ")
            query="select * from laptop where DISPLAY_SIZE='%s'" %(scr_size)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID","BRAND","MODEL","RAM_GB","DISK_GB","DISPLAY_SIZE","PROCESSOR","GRAPHICS","PRICE","RATINGS"))
            for row in data:
               lap_result_disp(row)
               
         elif i==3:
            storage=input("\nEnter Storage Size : ")
            query="select * from laptop where DISC_GB='%s'" %(storage)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID","BRAND","MODEL","RAM_GB","DISK_GB","DISPLAY_SIZE","PROCESSOR","GRAPHICS","PRICE","RATINGS"))
            for row in data:
               lap_result_disp(row)
               
         elif i==4:
            min_price=int(input("\nEnter minimum price limit : "))
            max_price=int(input("Enter maximum price limit : "))
            query="select * from laptop where price between '%s' and '%s'" %(min_price,max_price)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID","BRAND","MODEL","RAM_GB","DISK_GB","DISPLAY_SIZE","PROCESSOR","GRAPHICS","PRICE","RATINGS"))
            for row in data:
               lap_result_disp(row)


#---------------CAMERA-----------------------------------
               

def filter_cam():

      print("\nTo add filter for BRAND select 1")
      print("To add filter for PIXEL select 2")
      print("To add filter for ZOOM select 3")
      print("To add filter for PRICE select 4")
      L=[]
      N=int(input("\nHow many filters do you want to add : "))
      for i in range(N):
         
         x=int(input("Enter Filter to Add : "))
         L.append(x)
         
      for i in L:
         
         if i==1:
            brand=input("\nEnter Brand : ")
            query="select * from camera where brand='%s'" %(brand.lower())
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("ID","BRAND","PRICE","MODEL","TYPE","DIMENSIONS","EFFECTIVE_PIXELS","MODEL_NUMBER","DISPLAY_RESOLUTION","DIGITAL_ZOOM"))
            for row in data:
               cam_result_disp(row)
               
         elif i==2:
            pixel=input("\nEnter Pixel : ")
            query="select * from camera where effective_pixels='%s'" %(pixel)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("ID","BRAND","PRICE","MODEL","TYPE","DIMENSIONS","EFFECTIVE_PIXELS","MODEL_NUMBER","DISPLAY_RESOLUTION","DIGITAL_ZOOM"))
            for row in data:
               cam_result_disp(row)

         elif i==3:
            zoom=input("\nEnter Zoom : ")
            query="select * from camera where DIGITAL_ZOOM='%s'" %(zoom.lower())
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("ID","BRAND","PRICE","MODEL","TYPE","DIMENSIONS","EFFECTIVE_PIXELS","MODEL_NUMBER","DISPLAY_RESOLUTION","DIGITAL_ZOOM"))
            for row in data:
               cam_result_disp(row)
               
         elif i==4:
            min_price=int(input("\nEnter minimum price limit : "))
            max_price=int(input("Enter maximum price limit : "))
            query="select * from camera where price between '%s' and '%s'" %(min_price,max_price)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("BRAND","PRICE","MODEL_NAME","TYPE","DIMENSIONS","PIXELS","MODEL_NO","RESOLUTION","DIGITAL_ZOOM"))
            for row in data:
               cam_result_disp(row)



#---------------TELEVISION-----------------------------------



               
def filter_tel():

      print("\nTo add filter for BRAND select 1")
      print("To add filter for DISPLAY Size select 2")
      print("To add filter for RESOLUTION select 3")
      print("To add filter for PRICE select 4")
      L=[]
      N=int(input("how many filters do you want to add : "))
      for i in range(N):
         
         x=int(input("Enter Filter to Add : "))
         L.append(x)
         
      for i in L:
         
         if i==1:
            brand=input("\nEnter Brand : ")
            query="select * from television where brand='%s'" %(brand.lower())
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID","BRAND","MODEL","RESOLUTION","DISPLAY_SIZE","PRICE","WEIGHT_kg","OS"))
            for row in data:
               tel_result_disp(row)
               
         elif i==2:
            scr_size=input("\nEnter Screen Size : ")
            query="select * from television where DISPLAY_SIZE='%s'" %(scr_size)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID","BRAND","MODEL","RESOLUTION","DISPLAY_SIZE","PRICE","WEIGHT_kg","OS"))
            for row in data:
               tel_result_disp(row)

         elif i==3:
            resolution=input("\nEnter Resolution : ")
            query="select * from television where resolution='%s'" %(resolution.lower())
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID","BRAND","MODEL","RESOLUTION","DISPLAY_SIZE","PRICE","WEIGHT_kg","OS"))
            for row in data:
               tel_result_disp(row)
               
         elif i==4:
            min_price=int(input("\nEnter minimum price limit : "))
            max_price=int(input("Enter maximum price limit : "))
            query="select * from television where price between '%s' and '%s'" %(min_price,max_price)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print ("\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID","BRAND","MODEL","RESOLUTION","DISPLAY_SIZE","PRICE","WEIGHT_kg","OS"))
            for row in data:
               tel_result_disp(row)

      # television indexing properly

# COMPARING DEVICES

def mob_compare():
   ncomp_mob=int(input("\nEnter how many mobiles do you want to compare (max 3) : "))
   L=[]
   for i in range(ncomp_mob): 
      mob_ID=int(input("\nEnter ID to compare: "))
      L.append(mob_ID)
   print ("\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10} ".format("ID","BRAND","MODEL","RAM_GB","ROM_GB","DISPLAY_SIZE","CAMERA","PRICE"))
   for i in L:
      query="select * from mobile where ID='%s'" %(i)
      mycursor.execute(query)
      data=mycursor.fetchall()   
      for row in data:
         mob_result_disp(row)

def tab_compare():
   ncomp_tab=int(input("\nEnter how many tablets do you want to compare (max 3) : "))
   L=[]
   for i in range(ncomp_tab): 
      tab_ID=int(input("\nEnter ID to compare: "))
      L.append(tab_ID)
   print ("\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID","BRAND","MODEL","PRICE","SCREEN_SIZE","ROM","RESOLUTION","OS","PROCESSOR"))
   for i in L:
      query="select * from tablet where ID='%s'" %(i)
      mycursor.execute(query)
      data=mycursor.fetchall()   
      for row in data:
         tab_result_disp(row)

def lap_compare():
   ncomp_lap=int(input("\nEnter how many laptops do you want to compare (max 3) : "))
   L=[]
   for i in range(ncomp_lap): 
      lap_ID=int(input("\nEnter ID to compare: "))
      L.append(lap_ID)
   print ("\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID","BRAND","MODEL","RAM_GB","DISK_GB","DISPLAY_SIZE","PROCESSOR","GRAPHICS","PRICE","RATINGS"))
   for i in L:
      query="select * from laptop where ID='%s'" %(i)
      mycursor.execute(query)
      data=mycursor.fetchall()   
      for row in data:
         lap_result_disp(row)

def cam_compare():
   ncomp_cam=int(input("\nEnter how many camera do you want to compare (max 3) : "))
   L=[]
   for i in range(ncomp_cam): 
      cam_ID=int(input("\nEnter ID to compare: "))
      L.append(cam_ID)
   print ("\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("ID","BRAND","PRICE","MODEL","TYPE","DIMENSIONS","EFFECTIVE_PIXELS","MODEL_NUMBER","DISPLAY_RESOLUTION","DIGITAL_ZOOM"))
   for i in L:
      query="select * from camera where ID='%s'" %(i)
      mycursor.execute(query)
      data=mycursor.fetchall()   
      for row in data:
         cam_result_disp(row)

def tel_compare():
   ncomp_tel=int(input("\nEnter how many televisions do you want to compare (max 3) : "))
   L=[]
   for i in range(ncomp_tel): 
      tel_ID=int(input("\nEnter ID to compare: "))
      L.append(tel_ID)
   print ("\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID","BRAND","MODEL","RESOLUTION","DISPLAY_SIZE","PRICE","WEIGHT_kg","OS"))
   for i in L:
      query="select * from television where ID='%s'" %(i)
      mycursor.execute(query)
      data=mycursor.fetchall()   
      for row in data:
         tel_result_disp(row)

         
# SORTING TABLES W.R.T. PRICE

def mob_sort():
   x=input("Do you want in Ascending(1) or Descending(2) order ? : ")
   if x=="2":
      query="select * from mobile order by price DESC"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10} ".format("ID", "BRAND", "MODEL", "RAM_GB", "ROM_GB","DISPLAY_SIZE", "CAMERA", "PRICE"))
      for row in data:
         mob_result_disp(row)

   elif x=="1":
      query = "select * from mobile order by price"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<10} {:<25} {:<8} {:<8} {:<15} {:<48} {:<10} ".format("ID", "BRAND", "MODEL", "RAM_GB", "ROM_GB","DISPLAY_SIZE", "CAMERA", "PRICE"))
      for row in data:
         mob_result_disp(row)

   else :
      print("Incorrect Option")
      mob_sort()

def tab_sort():
   x = input("Do you want in Ascending(1) or Descending(2) order ? : ")
   if x == "2":
      query = "select * from tablet order by price DESC"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID","BRAND","MODEL","PRICE","SCREEN_SIZE","ROM","RESOLUTION","OS","PROCESSOR"))
      for row in data:
         tab_result_disp(row)

   elif x == "1":
      query = "select * from tablet order by price"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<12} {:<55} {:<10} {:<13} {:<4} {:<18} {:<15} {:<18}".format("ID", "BRAND", "MODEL", "PRICE","SCREEN_SIZE", "ROM", "RESOLUTION","OS", "PROCESSOR"))
      for row in data:
         tab_result_disp(row)

   else :
      print("Incorrect Option")
      tab_sort()


def lap_sort():
   x = input("Do you want in Ascending(1) or Descending(2) order ? : ")
   if x == "2":
      query = "select * from laptop order by price DESC"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID", "BRAND", "MODEL","RAM_GB", "DISK_GB","DISPLAY_SIZE", "PROCESSOR","GRAPHICS", "PRICE","RATINGS"))
      for row in data:
         lap_result_disp(row)

   elif x == "1":
      query = "select * from laptop order by price"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<10} {:<38} {:<7} {:<25} {:<15} {:<25} {:<35} {:<10} {:<10}".format("ID", "BRAND", "MODEL","RAM_GB", "DISK_GB","DISPLAY_SIZE", "PROCESSOR","GRAPHICS", "PRICE","RATINGS"))
      for row in data:
         lap_result_disp(row)

   else :
      print("Incorrect Option")
      lap_sort()

def cam_sort():
   x = input("Do you want in Ascending(1) or Descending(2) order ? : ")
   if x == "2":
      query = "select * from camera order by price DESC"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("ID", "BRAND", "PRICE","MODEL", "TYPE","DIMENSIONS","EFFECTIVE_PIXELS","MODEL_NUMBER","DISPLAY_RESOLUTION","DIGITAL_ZOOM"))
      for row in data:
         cam_result_disp(row)

   elif x == "1":
      query = "select * from camera order by price"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<12} {:<10} {:<20} {:<15} {:<25} {:<20} {:<15} {:<25} {:<15}".format("ID", "BRAND", "PRICE","MODEL", "TYPE","DIMENSIONS","EFFECTIVE_PIXELS","MODEL_NUMBER","DISPLAY_RESOLUTION","DIGITAL_ZOOM"))
      for row in data:
         cam_result_disp(row)

   else :
      print("Incorrect Option")
      cam_sort()



def tel_sort():
   x = input("Do you want in Ascending(1) or Descending(2) order ? : ")
   if x == "2":
      query = "select * from television order by price DESC"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID", "BRAND", "MODEL", "RESOLUTION","DISPLAY_SIZE", "PRICE", "WEIGHT_kg","OS"))
      for row in data:
         tel_result_disp(row)


   elif x == "1":
      query = "select * from television order by price"
      mycursor.execute(query)
      data = mycursor.fetchall()
      print("\n{:<5} {:<20} {:<60} {:<12} {:<15} {:<10} {:<15} {:<12}".format("ID", "BRAND", "MODEL", "RESOLUTION","DISPLAY_SIZE", "PRICE", "WEIGHT_kg","OS"))
      for row in data:
         tel_result_disp(row)


   else :
      print("Incorrect Option")
      tel_sort()
   
#---------------------------------------------------------------------MAIN CODE-------------------------------------------------------------------------------------

#-----------raw---------------------------
def function_menu_mob():
   print("\nselect 1 for SORT (by price) ")
   print("select 2 for FILTER ")
   print("select 3 for COMPARE ")
   print("select 4 for BACK TO MAIN MENU\n")
   opt=int(input("Enter the option : "))
   
   if opt==1:
      mob_sort()

   elif opt==2:
      filter_mob()

   elif opt==3:
      mob_compare()

   elif opt==4:
      main_menu()

def function_menu_tab():
   print("\nselect 1 for SORT (by price) ")
   print("select 2 for FILTER ")
   print("select 3 for COMPARE ")
   print("select 4 for BACK TO MAIN MENU\n ")
   opt=int(input("Enter the option : "))
   
   if opt==1:
      tab_sort()

   elif opt==2:
      filter_tab()

   elif opt==3:
      tab_compare()
   
   elif opt==4:
      main_menu()

def function_menu_lap():
   print("\nselect 1 for SORT (by price) ")
   print("select 2 for FILTER ")
   print("select 3 for COMPARE ")
   print("select 4 for BACK TO MAIN MENU\n ")
   opt=int(input("Enter the option : "))
   
   if opt==1:
      lap_sort()

   elif opt==2:
      filter_lap()

   elif opt==3:
      lap_compare()

   elif opt==4:
      main_menu()
      
def function_menu_cam():
   print("\nselect 1 for SORT (by price) ")
   print("select 2 for FILTER ")
   print("select 3 for COMPARE ")
   print("select 4 for BACK TO MAIN MENU\n ")
   opt=int(input("Enter the option : "))
   
   if opt==1:
      cam_sort()

   elif opt==2:
      filter_cam()

   elif opt==3:
      cam_compare()

   elif opt==4:
      main_menu()

def function_menu_tel():
   print("\nselect 1 for SORT (by price) ")
   print("select 2 for FILTER ")
   print("select 3 for COMPARE ")
   print("select 4 for BACK TO MAIN MENU\n ")
   opt=int(input("Enter the option : "))
   
   if opt==1:
      tel_sort()

   elif opt==2:
      filter_tel()

   elif opt==3:
      tel_compare()

   elif opt==4:
      main_menu()

#---------------------

      
#import os 
def main_menu():   
      #ans='y'
   #while ans=='y':      
      print("\n************  MOBILE (1)    *************")
      print("************  TABLET (2)    *************")
      print("************  LAPTOP (3)    *************")
      print("************  CAMERA (4)    *************")
      print("************  TELEVISION(5) *************")
      print("************  EXIT (0)      *************\n")

      cat=int(input(("Select Option : ")))

      if cat==0:
         {
         }
      
      elif cat==1:
         mobile()
         ans=input("\nDo you wish to continue? (y/n) : ")
         while ans.lower()=='y':
            function_menu_mob()
            ans=input("\nDo you wish to continue? (y/n) : ")            
             
      elif cat==2:
         tablet()
         ans=input("\nDo you wish to continue? (y/n) : ")
         while ans.lower()=='y':
            function_menu_tab()
            ans=input("\nDo you wish to continue? (y/n) : ")
         
      elif cat==3:
         laptop()
         ans=input("\nDo you wish to continue? (y/n) : ")
         while ans.lower()=='y':
            function_menu_lap()
            ans=input("\nDo you wish to continue? (y/n) : ")
         
      elif cat==4:
         camera()
         ans=input("\nDo you wish to continue? (y/n) : ")
         while ans.lower()=='y':
            function_menu_cam()
            ans=input("\nDo you wish to continue? (y/n) : ")
         
      elif cat==5:
         television()
         ans=input("\nDo you wish to continue? (y/n) : ")
         while ans.lower()=='y':
            function_menu_tel()
            ans=input("\nDo you wish to continue? (y/n) : ")
         
      else:
         print("Wrong input")
         main_menu()
         #cat=int(input(("Select Option : ")))
         

      



print("\n\n*************************************************************************") 
print("***************** WELCOME TO COMPARE PRODUCT SYSTEM *********************")   
print("*************************************************************************")

main_menu()

print("\n*****************************************************************************") 
print("*************** THANK YOU FOR VISITING COMPARE PRODUCT SYSTEM ***************")   
print("*****************************************************************************")
