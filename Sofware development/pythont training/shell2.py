import socket

s=socket.socket(); #create socket object
port=9999;
host='mechatron';
s.connect((host,port)); #connect to the socket of server
data=s.recv(1024); #recieve data from server
s.close();