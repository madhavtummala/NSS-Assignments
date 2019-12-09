import socket
import threading
import random
import time
import argparse
import sys

def client(SERVER):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((SERVER.IP,int(SERVER.PORT)))
	welcome_message=sock.recv(1024)
	print(welcome_message)
	p=input("Enter the option: ")
	sock.sendall(str(p))
	x=sock.recv(1024)
	while(x=="Please enter a valid choice"):
		p=input("Enter the option: ")
		sock.sendall(str(p))
		x=sock.recv(1024)
	if p == 1 or p == 2:
		print(x)
		p=input()
		sock.sendall(str(p))
		x=sock.recv(1024)
		print(x)
	elif p==3 or p==5:
		print(x)
		p=input()
		sock.sendall(str(p))
		x=sock.recv(1024)
		print(x)
		p=input()
		sock.sendall(str(p))
		x=sock.recv(1024)
		print(x)
	else:
		print(x)
		p=input()
		sock.sendall(str(p))
		x=sock.recv(1024)
		print(x)
		p=input()
		sock.sendall(str(p))
		x=sock.recv(1024)
		print(x)
		p=input()
		sock.sendall(str(p))
		x=sock.recv(1024)
		print(x)
		
if __name__ == "__main__":
	sys.stdout.flush()
	parser = argparse.ArgumentParser()
	parser.add_argument('-IP', required=True)
	parser.add_argument('-PORT', required=True)
	args=parser.parse_args()
	client(args)