import socket

s=socket.socket()
print('Socket created succesfully')

# reserve a port on your computer in our 
# case it is 1235 but it can be anything
port=1235

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('',port))
print('Socket binded to port %s'%(port))

# put the socket into listening mode
s.listen(5)
print('Socket is listening')

while True:
    c,addr=s.accept()
    print('Got connection from ',addr)
    message=input('Enter Message:')
    res=bytes(message,'utf-8')
    c.send(res)
    c.close()
