import sqlite3
import csv

conn=sqlite3.connect('tablet(new).sqlite')
cur=conn.cursor()

cur.execute('drop table if exists tablet')
cur.execute('''
CREATE TABLE "tablet"(
    "ID" TEXT,
    "BRAND" TEXT,
    "MODEL" TEXT,
    "PRICE" TEXT,
    "SCREEN_SIZE" TEXT,
    "ROM" TEXT,
    "RESOLUTION" TEXT,
    "OS" TEXT,
    "PROCESSOR" TEXT
)
''')
fname=input('enter the tablet csv file name')
if len(fname)<1 : fname="tablet.csv"

with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
          print(row)
          ID=row[0]
          BRAND=row[1]
          MODEL=row[2]
          PRICE=row[3]
          SCREEN_SIZE=row[4]
          ROM=row[5]
          RESOLUTION=row[6]
          OS=row[7]
          PROCESSOR=row[8]
          cur.execute('''INSERT INTO tablet(ID,BRAND,MODEL,PRICE,SCREEN_SIZE,ROM,RESOLUTION,OS,PROCESSOR)
             values(?,?,?,?,?,?,?,?,?)''',(ID,BRAND,MODEL,PRICE,SCREEN_SIZE,ROM,RESOLUTION,OS,PROCESSOR))
          conn.commit()
