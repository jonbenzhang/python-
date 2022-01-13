#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pymongo
uri = "mongodb://%s:%s@%s" % (
    "admin", "123456", "0.0.0.0:27017")
conn = MongoClient(uri)
# conn = MongoClient('0.0.0.0', 27017)
# 获取数据库
db = conn.mydb  # 连接mydb数据库，没有则自动创建
# 获取集合
my_set = db.test_set  # 使用test_set集合，没有则自动创建



# 集合插入数据
# 插入一条数据,推荐使用insert_one,插入多条使用insert_many
a1 = my_set.insert_one({"name": "zhangsan", "age": 18})
# 插入数据返回的id
print(a1.inserted_id)
a2 = my_set.insert_many([{"name": "zhangsan", "age": 18}, {"name": "wangwu"}])
# 插入数据返回的id
print(a2.inserted_ids)
# my_set.insert([{"name": "zhangsan", "age": 18}, {"name": "wangwu"}])
# 如果包括_id时,且数据库中已经存在此_id,save是更新,insert会报错
# my_set.save({"name": "zhangsan", "age": 18})



# 查询数据,，没有返回None
#查询全部
for i in my_set.find():
    print(i)
#查询name=zhangsan的
for i in my_set.find({"name":"zhangsan"}):
    print(i)
# 查询一个
print(my_set.find_one({"name":"zhangsan"}))



"""
删除数据
"""
# my_set.remove(
#    <query>,    #（可选）删除的文档的条件
#    {
#      justOne: <boolean>,    #（可选）如果设为 true 或 1，则只删除一个文档
#      writeConcern: <document>    #（可选）抛出异常的级别
#    }
# )
#删除name=zhangsan1的全部记录
# 官方推荐使用 delete_one 和 delete_many 代替remove
# my_set.remove({'name': 'zhangsan1'})

#删除name=lisi的某个id的记录/
# id = my_set.find_one({"name":"zhangsan"})["_id"]
# 官方推荐使用 delete_one 和 delete_many 代替remove
# my_set.remove(id)

#删除集合里的所有记录
# my_set.remove()


"""
更新
"""
# update_one or update_many
# 更新所有name为zhangsan的年龄改为25
my_set.update_many({"name":"zhangsan"},{"$set":{"age":"25"}})


"""
比较
"""
#    (>)  大于 - $gt
#    (<)  小于 - $lt
#    (>=)  大于等于 - $gte
#    (<= )  小于等于 - $lte
#例：查询集合中age大于25的所有记录
for i in my_set.find({"age":{"$gt":25}}):
    print(i)
# Double    1
# String    2
# Object    3
# Array    4
# Binary data    5
# Undefined    6    已废弃
# Object id    7
# Boolean    8
# Date    9
# Null    10
# Regular Expression    11
# JavaScript    13
# Symbol    14
# JavaScript (with scope)    15
# 32-bit integer    16
# Timestamp    17
# 64-bit integer    18
# Min key    255    Query with -1.
# Max key    127
#找出name的类型是String的
for i in my_set.find({'name':{'$type':2}}):
    print(i)
# 排序，其中 1 为升序，-1为降序。
for i in my_set.find().sort([("age",1)]):
    print(i)

"""
分页
"""
#limit()方法用来读取指定数量的数据
#skip()方法用来跳过指定数量的数据
#下面表示跳过两条数据后读取6条
for i in my_set.find().skip(2).limit(6):
    print(i)

"""
in
"""
#找出age是20、30、35的数据
for i in my_set.find({"age":{"$in":(20,30,35)}}):
    print(i)

"""
or
"""
#找出age是20或35的记录
for i in my_set.find({"$or":[{"age":20},{"age":35}]}):
    print(i)

"""
all
"""
'''
dic = {"name":"lisi","age":18,"li":[1,2,3]}
dic2 = {"name":"zhangsan","age":18,"li":[1,2,3,4,5,6]}

my_set.insert(dic)
my_set.insert(dic2)'''
for i in my_set.find({'li':{'$all':[1,2,3,4]}}):
    print(i)
#查看是否包含全部条件
#输出：{'_id': ObjectId('58c503b94fc9d44624f7b108'), 'name': 'zhangsan', 'age': 18, 'li': [1, 2, 3, 4, 5, 6]}