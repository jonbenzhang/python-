from celery_app_task import send_email
from datetime import datetime

# 方式一
# 指定固定的时间执行
v1 = datetime(2020, 7, 20, 13, 37, 00)
print(v1)
v2 = datetime.utcfromtimestamp(v1.timestamp())
print(v2)
result = send_email.apply_async(args=["方式1定时", ], eta=v2)
print(result.id)
