import cv2
import socket

PORT = 10020

s = socket.socket()
host = "0.0.0.0"
s.connect((host, PORT))
img = cv2.imread("image.jpg")
img_str = cv2.imencode('.jpg', img)[1].tostring()
s.send(img_str)
s.close()
