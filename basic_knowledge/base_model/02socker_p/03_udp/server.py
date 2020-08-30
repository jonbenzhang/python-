import socket

udp_sk = socket.socket(type=socket.SOCK_DGRAM)
udp_sk.bind(("0.0.0.0", 8969))
print("wait for data")
msg, addr = udp_sk.recvfrom(1024)
print(msg.decode("utf-8"))
udp_sk.sendto(b"i'm server", addr)
udp_sk.close()