
Computer Networks CSE 4344/5344
Project 1
Simple Web Server & Client
Assignment Submitted by: Nudrat Nawal Saber
UTA ID: 1001733394




Environment Requirement:
---------------------------------
Python (Version >= 2.7)
Microsoft Visual Studio


 Steps for the Compilation of the Code: 
------------------------------------------------

Run:

Command to run server.py :    python server.py <port_number>

i)If <port_number> is not given, 8080 will be used.

 
Command to run client.py:     python client.py <server_address/name> <port_number> <file_name>

i)If <server_address/name> is not given, '127.0.0.1' will be used. Accecptable values are either 'localhost' or '127.0.0.1' .
ii)If <port_number> is not given, 8080 will be used.
iii)If <file_name> is not specified, default (sample.txt) file will be used.


N.B. : 
1.Arguments should be given in order, for example providing only <server_address/name> and <file_name> will not work. 
2.It is only allowed to omit from the back, for example providing <server_address/name> and <port_number> is acceptable.


References & Citations:
------------------------------
*https://www.programcreek.com/python/example/1816/SocketServer.ThreadingMixIn
*https://docs.python.org/3/library/http.server.html
*https://realpython.com/working-with-files-in-python/#filename-pattern-matching-using-glob
*Book: Computer Networking. A Top Down Approach. Fifth Edition by James F. Kurose, Keith W. Ross. Chapter 2.