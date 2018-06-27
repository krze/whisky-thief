import os
from security_camera import SecurityCamera
from send_this import EmailSender

camera = SecurityCamera()
sender = EmailSender()
files = camera.capture()

sender.send_files(files)

for file in files:
    if os.path.isfile(file):
        os.remove(file)
    