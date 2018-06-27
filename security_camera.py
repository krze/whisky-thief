from picamera import PiCamera
from time import sleep
import datetime

# Camera for capturing
class SecurityCamera:
    camera = PiCamera()
    
    # Captures 3 pictures in the "security" folder on desktop
    def capture(self):
        file_names = []
        now = datetime.datetime.now()

        for i in range(0,3):
            name = str(now) + '_' + str(i) + '.jpg'
            file_names.append(name)

        for file_name in file_names:
            self.camera.start_preview()
            sleep(2)
            self.camera.capture(file_name)
            self.camera.stop_preview()
        
        return file_names
        
##hx = HX711(5, 6)
##hx.set_reading_format("LSB", "MSB")
##hx.set_reference_unit(92)
##hx.reset()
##hx.tare()
