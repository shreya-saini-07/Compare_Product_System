import sqlite3
import csv

conn=sqlite3.connect('television(new).sqlite')
cur=conn.cursor()

cur.execute('drop table if exists television')
cur.execute('''
CREATE TABLE "television"(
    "ID" TEXT,
    "BRAND" TEXT,
    "MODEL" TEXT,
    "RESOLUTION" TEXT,
    "DISPLAY_SIZE" TEXT,
    "PRICE" TEXT,
    "WEIGHT_kg" TEXT,
    "OS" TEXT
)
''')
fname=input('enter the mobile csv file name')
if len(fname)<1 : fname="television.csv"

with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
          print(row)
          ID=row[0]
          BRAND=row[1]
          MODEL=row[2]
          RESOLUTION=row[3]
          DISPLAY_SIZE=row[4]
          PRICE=row[5]
          WEIGHT_kg=row[6]
          OS=row[7]
          cur.execute('''INSERT INTO television(ID,BRAND,MODEL,RESOLUTION,DISPLAY_SIZE,PRICE,WEIGHT_kg,OS)
             values(?,?,?,?,?,?,?,?)''',(ID,BRAND,MODEL,RESOLUTION,DISPLAY_SIZE,PRICE,WEIGHT_kg,OS))
          conn.commit()
