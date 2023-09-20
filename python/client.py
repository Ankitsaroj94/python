import socket
import pyautogui
import io
import pickle

HOST = '127.0.0.1'  # The server's IP
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        screenshot = pyautogui.screenshot()
        bytes_io = io.BytesIO()
        screenshot.save(bytes_io, format='PNG')
        s.sendall(bytes_io.getvalue())

