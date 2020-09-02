from socket import *

ip_port = ('127.0.0.1', 9000)
bufsize = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>: ').strip()
    udp_client.sendto(msg.encode('utf-8'), ip_port)
    err, addr = udp_client.recvfrom(bufsize)
    out, addr = udp_client.recvfrom(bufsize)
    if err:
        print('error : %s' % err.decode('utf-8'), end='')
    if out:
        print('success:%s' % out.decode('utf-8'), end='')

# udp - client
