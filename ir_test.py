# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example shows using two TSL2491 light sensors attached to TCA9548A channels 0 and 1.
# Use with other I2C sensors would be similar.
import time
import board
import adafruit_mlx90614
import adafruit_tca9548a

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)


if __name__ == '__main__':
    # For each sensor, create it using the TCA9548A channel instead of the I2C object
    mlx0 = adafruit_mlx90614.MLX90614(tca[0])
    mlx1 = adafruit_mlx90614.MLX90614(tca[1])
    mlx2 = adafruit_mlx90614.MLX90614(tca[2])
    mlx3 = adafruit_mlx90614.MLX90614(tca[3])
    mlx4 = adafruit_mlx90614.MLX90614(tca[4])
    mlx5 = adafruit_mlx90614.MLX90614(tca[5])
    mlx6 = adafruit_mlx90614.MLX90614(tca[6])
    mlx7 = adafruit_mlx90614.MLX90614(tca[7])


    irs = ["IR0", "IR1", "IR2", "IR3", "IR4", "IR5", "IR6", "IR7"]

    # Print the header once
    print("IR Sensors")
    print("------------------------------------------------------------------")
    print(''.join(f'{label:<8}' for label in irs))  # Each label is left-justified in 8-character width

    try:
        # After initial setup, can just use sensors as normal.
        while True:
            temp0 = mlx0.ambient_temperature
            temp1 = mlx1.ambient_temperature
            temp2 = mlx2.ambient_temperature
            temp3 = mlx3.ambient_temperature
            temp4 = mlx4.ambient_temperature
            temp5 = mlx5.ambient_temperature
            temp6 = mlx6.ambient_temperature
            temp7 = mlx7.ambient_temperature
            
            temps = [temp0, temp1, temp2, temp3, temp4, temp5, temp6, temp7]
            print(''.join(f'{temp:<8.2f}' for temp in temps))  # Each temp is formatted to 2 decimal places
            
            time.sleep(0.1)
            temps = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    except KeyboardInterrupt: 
        print("Code stopped")


