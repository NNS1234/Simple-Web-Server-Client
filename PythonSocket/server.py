#Assignment Submitted by: Nudrat Nawal Saber
#UTA ID: 1001733394
#https: // www.programcreek.com/python/example/1816/SocketServer.ThreadingMixIn
#https: // docs.python.org/3/library/http.server.html


import sys
import os
import threading
from http.server import * 
from socketserver import *
import urllib.parse
import glob

# Checks validity of port number
def check_port_number(port):
    return port.isdigit()

class init_value_server():
    def __init__(self, host_name, port_number, file_name):
        self.HOST = host_name
        self.PORT = port_number
        self.DEFAULT_FILE = file_name
     # Parsing user arguments and checking validity
    def initiation(self):
        
        # User provided port number
        if len(sys.argv) > 2:
            print("Too many arguments provided. Default values are being used.\n")
        elif len(sys.argv) == 2: 
            # Checking validity of port number
            if check_port_number(sys.argv[1])==False:
                print("Invalid port number. Using port 8080\n")
            self.PORT = int(sys.argv[1])
        else:
            print("No port number provided. Using port 8080\n")

    # Searching for user's desired file       
    def file_exists(filename):
        # If the filename is '/'
        if filename == '/':
            return init_value_server.DEFAULT_FILE
        
        # Checking validity of path
        else:
            # Search file pattern
            paths = glob.glob("." + filename)
            # Invalid path as no file found
            if paths == None:
                return None

            # Seaching for folder or file
            else:
                for name in paths:
                    # File found
                    if os.path.isfile(name):
                        return name
                # No file found
                return None

# Client request handling

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
                
        print(">>> Connection Received <<<\n")
        print("Client IP Address: " + self.address_string() +
              "\nClient Port Number: " + str(self.client_address[1]) +
              "\nSocket Family: " + str(self.connection.family) +
              "\nSocket Type: " + str(self.connection.type) +
              "\nSocket Protocol: " + str(self.connection.proto) +
              "\nSocket Address: " + str(self.connection.getsockname()) +
              "\nClient Peername: " + str(self.connection.getpeername()) + '\n')
        
        filepath = init_value_server.file_exists(self.path)
        # File doesn't exists
        if filepath is None:
            # 404 Error
            self.send_response(404)
            self.end_headers()

        # File exists
        else:
            # 202 OK
            self.send_response(200)
            self.end_headers()
            with open(filepath, 'rb') as fUploadFile:
                uploadFile = fUploadFile.read()
                self.wfile.write(uploadFile)
        print("\n>>> Client Request Completed <<<\n") 
        print("----------------------------------")
        return

# Multi-threading
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    serverVar = init_value_server("127.0.0.1",8080,"sample.txt")
    serverVar.initiation()
    try:
        httpServer = ThreadedHTTPServer((serverVar.HOST, serverVar.PORT), RequestHandler)
        print('Server started !\n')
        httpServer.serve_forever() # Always looking for request untill terminated

    # Terminated by keyboard command
    except KeyboardInterrupt:
        httpServer.server_close()
