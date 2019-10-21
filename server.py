import cv2
import socket
import numpy as np

PORT = 10020

s = socket.socket()
host = "0.0.0.0"
s.bind((host, PORT))
s.listen()
print("Server Listening...")

while True:
    conn, addr = s.accept()
    print("Connection from " + str(addr))
    img_str = conn.recv(1024000)
    nparr = np.frombuffer(img_str, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("Test", img)
    cv2.waitKey()

