import pymysql

user = input("username:")
pwd = input("password:")

conn = pymysql.connect(host="localhost", user='root', password='123456', database="zhang")
cursor = conn.cursor()
# 加上如下参数可使sql的返回数据每一条都为字典类型．
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
"""
不要使用这种方法进行查询，容易被人进行sql注入
sql = "select * from userinfo where username='%s' and password='%s'" %(user,pwd,)
# select * from userinfo where username='uu' or 1=1 -- ' and password='%s'
使用　execute(sql,data)的方式，它集成了避免sql注入的机制
对于下面sql,代码data可以有如下两种形式
sql = "select * from userinfo where username=%s and password=%s"
每一个%s和后面列表中的值一一对应
cursor.execute(sql,[user,pwd])
cursor.execute(sql,(user,pwd))
"""
# cursor.execute也可以不传入参数，只执行sql
# cursor.execute(sql)
# sql = "select * from userinfo where username=%s and password=%s"
# cursor.execute(sql,[user,pwd])
# 按照名字指定
sql = "select * from userinfo where username=%(u)s and password=%(p)s"

cursor.execute(sql, {'u': user, 'p': pwd})
"""
cursor.fetchone():获取sql执行结果的第一个值，再次执行则获取第二个值,如果把获取到的值获取完，再执行则会获取到None
cursor.fetchmany(4):获取sql执行结果的前4个值,如果4大于所有结果的长度，则获取所有的结果
cursor.fetchall():获取sql执行得到的结果的所有值
"""
cursor.execute("select * from userinfo")

result = cursor.fetchmany(2)
print(result)
"""
cursor.scroll(-1, mode='relative') # 相对于当前行进行移动，本行为0，如向上移动一行为-1,向下移动两行为2
cursor.scroll(0,mode='absolute') # 相对与第一行进行移动,0为移动到第一行，因为只能向下移动只能为0或正数
"""
cursor.scroll(0, mode='absolute')
print(cursor.fetchall())
cursor.scroll(-1, mode='relative')
print(cursor.fetchone())
result = cursor.fetchone()
print(result)
cursor.close()
conn.close()
