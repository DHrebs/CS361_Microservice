import socket
import requests
import json
from dotenv import load_dotenv
import os

LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = 4444

def configure():
    load_dotenv()

def getPlantCare(plantName):
    request = requests.Session()
    url = f"https://perenual.com/api/species-care-guide-list?key={os.getenv('api_key')}&q={plantName}"
    r = request.get(url)
    return r.json()

def getDataFromJSON(JSONData):
    data = JSONData['data']
    if len(data) == 0:
        return {"Error": "No Result Found"}
    #for i in range(len(data)):
        #print(data[i])
    newData = {"Common Name":data[0]['common_name'], "Scientific Name":data[0]["scientific_name"][0], "Water Needs":data[0]['section'][0]['description'], "Light Needs":data[0]['section'][1]['description'] }
    return newData
    
def receiveData():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((LISTEN_HOST, LISTEN_PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received {data!r}. Sending to back end...")
                stringData = data.decode()
                plantCare = getPlantCare(stringData)
                result = json.dumps(getDataFromJSON(plantCare))
                print(f"Received {result!r}. Sending to front end")
                conn.sendall(result.encode())

def main():
    configure()
    receiveData()

main()