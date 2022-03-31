import sqlite3
import csv

conn=sqlite3.connect('laptop(new).sqlite')
cur=conn.cursor()

cur.execute('drop table if exists laptop')
cur.execute('''
CREATE TABLE "laptop"(
    "ID" TEXT,
    "BRAND" TEXT,
    "MODEL" TEXT,
    "RAM_GB" TEXT,
    "DISK_GB" TEXT,
    "DISPLAY_SIZE" TEXT,
    "PROCESSOR" TEXT,
    "GRAPHICS" TEXT,
    "PRICE" TEXT,
    "RATINGS" TEXT
)
''')
fname=input('enter the laptop csv file name')
if len(fname)<1 : fname="laptop.csv"

with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
          print(row)
          ID=row[0]
          BRAND=row[1]
          MODEL=row[2]
          RAM_GB=row[3]
          DISK_GB=row[4]
          DISPLAY_SIZE=row[5]
          PROCESSOR=row[6]
          GRAPHICS=row[7]
          PRICE=row[8]
          RATINGS=row[9]
          cur.execute('''INSERT INTO laptop(ID,BRAND,MODEL,RAM_GB,DISK_GB,DISPLAY_SIZE,PROCESSOR,GRAPHICS,PRICE,RATINGS)
             values(?,?,?,?,?,?,?,?,?,?)''',(ID,BRAND,MODEL,RAM_GB,DISK_GB,DISPLAY_SIZE,PROCESSOR,GRAPHICS,PRICE,RATINGS))
          conn.commit()
