from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

#camera preview for 5 second, then takes picture
camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('pipic.jpg')
camera.stop_preview()



