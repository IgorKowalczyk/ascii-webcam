import cv2
from PIL import Image
import time

char = [' ', '.', ':', '-', '=', '+', '#', '%', '@']

def ascii(img, width=-1):
    img = img.resize((int(img.size[0]), int(img.size[1] * (7/11))))
    if width != -1:
        ratio = width / img.size[0]
        img = img.resize((int(img.size[0]*ratio), int(img.size[1]*ratio)))
    width, height = img.size
    text = ''
    for y in range(height):
        line = ''
        for x in range(width):
            pixel = img.getpixel((x, y))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            vid = int((red+blue+green)/3)
            line += char[int(vid*len(char)/255) % len(char)]
        text += line + '\n'
    return text

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if not ret:
        print("Error! Failed to run camera!")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    print(ascii(img, 100))
    time.sleep(.02)
cam.release()
