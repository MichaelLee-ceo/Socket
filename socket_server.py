import socket
from tools import *
import param

sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sever.bind(('', 6969, ))
sever.listen(5)
print("Waiting for connection...")

while True:
    conn, addr = sever.accept()
    print("connect from device", addr)
    handle = param.PARAM(server = conn)

    while True:
        data = handle.read()
        print(data)
        handle.write(data)
        # data = conn.recv(1024)
        # if str(data) == "b\'end\'":
        #     print('Terminal connection from device', addr,  '\n')
        #     break
        #
        # print("Message: ", str(data))
        # conn.send(b'Server received your message.')

    conn.close()

server.shutdown(socket.SHUT_RDWR)
sever.close()




