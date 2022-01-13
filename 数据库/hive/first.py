# from pyhive import hive
# # conn = hive.Connection(host='ip地址', port=10000, username='用户名', database='default')
# conn = hive.Connection(host='172.20.3.21', port=10000,  database='hive_test1_db')
# cursor = conn.cursor()
# # cursor.execute('select * from testhive limit 10')
# # cursor.execute('show databases')
# cursor.execute('show create table user_info')
# for result in cursor.fetchall():
#     print(result)
from pyhive import hive  # or import hive

# cursor = hive.connect(host='172.20.3.21', port=10000, database='hive_test1_db').cursor()
cursor = hive.connect(host='172.20.3.23', port=10003, database='default').cursor()
cursor.execute('show databases')
# print(cursor.fetchone())#安装
print(cursor.fetchall())
