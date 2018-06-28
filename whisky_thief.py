import os
from security_camera import SecurityCamera
from send_this import EmailSender

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) #PIR
camera = SecurityCamera()
sender = EmailSender()

try:
    time.sleep(2) # to stabilize sensor
    while True:
        inputGPIO = GPIO.input(4)
        print(str(inputGPIO))
        
        if inputGPIO:
            print("ENEMY SPOTTED!!")
            files = camera.capture()
            sender.send_files(files)
            
            print("Files sent. Cleaning up.")
            
            # Deletes files from the local dir
            for file in files:
                if os.path.isfile(file):
                    os.remove(file)
            
            print("All clean.")
            
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()





    