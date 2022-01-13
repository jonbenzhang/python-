import asyncio
import threading

# 把python3.5 @asyncio.coroutine换为def 前面加async
async def func1():
    print(1)
    print(threading.current_thread())
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    print(threading.current_thread())
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
# 执行的方式1
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
# 执行的方式2
# asyncio.run([func1(),func2()])
