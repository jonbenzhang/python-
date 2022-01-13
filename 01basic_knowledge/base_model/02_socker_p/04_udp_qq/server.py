import socket

udp_sk = socket.socket(type=socket.SOCK_DGRAM)
udp_sk.bind(("0.0.0.0", 8969))
print("wait for data")
while True:
    msg, addr = udp_sk.recvfrom(1024)
    print(addr, msg.decode("utf-8"))
    # .encode("utf-8")  str -->bytes
    info = input("input>>").encode("utf-8")
    udp_sk.sendto(info, addr)
udp_sk.close()