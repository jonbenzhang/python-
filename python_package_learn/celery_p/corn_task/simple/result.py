"""
结果检查
"""
from celery.result import AsyncResult
from celery_app_task import cel

async_result = AsyncResult(id="eb408063-e2a4-4e38-8bf1-91c04f7ba520", app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
    # result.forget() # 将结果删除
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('任务等待中被执行')
elif async_result.status == 'RETRY':
    print('任务异常后正在重试')
elif async_result.status == 'STARTED':
    print('任务已经开始被执行')
