# CLASS FOR IR SENSOR #

import time
import board
import adafruit_mlx90614
import adafruit_tca9548a

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

class IRSensor:
    def __init__(self, sensor_pin):
        self.sensor = adafruit_mlx90614.MLX90614(tca[sensor_pin])

    def get_temp(self):
        return self.ambient_temperature
    
    def calibrate_ir(self):
        pass

    def object_detect_ir(self):
        pass
