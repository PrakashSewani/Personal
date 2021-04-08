import socket
import sys

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket Successfully created')
except socket.error as err:
    print('Socket creation failed due to %s'%(err))

port=80

try:
    host_ip=socket.gethostbyname('www.google.com')
    print(host_ip)
except socket.gaierror:
    # this means could not resolve the host 
    print ("There was an error resolving the host")
    sys.exit()

s.connect((host_ip,port))

print('Socket successfully connected to google')

f=socket.gethostbyaddr('www.google.com')
print(f)