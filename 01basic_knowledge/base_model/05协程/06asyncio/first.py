import asyncio


@asyncio.coroutine
def func1():
    print(1)
    # 遇到io阻塞自动切换，可以自动识别io,asyncio.sleep(2)是io的一种
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到tasks中的其他任务
    print(4)

# 将所有的协程打包到task中
tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
# 生成一个时间循环
loop = asyncio.get_event_loop()
#  启动事件循环把所有的协程放如其中,随机执行task中的程序
loop.run_until_complete(asyncio.wait(tasks))
