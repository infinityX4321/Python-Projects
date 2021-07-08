import socket
ip='192.168.1.103'
port_list = [20,80,8080,139,445,23,21,22]
for port in port_list:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #FTP
    result=s.connect_ex((ip,port))
    if result==0:
        print('port: ',port,'open')
    else:
        print('port: ',port,'closed')
