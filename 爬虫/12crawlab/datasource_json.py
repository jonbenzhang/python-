import json
import os

# CRAWLAB_DATA_SOURCE 数据源配置
# CRAWLAB_COLLECTION 表名
#
os.environ[
    'CRAWLAB_DATA_SOURCE'] = '{"host": "10.20.1.24", "port": "3307", "username": "sguser", "password": "python1python", "database": "spider", "type": "mysql"}'
os.environ['CRAWLAB_COLLECTION'] = 't_1'
data_source = {
    'host': '10.20.1.24',
    'port': '3307',
    'username': 'sguser',
    'password': 'python1python',
    'database': 'spider',
    'type': 'mysql',
}
data = json.dumps(data_source)
# print(repr(data))

c = '{"CRAWLAB_MONGO_AUTHSOURCE": "admin", "CRAWLAB_DEDUP_FIELD": "", "PYTHONIOENCODING": "utf-8", "HOSTNAME": "7d1ca3dff1e5", "SHLVL": "1", "CRAWLAB_COLLECTION": "undefined", "HOME": "/root", "PYTHONUNBUFFERED": "0", "CRAWLAB_SERVER_MASTER": "Y", "CRAWLAB_REDIS_ADDRESS": "redis", "CRAWLAB_MONGO_HOST": "mongo", "CRAWLAB_DEDUP_METHOD": "", "_": "/usr/local/bin/crawlab-server", "PATH": "/usr/lib/node_modules:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "CRAWLAB_DATA_SOURCE": "\'{\\"host\\": \\"10.20.1.24\\", \\"port\\": \\"3307\\", \\"username\\": \\"sguser\\", \\"password\\": \\"python1python\\", \\"database\\": \\"spider\\", \\"type\\": \\"mysql\\"}\'", "CRAWLAB_MONGO_PORT": "27017", "LANG": "C.UTF-8", "CRAWLAB_IS_DOCKER": "Y", "DEBIAN_FRONTEND": "noninteractive", "CRAWLAB_MONGO_DB": "crawlab_test", "NODE_PATH": "/usr/lib/node_modules", "PWD": "/app/spiders/t", "LC_ALL": "C.UTF-8", "CRAWLAB_TASK_ID": "07e3d666-7304-45d4-8874-71526892dde4", "CRAWLAB_IS_DEDUP": "0", "TZ": "Asia/Shanghai"}'
d = json.loads(c)
for i in d.items():
    print(i)
# import os
#
# print(json.dumps(dict(os.environ)))
