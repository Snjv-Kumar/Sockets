import socket



s=socket.socket()
print("socket created")


s.bind(("localhost",9999))

s.listen(5)
print("waiting for connection")


while True:
    c,add=s.accept()
    name=c.recv(1024).decode()
    print("connected with",add,name)

    c.send(bytes("welcome my friend",'utf-8'))

    c.close()
