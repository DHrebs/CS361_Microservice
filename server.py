import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 4444  # Port to listen on (non-privileged ports are > 1023)

"""
This is the main microservice. It will receive a message from the main program. The message will be passed to the back end and then
it will receive the response from the back end and pass that to the main program. This is very rough pseudocode and I will probably
break it up into multiple classes instead of having very long methods like below. This is just to give a rough outline of the plan.

# Initialize class for the server
class Server:
    def __init__(self):
        # set up class parameters here
        self.message = None

    # Listen for incoming connections
    def receiveHostMessage():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received {data!r}")
                # Store received data as a message
                self.message = data
                # Send Data to back end
                newData = sendDatabaseMessage(self.message)
                # Send new data back to client
                s.sendall(newData)
                s.close()

    # Send received data to the Server
    def sendDatabaseMessage(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"Sending {message!r}")
            s.sendall(message)
            # receive the respinse
            data = s.recv(1024)
            s.close()
            return data

"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received {data!r}")
