from celery_app_task import send_email
from datetime import datetime
from datetime import timedelta

# 方式二
# 指定固定时间后执行
ctime = datetime.now()
# 默认用utc时间
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
time_delay = timedelta(seconds=10)
# 当前时间延迟10秒
task_time = utc_ctime + time_delay

# 使用apply_async并设定时间
result = send_email.apply_async(args=["方式2定时"], eta=task_time)
print(result.id)

