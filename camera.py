from picamera import PiCamera
from time import sleep

from gpiozero import LED, Button

from signal import pause
import datetime

sayCheese = Button(5)

camera - PiCamera()

def takePicture():
	timestamp = datetime.datetime.now().isoformat()
	camera.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	camera.start_preview()
	sleep(3)
	camera.capture('/home/pi/Desktop/capture-%s.jpg' % timestamp)

sayCheese.when_pressed = takePicture;


pause()
