
#This program asks the user if they want to take a video or a photo and it does so accordingly
#I built this on a rasberry pi 4 

#imports libraries
from picamera import PiCamera
import time as t




#setting up the camera
camera = PiCamera()
camera.resolution = (640, 480)

#asks the user if they want a video or photo
g = input("Video or photo??[v/p]: ")

#if the answer is = v it will start taking a video and put it into a folder
if g == "v":
    r = "recording start"
    camera.start_preview()
    t.sleep(2)
    print("recording start")
    camera.start_recording("my_movie.h264")
    t.sleep(8)
    print("recording stopped")
    camera.stop_recording()
    exit()
#if the user wants a picture it will take one and save it.
else:
    camera.start_preview()
    print("your photo will be taken soon")
    t.sleep(4)
    camera.capture("your_photo.jpg")
    print("done")
    t.sleep(2)
    exit()
