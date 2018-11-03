import io
import time
from PIL import Image
from picamera import PiCamera


class Camera:
    def __init__(self, img_width=128, img_height=96, img_rot=0, img_iso=1200):
        self.value = None
        self.img_width = img_width
        self.img_height = img_height
        self.img_rot = img_rot
        self.img_iso = img_iso
        self.init_camera()

    def init_camera(self):
        self.camera = PiCamera()
        self.camera.iso = self.img_iso
        self.camera.rotation = self.img_rot
        self.camera.resolution = (self.img_width, self.img_height)
        time.sleep(2)  # Camera warm-up time
        self.camera.start_preview()

    def get_value(self):
        return self.value

    def update(self):
        self.sensor_get_value()
        return self.value

    def reset(self):
        self.value = None

    def sensor_get_value(self):
        stream = io.BytesIO()
        self.camera.capture(stream, format='jpeg')
        stream.seek(0)  # "Rewind" the stream to the beginning so we can read its content
        self.value = Image.open(stream)
