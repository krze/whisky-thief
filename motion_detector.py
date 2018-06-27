import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    while True:
        inputGPIO = GPIO.input(4)
        print(str(inputGPIO))
        if inputGPIO:
            print("Motion Detected...")
            
            time.sleep(1) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()