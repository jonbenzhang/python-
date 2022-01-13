from flask_.json import JSONEncoder
from bson import ObjectId


# 编写自己的json编码器，并继承原有的
class MyJSONEncoder(JSONEncoder):
    # 在jsonify中不能直接序列化该类型的时候，才会调用default方法，并进入分类执行
    def default(self, obj):
        if isinstance(obj, ObjectId):
            # 自定义返回字典
            return str(obj)
        return super().default(obj)

def customize_json(app):
    app.json_encoder = MyJSONEncoder  # 将自定义的json编码器赋给flask原有的
