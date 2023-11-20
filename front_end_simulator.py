import socket
import pickle

HOST = "127.0.0.1"
PORT = 4444
message = b"European Silver Fir"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Sending {message!r}")
    s.sendall(message)
    newData = s.recv(1024)
    result = pickle.loads(newData)
    for key in result:
        print(key + ": " + result[key])