import socket
import threading
import random
import time
import sys
import argparse
import json
import fnmatch

def connection(conn,addr):
	conn.sendall("Hi, you are connected to server. Press 1 to do a lookup"+
			" by name, 2 for a lookup by phone number, 3 to update name against number"+
			", 4 to update number against name, 5 to register a new entry")
	choice=int(conn.recv(1024))
	while True:
		if choice == 1:
			with open("database_name.json","r") as f:
				s=f.read()
			s=json.loads(s)
			conn.sendall("Please enter the name")
			search=conn.recv(1024)
			k = [ r for r in s.keys() ]
			k = fnmatch.filter(k,search+"*")
			subdict=dict()
			for i in k:
				subdict[i]=s[i]
			s=json.dumps(subdict)
			if len(subdict)>0:
				conn.sendall("The possible matches are: "+s)
			else:
				conn.sendall("Couldn't find such an entry :(")
			break
		elif choice == 2:
			with open("database_mob.json","r") as f:
				s=f.read()
			s=json.loads(s)
			conn.sendall("Please enter the number")
			search=conn.recv(1024)
			k = [ r for r in s.keys() ]
			k = fnmatch.filter(k,search+"*")
			subdict=dict()
			for i in k:
				subdict[i]=s[i]
			s=json.dumps(subdict)
			if len(subdict)>0:
				conn.sendall("The possible matches are: "+s)
			else:
				conn.sendall("Couldn't find such an entry :(")
			break
		elif choice == 3:
			conn.sendall("Enter the number whose name to update")
			num=conn.recv(1024)
			conn.sendall("Enter the new name")
			new_name=conn.recv(1024)
			with open("database_mob.json","r") as f:
				s=f.read()
			s=json.loads(s)
			if num not in s:
				conn.sendall("Couldn't find entry to update")
				break
			old_name=s[num]
			with open("database_name.json","r") as f:
				ss=f.read()
			ss=json.loads(ss)
			if new_name in ss:
				conn.sendall("This name already exists. Please choose a new name")
				break
			s[num]=new_name
			with open("database_mob.json","w") as f:
				f.write(json.dumps(s))
			with open("database_name.json","r") as f:
				s=f.read()
			s=json.loads(s)
			s[new_name]=s.pop(old_name)
			with open("database_name.json","w") as f:
				f.write(json.dumps(s))
			conn.sendall("Database updated successfully")
		elif choice == 4:
			conn.sendall("Enter the name whose number to update")
			target=conn.recv(1024)
			conn.sendall("Enter the new number")
			new_number=conn.recv(1024)
			with open("database_name.json","r") as f:
				s=f.read()
			s=json.loads(s)
			if target not in s:
				conn.sendall("Couldn't find entry to update")
				break
			old_number=s[target]
			s[target]=new_number
			with open("database_name.json","w") as f:
				f.write(json.dumps(s))
			with open("database_mob.json","r") as f:
				s=f.read()
			s=json.loads(s)
			s[new_number]=s.pop(old_number)
			with open("database_mob.json","w") as f:
				f.write(json.dumps(s))
			conn.sendall("Database updated successfully")
		elif choice == 5:
			conn.sendall("Enter the name")
			target_name=conn.recv(1024)
			conn.sendall("Enter the number")
			target_number=conn.recv(1024)
			with open("database_mob.json","r") as f:
				s=f.read()
			s=json.loads(s)
			with open("database_name.json","r") as f:
				s2=f.read()
			s2=json.loads(s2)
			if target_name in s2:
				conn.sendall("Name already exists. Consider updating rather than adding")
				break
			elif target_number in s:
				conn.sendall("Number already exists. Consider updating rather than adding")
				break
			s[target_number]=target_name
			with open("database_mob.json","w") as f:
				f.write(json.dumps(s))
			s2[target_name]=target_number
			with open("database_name.json","w") as f:
				f.write(json.dumps(s2))
			conn.sendall("Addition successful")
			break
		else:
			conn.sendall("Please enter a valid choice")
			choice=int(conn.recv(1024))

def server(SERVER):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((SERVER.IP,int(SERVER.PORT)))
	sock.listen(4)
	x=0
	while True:
		x+=1
		(conn,addr) = sock.accept()
		t = threading.Thread(target=connection, args=(conn, addr))
		t.start()
		if x>=3:
			break

if __name__ == "__main__":
	sys.stdout.flush()
	parser = argparse.ArgumentParser()
	parser.add_argument('-IP', required=True)
	parser.add_argument('-PORT', required=True)
	args=parser.parse_args()
	server(args)