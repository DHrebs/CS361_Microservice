import socket
import pickle

HOST = "127.0.0.1"
PORT = 5555

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
            newData = pickle.dumps({"Name":"Chrysanthemum", "Scientific Name":"Chrysanthemum indicum", "Care Instructions":"Chrysanthemums are susceptible to aphids and mildew, so keeping plants dry is a priority. Mums need plenty of air circulation and water drainage. Space 18 to 30 inches apart for best results. When plants are six inches tall, pinch about 3/4 of an inch from each branch to promote more blooms and bushier plants"})
            conn.sendall(newData)