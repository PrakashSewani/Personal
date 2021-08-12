import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
"""
Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.
"""
ip=socket.gethostbyname('www.google.com')
print(ip)

