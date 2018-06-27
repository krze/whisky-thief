from security_camera import SecurityCamera
from send_this import EmailSender

#camera = SecurityCamera()
#camera.capture()

files = ['test.jpg', 'test2.jpg', 'test3.jpg']
sender = EmailSender()

sender.send_files(files)
