import socket

HOST = 'chitturi'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('chitturi', 50007))
s.listen(1)
conn, addr = s.accept()
#print 'Connected by', addr
while 1:
    data = conn.recv(1027)
    if not data: break
    conn.send(data)
conn.close()
print "hello"
