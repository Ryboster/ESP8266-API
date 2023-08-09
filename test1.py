import serial
from vpython import *
import time
import regex as re

class Communicate:
        def __init__(self, connection):
            self.connection = connection
        
        def reset(self):
            self.connection.write("AT+RST\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def cwmode(self):
            self.connection.write("AT+CWMODE?\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def cwSTA(self):
            self.connection.write("AT+CWMODE=1\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def cwAP(self):
            self.connection.write("AT+CWMODE=2\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def cwBOTH(self):
            self.connection.write("AT+CWMODE=3\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def ishost(self):
            self.connection.write("AT+CIPMUX?\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            self.connection.write("AT+CIFSR\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def starthost(self):
            self.connection.write("AT+CIPMUX=1\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def endhost(self):
            self.connection.write("AT+CIPMUX=0\r\n".encode())
            time.sleep(1)
            dataPacket = self.connection.read_all()
            self.print(dataPacket)
            return
        def print(self, packet):
            time.sleep(2)
            try:
                decodedPacket = str(packet, "utf-8")
                decodedPacket = decodedPacket.strip('b').strip('\'')
            except UnicodeDecodeError:
                decodedPacket = str(packet)
                decodedPacket = decodedPacket.strip('b').strip('\'')
            print(decodedPacket)
            return
            

connection1 = serial.Serial("/dev/ttyACM0", 115200)
time.sleep(1)
while True:
    while True:
        x = input("> ")
        if x == "reset":
            Communicate(connection1).reset()
        elif x == "mode?":
            Communicate(connection1).cwmode()
        elif x == "setmode":
            print("Syntax: \nsetmode STA | AP | BOTH")
            print("STA = Station mode. Used for connecting")
            print("AP = Access Point. Used for hosting")
            print("BOTH = STA+AP.") 
        elif x == "setmode STA" or x == "setmode 1":
            Communicate(connection1).cwSTA()
        elif x == "setmode AP" or x == "setmode 2":
            Communicate(connection1).cwAP()
        elif x == "setmode BOTH" or x == "setmode 3":
            Communicate(connection1).cwBOTH()
        elif x == "host?" or x =="ishost":
            Communicate(connection1).ishost()
        elif x == "host start" or x == "host 1":
            Communicate(connection1).starthost()
        elif x == "host end" or x == "host 0":
            Communicate(connection1).endhost()
        elif x.startswith("help"):
            command = re.search(r'(?<=help ).*?([A-Z].*?[.!?])', str(x))
            if command:
                print(command.group(0))
            else:
                print("command not found")
        else:
            print("Command not recognized:", str(x))
    
            
        