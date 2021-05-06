import sqlite3

conn = sqlite3.connect("url.db")

def create_table():
    cursor = conn.cursor()
    table_sql = """
    create table url(
      id INTEGER PRIMARY KEY autoincrement NOT NULL ,
      short_url text NOT NULL,
      long_url text NOT NULL
    )
    """
    cursor.execute(table_sql)
    conn.commit()       # 一定要提交,否则不会执行sql

    table_sql = """
    create table url_index(
      id INTEGER PRIMARY KEY autoincrement NOT NULL,
      useless INTEGER
    )
    """
    cursor.execute(table_sql)
    conn.commit()       # 一定要提交,否则不会执行sql

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






def add_url(long_url, short_url):
    """
    长短地址映射关系
    :param long_url:
    :param short_url:
    :return:
    """
    cursor = conn.cursor()
    sql = "insert into url(short_url, long_url)values('{short_url}', '{long_url}')"
    sql = sql.format(short_url=short_url, long_url=long_url)
    cursor.execute(sql)
    conn.commit()
    cursor.close()


def get_long_url(short_url):
    """
    根据短地址查询长地址
    :param short_url:
    :return:
    """
    cursor = conn.cursor()
    sql = "select * from url where short_url='{short_url}'".format(short_url=short_url)
    cursor.execute(sql)
    rows = cursor.fetchall()  # 获取全部数据
    if len(rows) == 0:
        return None
    row = rows[0]
    info = tuple(row)
    return info[2]


def get_max_index():
    """
    获取最新拨号
    :return:
    """
    cursor = conn.cursor()
    sql = "insert into url_index(useless)values(1)"
    result = cursor.execute(sql)
    index = result.lastrowid
    conn.commit()
    cursor.close()
    return index



def get_buohao_index():
    """
    获取最新拨号
    :return:
    """
    cursor = conn.cursor()
    sql = "insert into max_number(useless)values(1)"
    result = cursor.execute(sql)
    index = result.lastrowid
    conn.commit()


    cursor.close()
    print(1)
    return index*100



if __name__ == '__main__':
    #create_table()
    #add_url('http://www.baidu.com', 'oer2')
    # print(get_long_url('oer2'))
    print(get_buohao_index())
