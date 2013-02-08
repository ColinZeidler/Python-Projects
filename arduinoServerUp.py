#arduino Server viewer

import serial
import time
import socket

ser = serial.Serial("COM3", 9600)
time.sleep(2)
print "ready"

host = '172.19.73.56'
port = 25565

while True:
    print "checking server status"
    exists = True
    s = socket.socket()
    s.settimeout(2)
    
    try: #attempt to connect
        s.connect((host,port))
    except:
        exists = False
    
    if exists:
        ser.write('T')
        print "sent 'T'"
    else:
        ser.write('F')
        print "sent 'F'"
        
    s.close()
    del s
    
    time.sleep(2)