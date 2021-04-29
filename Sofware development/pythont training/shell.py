import socket

s=socket.socket(); #create socket object
port=9999;
host='';
s.bind((host,port)); #bind adress to end of socket
s.listen(5);
while True:
    conn,addr=s.accept(); # accept connection from client
    print('Got a connection from : '+str(conn));
    print('Ip :'+str(addr[0])+' port :'+str(addr[1]));
    file=open('datatosend.txt','rb+'); #open file for both reading and writing binary
    data=str.encode(file);
    s.send(data);
    s.close();