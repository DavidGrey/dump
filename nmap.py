import socket
from os import devnull
from subprocess import Popen
#print(socket.gethostbyaddr("192.168.1.2"))





def ping(device_ip):
    '''Sends one ping to the device on the LAN with the specified IP'''
    with open(devnull, "wb") as limbo:
        while True:
            result = Popen(["ping", "-n", "1", "-w", "200", \
                     device_ip], stdout=limbo, stderr=limbo).wait()
            if result:
                return False
            else:
                return True

#Pings the given IP num_ping times and returns True
#if it gets a response to any of them
def get_sample(device_ip, num_ping):
    '''Pings the specified device num_ping times and returns a list
    of the responses
    '''
    return any([ping(device_ip) for i in range(num_ping)])



def nmap(start, end):
    for i in range(start, end+1):
        device = socket.gethostbyaddr("192.168.1."+str(i))
        print device[0], device [2]
        print get_sample(device[0], 5)
        print "\n"
        
    
nmap(5, 12)

