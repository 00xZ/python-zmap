import threading
import sys, math
import socket, ftplib
import random
import pickle ###serialize shit/ or make it kill itself before it gets too big a buffer 
import time
print ("\n +-+-+-+-+-+-+-+-+-+-+-+")
print   (" |--------ZMAP---------|")
print   (" +-+-+-+-+-+-+-+-+-+-+-+")
print ("use:zmap.py port threads output.txt")
threads = str(sys.argv[2])
count = 0
ipf=open('list.txt', 'w')
ipf.write('')
ipf.close()

port = int(sys.argv[1])
def yadigg():
    global running
    running = (0)
#    for x in range(50): use thisif you on normal hydra not the shitty windows one
    while running < 10: #lazy mans thread killing by making tog switch/doesnt need on linux but the windows hydra is fucky
            p=random.randint(1,254)
            q=random.randint(1,254)
            r=random.randint(1,254)
            s=random.randint(1,254)
            #global running
            ip=str(p) + "." +str(q) + "." +str(r) + "." +str(s)
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.5)
                result = sock.connect((ip, port))
                try:
                    #dns, alias, addresslist = socket.gethostbyaddr(ip)
                    #dns.replace("'", '')
                    #print(dns)
                    print (" [X] FOUND: " + ip +" [X] ")
                    ipf=open('list.txt', 'a')
                    ipf.write(ip +  '\n')
                    ipf.close()
                    running = running + 1
                except:
                    #ipf=open('list.txt', 'a')
                    #ipf.write(ip +  '\n')
                    #ipf.close()
                    #running = running + 1
                    #print " [!] FOUND: " + ip + " [!]\n"
                    pass
            #count = count + 1 
            except: #Exception ,e:
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
