import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1', 99, ))

#while True:
#client.send(b"Hi!")
client.send(bytes('Hello','utf8'))
data = client.recv(1024)
print("receive:", str(data,'utf8'))

client.close()

