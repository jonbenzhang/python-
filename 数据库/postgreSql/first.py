# postgresql://postgres:abc123@172.20.3.29:5432/quke_test

import psycopg2
import psycopg2.extras
conn = psycopg2.connect(database="zhang_test", user="postgres", password="abc123", host="172.20.3.29", port="5432")

print("Opened database successfully")

# postgresql保存的字段，或表名，数据库名，要保存大写必须加双引号,否则就会自动改为小写

def creat_table():
    """
    # 执行sql创建表
    :return:
    """
    cur = conn.cursor()
    cur.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    print("Table created successfully")
    conn.commit()
    conn.close()


# 创建表
# creat_table()


def insert_table():
    """
    插入数据
    :return:
    """
    cur = conn.cursor()
    # 插入数据的引号必须为单引号
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    conn.commit()
    print("Records created successfully")
    conn.close()


# insert_table()


def query_table():
    """
    查询数据
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT id, name, address, salary  from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()


# query_table()


def query_table2():
    """
    直接返回字典类型
    :return:
    """
    # 需要倒入import psycopg2.extras，不然找不到psycopg2.extras.RealDictCursor
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT id, name, address, salary  from COMPANY")
    rows = cur.fetchall()
    for i in rows:
        print(dict(i))
    conn.close()


query_table2()


def update_table():
    """
    更新数据
    :return:
    """
    cur = conn.cursor()
    cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit()
    conn.close()


# update_table()


def del_data():
    """
    删除数据
    :return:
    """
    cur = conn.cursor()
    cur.execute("DELETE from COMPANY where ID=2;")
    conn.commit()
    conn.close()
# del_data()
