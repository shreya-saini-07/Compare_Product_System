import sqlite3
import csv

conn=sqlite3.connect('camera(new).sqlite')
cur=conn.cursor()

cur.execute('drop table if exists camera')
cur.execute('''
CREATE TABLE "camera"(
    "ID" TEXT,
    "BRAND" TEXT,
    "PRICE" TEXT,
    "MODEL" TEXT,
    "TYPE" TEXT,
    "DIMENSIONS" TEXT,
    "EFFECTIVE_PIXELS" TEXT,
    "MODEL_NUMBER" TEXT,
    "DISPLAY_RESOLUTION" TEXT,
    "DIGITAL_ZOOM" TEXT
)
''')
fname=input('enter the camera csv file name')
if len(fname)<1 : fname="camera.csv"

with open(fname) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
          print(row)
          ID=row[0]
          BRAND=row[1]
          PRICE=row[2]
          MODEL=row[3]
          TYPE=row[4]
          DIMENSIONS=row[5]
          EFFECTIVE_PIXELS=row[6]
          MODEL_NUMBER=row[7]
          DISPLAY_RESOLUTION=row[8]
          DIGITAL_ZOOM=row[9]
          cur.execute('''INSERT INTO camera(ID,BRAND,PRICE,MODEL,TYPE,DIMENSIONS,EFFECTIVE_PIXELS,MODEL_NUMBER,DISPLAY_RESOLUTION,DIGITAL_ZOOM)
             values(?,?,?,?,?,?,?,?,?,?)''',(ID,BRAND,PRICE,MODEL,TYPE,DIMENSIONS,EFFECTIVE_PIXELS,MODEL_NUMBER,DISPLAY_RESOLUTION,DIGITAL_ZOOM))
          conn.commit()
