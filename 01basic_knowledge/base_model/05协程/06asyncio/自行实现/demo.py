import socket
from selectors import EVENT_READ, EVENT_WRITE, DefaultSelector
from socket import create_connection

selector = DefaultSelector()
stopped = False
urls_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}


class Future:
    """
    未来对象
    异步调用执行完的时候，就把结果放在它里面。
    """

    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)


class Crawler:
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('example.com', 80))
        except BlockingIOError:
            pass
        f = Future()

        def on_connect():
            f.set_result(None)

        selector.register(sock.fileno(), EVENT_WRITE, on_connect)
        yield f
        selector.unregister(sock.fileno())
        get = 'GET {0} HTTP/1.0 \r\nHost: example.com\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))

        global stopped
        while True:
            f = Future()

            def on_readable():
                f.set_result(sock.recv(4096))

            selector.register(sock.fileno(), EVENT_READ, on_readable)
            chunk = yield f
            selector.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                urls_todo.remove(self.url)
                if not urls_todo:
                    stopped = True
                    break


class Task:
    """任务对象"""

    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            # send放到coro执行，即fetch，直到下次yield
            # next_future为yield返回对象
            next_future = self.coro.send(future.result)
        except StopIteration:
            return
        next_future.add_done_callback(self.step)


def loop():
    """事件循环驱动协程"""
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()
    import asyncio
    asyncio.get_event_loop()
    asyncio.run()


if __name__ == "__main__":
    import time

    start = time.time()
    for url in urls_todo:
        crawler = Crawler(url)
        Task(crawler.fetch())
    loop()
    print(time.time() - start)

"""
现在loop有了些许变化，callback()不再传递event_key和event_mask参数。也就是说，
这里的回调根本不关心是谁触发了这个事件,
结合fetch()可以知道，它只需完成对future设置结果值即可f.set_result()。
"""
