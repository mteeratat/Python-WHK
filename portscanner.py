# import pyfiglet
import sys
import socket
import threading
import time
from datetime import datetime
  
def threadF(start,end):
    for port in range(start,end):
        # print(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

# ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
# print(ascii_banner)

# Defining a target
if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
 
# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
t = []
  
try:
    start = time.time()
    # will scan ports between 1 to 65,535
    # for port in range(1,200):
    #     # print(port)
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     socket.setdefaulttimeout(1)
         
    #     # returns an error indicator
    #     result = s.connect_ex((target,port))
    #     if result == 0:
    #         print("Port {} is open".format(port))
    #     s.close()

    # t1 = threading.Thread(target=threadF, args=(1,100))
    # t2 = threading.Thread(target=threadF, args=(100,200))
    # t3 = threading.Thread(target=threadF, args=(200,300))
    # t4 = threading.Thread(target=threadF, args=(300,400))
    # t5 = threading.Thread(target=threadF, args=(400,500))
    # t6 = threading.Thread(target=threadF, args=(500,600))
    # t7 = threading.Thread(target=threadF, args=(600,700))
    # t8 = threading.Thread(target=threadF, args=(700,800))
    # t9 = threading.Thread(target=threadF, args=(800,900))
    # t10 = threading.Thread(target=threadF, args=(900,1000))

    for i in range(200):
        t.append(threading.Thread(target=threadF, args=(i*200,(i+1)*200)))

    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    # t7.start()
    # t8.start()
    # t9.start()
    # t10.start()

    for i in range(200):
        t[i].start()

    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
    # t7.join()
    # t8.join()
    # t9.join()
    # t10.join()

    for i in range(200):
        t[i].join()

    end = time.time()
    print(end - start)
    
         
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()