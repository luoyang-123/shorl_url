import sqlite3

conn = sqlite3.connect("url.db")

def create_table(shu):
    cursor = conn.cursor()
    max_number='max_number'+'shu'
    table_sql = """
    create table max_number(
      id INTEGER PRIMARY KEY autoincrement NOT NULL,
      useless INTEGER
    )
    """
    print(1)
    cursor.execute(table_sql)
    conn.commit()       # 一定要提交,否则不会执行sql
    cursor.close()



if __name__ == '__main__':
    print(1)
