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
file = (sys.argv[3])
ipf=open(file, 'w')
ipf.write('')
ipf.close()
running = 0
port = str(sys.argv[2])
if len(sys.argv) < 4:
	print("use: zmap.py threads port output.txt")
	exit()
else:
	pass
	
#print("scanning: " + port)
def yadigg():
#    for x in range(50): use thisif you on normal hydra not the shitty windows one
        while running < 10: #lazy mans thread killing by making tog switch/ doesnt need on linux but the windows hydra is fucky
            a=random.randint(1,254)
            b=random.randint(1,254)
            c=random.randint(1,254)
            d=random.randint(1,254)
            global running
            ip=str(a) + "." +str(b) + "." +str(c) + "." +str(d)
            #print(ip + ":" + port)
            #port = str(sys.argv[2])
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.5)
                result = sock.connect((ip, port))
                try:
                    dns, alias, addresslist = socket.gethostbyaddr(ip)
                    dns.replace("'", '')
                    #print(dns)
                    print " [!] FOUND: " + ip + " : " + dns+ "[!]\n"
                    ipf=open('list.txt', 'a')
                    ipf.write(ip +  '\n' + dns + '\n')
                    ipf.close()
                    running = running + 1
                except:
                    ipf=open('list.txt', 'a')
                    ipf.write(ip +  '\n' + dns + '\n')
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
