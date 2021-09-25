import threading
import sys, math
import socket, ftplib
import random
import pickle ###serialize shit/ or make it kill itself before it gets too big a buffer 
import time
print "\n +-+-+-+-+-+-+-+-+-+-+-+"
print   " |--------ZMAP---------|"
print   " +-+-+-+-+-+-+-+-+-+-+-+"
threads = str(sys.argv[1])
count = 0
ipf=open('list.txt', 'w')
ipf.write('')
ipf.close()
running = 0
port = 80 #str(sys.argv[2])
#print("scanning: " + port)
def yadigg():
#    for x in range(50): use thisif you on normal hydra not the shitty windows one
        while running < 10: #lazy mans thread killing by making tog switch/ doesnt need on linux but the windows hydra is fucky
            p=random.randint(1,254)
            q=random.randint(1,254)
            r=random.randint(1,254)
            s=random.randint(1,254)
            global running
            ip=str(p) + "." +str(q) + "." +str(r) + "." +str(s)
            if (p==10 or p==127):
                #Private IP and Loopback IP
                ip = "null"
            elif (p == 100 and q >= 64 and q <= 127):
                #Shared Address Space
                ip = "null"
            elif (p >= 0 and p <= 15 and q >= 0 and q <= 20):
                #STARTS ON 15.20.X.X
                ip = "null"
            elif (p == 169 and q == 254):
                # APIPA
                ip = "null"
            elif (p == 172 and q >= 16 and q <= 31):
                #Private IP  172.16.0.0 - 172.31.255.255
                ip = "null"
            elif (p == 192 and q == 0 and r == 0):
                #192.0.0.0/24        # RFC6890: IETF Protocol Assignments
                ip = "null"
            elif (p == 192 and q == 0 and r == 2):
                #192.0.2.0/24        # RFC5737: Documentation (TEST-NET-1)
                ip = "null"
            elif (p == 192 and q == 88 and r == 99):
                #192.88.99.0/24      # RFC3068: 6to4 Relay Anycast
                ip = "null"
            elif (p == 192 and q == 168):
                #RFC1918: Private-Use
                ip = "null"
            elif (p == 192 and q == 18):
                # RFC2544: Benchmarking
                ip = "null"
            elif (p == 192 and q == 19):
                # RFC2544: Benchmarking
                ip = "null"
            elif (p == 192 and q == 51 and r == 100):
                # RFC5737: Documentation (TEST-NET-2)
                ip = "null"
            elif (p == 203 and r == 113):
                # RFC5737: Documentation (TEST-NET-2)
                ip = "null"
            elif (p >= 224):
                # RFC5737: Reserved D & E
                ip = "null"
            if (ip != "null"):
                pass
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.5)
                result = sock.connect((ip, port))
                try:
                    dns, alias, addresslist = socket.gethostbyaddr(ip)
                    dns.replace("'", '')
                    #print(dns)
                    print " [!] FOUND: " + ip + " : " + dns+ "[!]"
                    ipf=open('list.txt', 'a')
                    ipf.write(ip +  '\n' + dns + '\n')
                    ipf.close()
                    running = running + 1
                except:
                    ipf=open('list.txt', 'a')
                    ipf.write(ip +  '\n')
                    ipf.close()
                    running = running + 1
                    print " [!] FOUND: " + ip + " [!]\n"
                    pass
            #count = count + 1 
            except Exception ,e:
                pass         
for threads in range(0, int(threads)):
	try:
		count = count + 1
		t = threading.Thread(target=yadigg)
		#t.daemon=True
		t.start()
	except:
		print('Thread failed: ' + str(count))
print('Threads: ' + str(count))
