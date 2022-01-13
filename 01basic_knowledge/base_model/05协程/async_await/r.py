import requests
import asyncio

# url = "http://0.0.0.0:15061/empi/api/data_standard/catalog/get?classify=%E5%8C%BB%E7%96%97%E6%9C%8D%E5%8A%A1"
url = "http://172.20.3.21:8903/empi/api/data_standard/catalog/get?classify=%E5%8C%BB%E7%96%97%E6%9C%8D%E5%8A%A1"
c = {200: 0, 500: 0}
lock = asyncio.locks


def count():
    pass


async def b():
    for _ in range(10):
        b = requests.get(url)
        c[b.status_code] += 1
        # print(type(b.status_code))


# 获取EventLoop:
# loop = asyncio.get_event_loop()
# 执行coroutine
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
async def main():
    tasks = [b() for _ in range(100)]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
    print(c)