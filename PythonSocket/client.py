#Assignment Submitted by: Nudrat Nawal Saber
#UTA ID: 1001733394
#https: // www.programcreek.com/python/example/1816/SocketServer.ThreadingMixIn
#https: // docs.python.org/3/library/http.server.html

import socket
import sys
import http.client
import time

# Check validity of hostname
def check_host_name(name):
    if name == 'localhost' or name == '127.0.0.1':
        return True
    return False
        
# Checks validity of port number
def check_port_number(port):
    return port.isdigit()
        
class init_value_client():
    
    def __init__(self, host_name, port_number, file_name):
        self.HOST = host_name
        self.PORT = port_number
        self.FILE = file_name
    def initiation(self):
        # Parsing user arguments and checking validity
        if len(sys.argv) > 4:
            print("Too many arguments provided. Default values are being used.\n")
        elif len(sys.argv) == 4:
            if check_host_name(sys.argv[1])==False:
                print("Invalid host address. Using localhost by default\n")
            self.HOST = '127.0.0.1'
            
            if check_port_number(sys.argv[2])==False:
                print("Invalid port number. Using port 8080\n")
            self.PORT = int(sys.argv[2])
            
            self.FILE = sys.argv[3]
            
        elif len(sys.argv) == 3:
            if check_host_name(sys.argv[1])==False:
                print("Invalid host address. Using localhost by default\n")
            self.HOST = '127.0.0.1'
            
            if check_port_number(sys.argv[2])==False:
                print("Invalid port number. Using port 8080\n")
            self.PORT = int(sys.argv[2])
            
            print("Filename not provided. Default filename is used.\n")
        
        elif len(sys.argv) == 2:
            if check_host_name(sys.argv[1])==False:
                print("Invalid host address. Using localhost by default.\n")
            self.HOST = '127.0.0.1'
            
            print("Port number and filename not provided. Using port 8080 and default filename.\n")
        else:
            print("No argument provided. Default values are being used.\n")
    

class HttpClient():    
    
    # Method instantiates the class
    def __init__(self, host_name, port_number, file_name):
        self.host = host_name
        self.port = port_number
        self.file = file_name
    
    # Creating http request, sending it, and printing the received file content with connection parameters
    def make_request(self):
        connection = http.client.HTTPConnection(self.host + ':' + str(self.port))
        
        try:
            # Calculate Round Trip Time
            request_time = time.time()
            connection.request("GET", '/' + self.file)
            receive_time = time.time()
        except ConnectionRefusedError:
            print("Connection refused\n")
            return
        
        # Socket details before response
        socketType  = connection.sock.type
        socketProtocol = connection.sock.proto
        socketFamily = connection.sock.family
        peerName = connection.sock.getpeername()
        
        # Trying to get server response 
        try:
            response = connection.getresponse()
        except:
            print("Unable to connect\n")
            return
        print(">>> Connection Received <<<\n")
       
        # Print http status code
        if response.code == 200:
            print('HTTP/1.1 200 OK\n')
        elif response.code == 404:
            print('HTTP/1.1 404 Not Found\n')
            
        # Print file content
        print(response.read().decode('utf-8') + '\n')
            
        # Print host parameters
        print("RTT: %s\n" % str(receive_time - request_time) +
              "Host Name: %s\n" % connection.host +
              "Socket Family: " + str(socketFamily) + '\n' +
              "Socket Type: " + str(socketType) + '\n' +
              "Socket Protocol: " + str(socketProtocol) + '\n' +
              "Peer Name: " + str(peerName) + '\n' )
        print(">>> Connection Closed <<<\n")
        connection.close()

if __name__ == '__main__':
    clientVar = init_value_client("127.0.0.1",8080,"sample.txt")
    clientVar.initiation()
    
    client = HttpClient(clientVar.HOST, clientVar.PORT, clientVar.FILE)
    client.make_request()
