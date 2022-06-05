
#This program asks the user if they want to take a video or a photo and i does so accordingly
#I built this on a rasberry pi 4 


from picamera import PiCamera
import time as t





camera = PiCamera()
camera.resolution = (640, 480)


g = input("Video or photo??[v/p]: ")

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
else:
    camera.start_preview()
    print("your photo will be taken soon")
    t.sleep(4)
    camera.capture("your_photo.jpg")
    print("done")
    t.sleep(2)
    exit()
