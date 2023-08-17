import selectors
import collections

selector = selectors.DefaultSelector()

class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            return

        next_future.add_done_callback(self.step)

def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

# Usage:

import socket

async def echo_server(address):
    sock = socket.socket()
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await accept_client(sock)
        await handle_echo(client)

def accept_client(sock):
    f = Future()

    def on_accept():
        conn, addr = sock.accept()
        f.set_result((conn, addr))

    selector.register(sock.fileno(), selectors.EVENT_READ, on_accept)
    return f

async def handle_echo(client):
    while True:
        data = await client_recv(client)
        if not data:
            break
        await client_send(client, data)

# similarly, client_recv and client_send implemented

Task(echo_server(('', 25000)))
loop()