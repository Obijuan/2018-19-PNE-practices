# SEQ Server
from Seq import Seq
import socket


# List of operations for the server
LEN = "len"   # Return the sequence's length
COUNT = "count"  # Count the number of a specific base
PERC = "perc"  # Calculate the percentage of a specific base


def valid_strbase(strbase):
    """Check if a received string is correct or not
    Only is considered correct if it only contains the characters A, T, C or G"""
    for b in strbase:
        if b not in {'A', 'C', 'T', 'G', 'a', 'c', 't', 'g'}:
            return False

    return True


def process_client(cs):
    """This function is called everytime there is a new client to attend
       cs: Socket for communicating with the client
    """

    # Read the request message. The request is a string
    msg = cs.recv(2048).decode("utf-8")

    print("Message received: {}".format(msg))

    # -- Split the request into the commands
    cmds = msg.split('\n')

    print("Hello")

    # -- If the first line is blanck, it means the request is a check
    if cmds[0] == "":
        print("Response: READY!")
        response_msg = "Server READY!"
        response = str.encode(response_msg)
        cs.send(response)
        cs.close()
        return

    # If the first line is not black, it should contain the sequence
    strbase = cmds[0].upper()

    # Check if the string is valid or not
    if not valid_strbase(strbase):
        # The string is not valid
        print("Response: ERROR!!!!")
        response_msg = "ERROR: Sequence not valid"
        response = str.encode(response_msg)
        cs.send(response)
        cs.close()

    # Create the sequence object
    print("Sequence received: {}".format(strbase))
    seq = Seq(strbase)

    response_msg = "OK\n"

    # Process the requested operation
    for cmd in cmds[1:]:
        print("Cmd: {}".format(cmd))
        if cmd == LEN:
            response_msg += str(seq.len()) + '\n'
        elif cmd[0:5] == COUNT:
            base = cmd[5]
            response_msg += str(seq.count(base)) + '\n'
        elif cmd[0:4] == PERC:
            base = cmd[4]
            response_msg += str(seq.count(base)) + '\n'

    print("Generated response: {}".format(response_msg))
    response = str.encode(response_msg)
    cs.send(response)
    cs.close()


# ------- Main program
# Configure the Server's IP and PORT
PORT = 8085
IP = "192.168.1.36"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Increase the connection counter
    number_con += 1

    # Connection received. A new socket is returned for communicating with the client
    print("#{}. Attending connections from client: {}".format(number_con, address))

    # Process the client
    process_client(clientsocket)
