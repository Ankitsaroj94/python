import socket
import pickle
from PIL import Image
import io

HOST = '127.0.0.1'  # Use the appropriate IP here
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = b""
            while True:
                packet = conn.recv(4096)
                if not packet: break
                data += packet
            try:
                image = Image.open(io.BytesIO(data))
                image.show()
            except Exception as e:
                print("Error receiving data:", e)
