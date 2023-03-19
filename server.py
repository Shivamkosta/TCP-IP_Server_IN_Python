import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
sktadd = (host, port)
print("Server running on ", sktadd)
skt.bind(sktadd)
skt.listen(5)
client, add = skt.accept()
while True:
    data = client.recv(1024)
    if data:
        print("RECIEVED DATA FROM CLIENT: ", data.decode('utf-8'))
client.close()

