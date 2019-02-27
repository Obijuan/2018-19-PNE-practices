import socket

# SERVER IP, PORT
IP = "192.168.1.36"
PORT = 8086

#while 1:
# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = """aaCTg
len
countA
countG
percA
"""

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode(msg))

# Read the server's response
#sresponse = s.recv(2048).decode("utf-8")

#print("Server's Response: {}".format(sresponse))

s.close()
