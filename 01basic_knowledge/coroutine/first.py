import asyncio

async def f1():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "f1"

async def f2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return "f2"

async def main():
    tasks = [
        asyncio.create_task(f1(), name="t1"),
        asyncio.create_task(f2(), name="t2"),
        asyncio.ensure_future(f1())
    ]
    for t in tasks:
        print(t.get_name())
    await asyncio.wait(tasks)

asyncio.run(main())