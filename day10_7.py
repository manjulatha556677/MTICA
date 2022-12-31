import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE cars(ID INT Name TEXT,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',5264)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercrdes',57127)")

cur.execute("INSERT INTO Cars VALUES(3,'Akoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'Volva',2900)")
cur.execute("INSERT INTO Cars VALUES(5,'Bently',35000)")
cur.execute("INSERT INTO Cars VALUES(6,'citrone',21000)")
cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
cur.execuet("INSERT INTO Cars VALUES(8,'Hani',52642)")

con.commit()
print("values in table Cars inserted.")


