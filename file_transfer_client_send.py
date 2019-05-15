import socket
import os
import hashlib
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file_name = input("Input your file name : ")
f = open(file_name,'rb')
file_size = os.path.getsize(file_name)
socket.sendto(file_name.encode(), ('localhost',9000))
data, addr = socket.recvfrom(2000)
socket.sendto(str(file_size).encode(), ('localhost',9000))
data, addr = socket.recvfrom(2000)
print("File Transmit Start....")
l = '0';
acc = 0;
while l:
	l = f.read(1024)
	socket.sendto(l, addr)
	acc += len(l);
	if acc == file_size:
		break
	print("current_size / total_size = %d/%d, %.15f%%"%(acc,file_size,100*acc/file_size))
print("current_size / total_size = %d/%d, %.1f%%"%(acc,file_size,100*acc/file_size))
f.close()
print("ok")
print("file_send_end")
print("The md5 value of the sent file is : %s"%(hashlib.md5(open(file_name,'rb').read()).hexdigest()))
