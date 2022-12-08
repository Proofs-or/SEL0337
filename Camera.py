from picamera import PiCamera, Color

#--Configurações da Camera--#


camera.resolution = (1920, 1080)
camera.framerate = 15


#----#

def text:
    camera.annotate_background = Color('blue')
    camera.annotate_foreground = Color('red')
    camera.annotate_text = "9066 Group"


camera.start_preview()
text()
sleep(5)
camera.capture('/home/pi/Desktop/9066.jpg')
camera.stop_preview()