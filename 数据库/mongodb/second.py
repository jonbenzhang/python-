from pymongo import MongoClient
import pymongo

uri = "mongodb://%s:%s@%s" % (
    "admin", "123456", "0.0.0.0:27017")
conn = MongoClient(uri)
# conn = MongoClient('0.0.0.0', 27017)
# 获取数据库
db = conn.mydb  # 连接mydb数据库，没有则自动创建
# 获取集合
my_set = db.test_set2  # 使用test_set集合，没有则自动创建
# '''
dic = {"name": "lisi", "age": 18, "li": [1, 2, 3]}
dic2 = {"name": "zhangsan", "age": 18, "li": [1, 2, 3, 4, 5, 6]}

my_set.insert(dic)
my_set.insert(dic2)
# '''
for i in my_set.find({'li': {'$all': [1, 2, 3, 4]}}):
    print(i)
# 查看是否包含全部条件
# 输出：{'_id': ObjectId('58c503b94fc9d44624f7b108'), 'name': 'zhangsan', 'age': 18, 'li': [1, 2, 3, 4, 5, 6]}

# 在name为lisi的li(集合)中添加4
my_set.update({'name': "lisi"}, {'$push': {'li': 4}})
for i in my_set.find({'name': "lisi"}):
    print(i)
# 输出：{'li': [1, 2, 3, 4], '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi'}


# 在name为lisi的li中添加4,5
# my_set.update({'name': "lisi"}, {'$pushAll': {'li': [4, 5]}})
# for i in my_set.find({'name': "lisi"}):
#     print(i)
# # 输出：{'li': [1, 2, 3, 4, 4, 5], 'name': 'lisi', 'age': 18, '_id': ObjectId('58c50d784fc9d44ad8f2e803')}



#pop
#移除最后一个元素(-1为移除第一个)
my_set.update({'name':"lisi"}, {'$pop':{'li':1}})
for i in my_set.find({'name':"lisi"}):
    print(i)
#输出：{'_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi', 'li': [1, 2, 3, 4, 4]}


#pullAll （移除全部符合条件的）
my_set.update({'name':"lisi"}, {'$pullAll':{'li':[1,2,3]}})
for i in my_set.find({'name':"lisi"}):
    print(i)
#输出：{'name': 'lisi', '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'li': [4, 4], 'age': 18}