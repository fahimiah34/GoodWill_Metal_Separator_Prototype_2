# CLASS FOR PROXIMITY SENSOR #

from gpiozero import InputDevice
import time

class ProximitySensor:
    def __init__(self, sensor_pin):
        self.sensor = InputDevice(sensor_pin, pull_up = False)

    def is_object_detected(self):
        return self.sensor.value == 1

    def cleanup(self):
        self.sensor.close()  # gpiozero handles cleanup automatically, but providing for explicit control
