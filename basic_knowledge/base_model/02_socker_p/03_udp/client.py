import socket

udp_sk = socket.socket(type=socket.SOCK_DGRAM)
addr = ("0.0.0.0", 8969)
udp_sk.sendto(b"i'm client",addr)
rec_data,addr = udp_sk.recvfrom(1024)
print(rec_data.decode("utf-8"))
udp_sk.close()
