import asyncio
# from asyncio import sleep
from time import sleep


async def func():
    print(1)
    await asyncio.sleep(2)
    print(10)
    return "返回值"


async def main():
    print("main开始")
    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    task1 = asyncio.create_task(func())
    # 创建协程，将协程封装到一个Task对象中并立即添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    task2 = asyncio.create_task(func())
    task3 = asyncio.create_task(func())
    task4 = asyncio.create_task(func())
    task5 = asyncio.create_task(func())
    print("main结束")
    # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
    # 此处的await是等待相对应的协程全都执行完毕并获取结果
    ret1 = await task1
    ret2 = await task2
    ret3 = await task3
    ret4 = await task4
    ret5 = await task5
    print(ret1, ret2, ret3, ret4, ret5)


# 方式1
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# 方式2
asyncio.run(main())
