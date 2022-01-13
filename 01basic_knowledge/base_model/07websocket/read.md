# websocket原理
1. 服务端等待运行等待连接
2. 客户端来和服务器连接，服务器同意连接成功
3. 客户端来连接后，发送来了一个“握手信息”
    'GET /message HTTP/1.1\r\nHost: 0.0.0.0:8008\r\nConnection: Upgrade\r\nPragma: no-cache\r\nCache-Control: no-cache\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36\r\nUpgrade: websocket\r\nOrigin: http://localhost:63342\r\nSec-WebSocket-Version: 13\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\nSec-WebSocket-Key: WbKb8XZ0K2mh7EHC3An36Q==\r\nSec-WebSocket-Extensions: permessage-deflate; client_max_window_bits\r\n\r\n'
    
    GET /message HTTP/1.1
    Host: 0.0.0.0:8008
    Connection: Upgrade
    Pragma: no-cache
    Cache-Control: no-cache
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
    Upgrade: websocket
    Origin: http://localhost:63342
    Sec-WebSocket-Version: 13
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Sec-WebSocket-Key: WbKb8XZ0K2mh7EHC3An36Q==
    Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
    
    1. Sec-WebSocket-Key 是一个Base64 encode的值，这个是浏览器随机生成的,秘文
    2. Sec_WebSocket-Protocol 是一个用户定义的字符串，用来区分同URL下，不同的服务所需要的协议
4. 服务器接收到握手的信息，然后对数据进行加密，然后返回给客户端
    'HTTP/1.1 101 Switching Protocols\r\nUpgrade:websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: JuTPcfYeuIf88FS4rTco0CBeej0=\r\nWebSocket-Location: ws://0.0.0.0:8008\r\n\r\n'
    HTTP/1.1 101 Switching Protocols
    Upgrade:websocket
    Connection: Upgrade
    Sec-WebSocket-Accept: JuTPcfYeuIf88FS4rTco0CBeej0=
    WebSocket-Location: ws://0.0.0.0:8008
    1. Sec-WebSocket-Accept的值是服务端采用与客户端一致的密钥（Sec-WebSocket-Key）计算出来后返回客户端的
5. 客户端验证服务器发送过来的信息，如果正确则连接成功
    
6. 双方可以进行任意通信了
    1. 客户端发送消息给服务器

        1.服务器读取客户端发送过来的数据，二进制的9-15位数据，也就是第二个字节的后7位(可以把第二个字节通过与127进行与运算获取后7位)
        2. 如果后7位的值为
            127：那就是数据的前10个字节为请求头，后面的为发送过来的数据
            126：那就是数据的前4个字节为请求头，后面的为发送过来的数据
            小于等于125：那就是数据的前2个字节为请求头，后面的为发送过来的数据
        3. 后面数据的前4个字节为MASK，再后面就为真正的数据（decoded）
            把获取到的数据decode和MASK进行如下运算,最后得到的bytes_list为发送过来的数据
            ```
             bytes_list = bytearray()
            for i in range(len(decoded)):
                chunk = decoded[i] ^ mask[i % 4]
                bytes_list.append(chunk)
            bytes_list # 为发送过来的数据
           ```
        4.具体代码实现
            ```
                payload_len = info[1] & 127
                if payload_len == 127:
                    extend_payload_len = info[2:10]
                    mask = info[10:14]
                    decoded = info[14:]
                elif payload_len == 126:
                    extend_payload_len = info[2:4]
                    mask = info[4:8]
                    decoded = info[8:]
                else:
                    extend_payload_len = None
                    mask = info[2:6]
                    decoded = info[6:]
            
                bytes_list = bytearray()
                for i in range(len(decoded)):
                    chunk = decoded[i] ^ mask[i % 4]
                bytes_list.append(chunk)
            body = str(bytes_list, encoding='utf-8')
           ```
    2. 服务器像客户端发送数据
        1. 具体代码实现
        ```
            token = b"\x81"
            length = len(msg_bytes)
            if length < 126:
                token += struct.pack("B", length)
            elif length <= 0xFFFF:
                token += struct.pack("!BH", 126, length)
            else:
                token += struct.pack("!BQ", 127, length)
        
            msg = token + msg_bytes
        ```