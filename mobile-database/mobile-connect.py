import sqlite3
import csv

conn=sqlite3.connect('mobile(new).sqlite')
cur=conn.cursor()

cur.execute('drop table if exists mobile')
cur.execute('''
CREATE TABLE "mobile"(
    "ID" TEXT,
    "BRAND" TEXT,
    "MODEL" TEXT,
    "RAM_GB" TEXT,
    "ROM_GB" TEXT,
    "DISPLAY_SIZE" TEXT,
    "CAMERA" TEXT,
    "PRICE" TEXT
    
)
''')
fname=input('enter the mobile csv file name')
if len(fname)<1 : fname="mobile.csv"

with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
          print(row)
          ID=row[0]
          BRAND=row[1]
          MODEL=row[2]
          RAM_GB=row[3]
          ROM_GB=row[4]
          DISPLAY_SIZE=row[5]
          CAMERA=row[6]
          PRICE=row[7]
          cur.execute('''INSERT INTO mobile(ID,BRAND,MODEL,RAM_GB,ROM_GB,DISPLAY_SIZE,CAMERA,PRICE)
             values(?,?,?,?,?,?,?,?)''',(ID,BRAND,MODEL,RAM_GB,ROM_GB,DISPLAY_SIZE,CAMERA,PRICE))
          conn.commit()
