from gpiozero import DigitalInputDevice
import time

class ProximitySensor:
    def __init__(self, sensor_pin):
        self.sensor = DigitalInputDevice(sensor_pin)

    def is_object_detected(self):
        return self.sensor.value == 1

    def cleanup(self):
        self.sensor.close()  # gpiozero handles cleanup automatically, but providing for explicit control
