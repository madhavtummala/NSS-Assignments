#!/usr/bin/python
import socket
import threading
import random
import time


CLIENT=8080
IP = '127.0.0.1'
SERVER_LIST = [8081,8082,8083,8084]

arp_table = {}
mac_list = ['c3:95:ae:08:6d:3f',
            '80:5c:1c:46:c6:67',
            '3a:aa:75:0b:96:a2',
            'b3:8b:62:9f:e8:cf']

def server(SERVER):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP,SERVER))

    while True:
        (data,addr) = sock.recvfrom(1024)

        if data==str(SERVER):
            sock.sendto(mac_list[SERVER-8081],(IP,CLIENT))

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP,CLIENT))
    
    # sock.settimeout(0.5)  #waits for 0.5 sec

    while True:
        request = random.randint(8081,8084)

        if request in arp_table.keys():
            print ('Mac address is '+arp_table[request])
        else:
            for SERVER in SERVER_LIST:
                sock.sendto(str(SERVER),(IP,SERVER))

            (data,addr) = sock.recvfrom(1024)
            arp_table[request] = data

            print ('\n****Current ARP Table****')

            d = arp_table
            max_len = max([len(v) for v in d.values()])
            padding = 4
            for k,v in sorted(d.items(), key=lambda i:i[1]):
                print('127.0.0.1:{k:3} {v:{v_len:d}}'.format(v_len=max_len+padding,v=v, k=k))

            print '\n'

        time.sleep(1)


for SERVER in SERVER_LIST:
    threading.Thread(target=server,args=(SERVER,)).start()

threading.Thread(target=client).start()