import sqlite3

con = sqlite3.connect(r"D:\DEMO.db")
cur = con.cursor()
sql = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
cur.execute(sql)
data = "1,'Desire',5"
cur.execute('INSERT INTO test VALUES (%s)' % data)
con.commit()
cur.execute("select * from Test")
print(cur.fetchall())