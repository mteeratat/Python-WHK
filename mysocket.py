import socket
import re

file = open('myfile.txt', 'r')
data = file.read()
file.close()
data = data.replace("\'", "")
data = data.replace("\"", "")
data = data.split(", ")
# [print(d) for d in data]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("104.248.39.146" , 27617))
# s.sendall("GET / HTTP/1.1\r\n\r\n")
request = "GET / HTTP/1.1\r\n\r\n\r\n"
s.send(request.encode()) 
print(s.recv(4096).decode())
# s.send(b"chayote fruit-kundong-chayote fruit")
for d in data:
    for a in data:
        for t in data:
            st = d + '-' + a + '-' + t
            print(st)
            s.send(st.encode())
            data = s.recv(4096).decode()
            print(data)
            
# data = s.recv(4096)
# print(data)
s.close