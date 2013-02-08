#test python script
import serial
import time

ser = serial.Serial("COM3", 9600)
time.sleep(2)
print "ready"
time.sleep(1)
print "sending 'T'"
ser.write('T')

time.sleep(1)

print "sending 'F'"
ser.write('F')