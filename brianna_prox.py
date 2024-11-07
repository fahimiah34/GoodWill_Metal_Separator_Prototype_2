from gpiozero import InputDevice
import time

sensor = InputDevice(23, pull_up=True)
try:
    while True:
        print(sensor.value)
        time.sleep(0.5)

except KeyboardInterrupt:
    sensor.close()
