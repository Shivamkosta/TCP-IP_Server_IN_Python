import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
sktadd = (host, port)
print("Connected to: ", skt)
skt.connect(sktadd)
msg = input("Enter a message: ")
while msg != "end":
    skt.sendall(msg.encode("utf-8"))
    msg = input("Enter a message:")
skt.close()


