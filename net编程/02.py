'''
- Client端流程
            - 建立通信的socket
            - 发送内容到指定服务器
            - 接受服务器给定的反馈内容
'''

import socket

def clientFunc():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = 'I love jingjing'

    # 发送的数据必须是byte格式
    data = text.encode()

    # 发送
    sock.sendto(data,('127.0.0.1',7852))

    data,addr = sock.recvfrom(200)

    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFunc()