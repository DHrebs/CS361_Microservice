import socket
import pickle

HOST = "127.0.0.1"
FRONT_END_PORT = 4444
BACK_END_PORT = 5555

# Send received data to the Server
def sendDatabaseMessage(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, BACK_END_PORT))
        print(f"Sending {message!r}")
        s.sendall(message)
        # receive the respinse
        data = s.recv(1024)
        return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, FRONT_END_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received {data!r}. Sending to back end...")
            newData = sendDatabaseMessage(data)
            print(f"Received {pickle.loads(newData)!r}. Sending to front end")
            conn.sendall(newData)