import pymysql

# 增加，删，该
# conn = pymysql.connect(host="localhost", user='root', password='123456', database="zhang")
# cursor = conn.cursor()
# sql = "insert into userinfo(username,password) values('root','123123')"
# 受影响的行数
# r = cursor.execute(sql)
# #  ******
# conn.commit()
# cursor.close()
# conn.close()

# conn = pymysql.connect(host="localhost", user='root', password='123456', database="zhang")
# cursor = conn.cursor()
# # sql = "insert into userinfo(username,password) values(%s,%s)"
# # cursor.execute(sql,(user,pwd,))
#
# sql = "insert into userinfo(username,password) values(%s,%s)"
# # 受影响的行数
# r = cursor.executemany(sql,[('egon','sb'),('laoyao','BS')])
# #  ******
# conn.commit()
# cursor.close()
# conn.close()

