import socket
import os
import hashlib
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',9000))
data, addr = server_socket.recvfrom(2000)
server_socket.sendto("name_received".encode(), addr)
print('file recv start from %s'%(addr[0]))
print(data)
file_name = data.decode()
print('File Name : %s'%(file_name))
data, addr = server_socket.recvfrom(2000)
server_socket.sendto("size_received".encode(), addr)
file_size = int(data)
print('File Size : %d'%(file_size))
acc = 0;
with open(file_name, 'wb') as f:
	while True:
		data = server_socket.recv(1024)
		if not data:
			break
		f.write(data)
		acc += len(data)
		if  acc == file_size:
			print("current_size / total_size = %d/%d, %.1f%%"%(acc,file_size,100*acc/file_size))
			break
		print("current_size / total_size = %d/%d, %.15f%%"%(acc,file_size,100*acc/file_size))
print("The md5 value of the received file is : %s"%(hashlib.md5(open(file_name,'rb').read()).hexdigest()))
f.close()
