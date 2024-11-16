import time
import RPi.GPIO as GPIO
from Proximity_Sensor.proximity_sensor import ProximitySensor # use the ProximitySensor class from proximity_sensor.py

if __name__ == '__main__':
    # set up proximity sensors
    prox1 = ProximitySensor(23) # initialize proximity sensor to work on GPIO 24
    prox2 = ProximitySensor(18) # initialize proximity sensor to work on GPIO 24
    prox3 = ProximitySensor(15) # initialize proximity sensor to work on GPIO 24
    prox4 = ProximitySensor(14) # initialize proximity sensor to work on GPIO 24
    prox5 = ProximitySensor(24) # initialize proximity sensor to work on GPIO 24
    prox6 = ProximitySensor(25) # initialize proximity sensor to work on GPIO 24
    prox7 = ProximitySensor(8) # initialize proximity sensor to work on GPIO 24
    prox8 = ProximitySensor(7) # initialize proximity sensor to work on GPIO 24
    prox9 = ProximitySensor(1) # initialize proximity sensor to work on GPIO 24
    prox10 = ProximitySensor(12) # initialize proximity sensor to work on GPIO 24
    prox11 = ProximitySensor(16) # initialize proximity sensor to work on GPIO 24

    proxSensors = [prox1, prox2, prox3, prox4, prox5, prox6, prox7, prox8, prox9, prox10, prox11] # array holding all proximity sensor variables
    detection = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # array to store if sensors detected metal 

    try:
        while True:
            # for i in range(len(proxSensors)):
            #     if (proxSensors[i]).is_object_detected():
            #         detection[i] = 1

            print(prox11.is_object_detected())

            time.sleep(0.5) # waits 0.5 seconds before loop restarts

    except KeyboardInterrupt: 
        print("\nCode stopped")

    finally: 
        prox1.cleanup()
        prox2.cleanup()
        prox3.cleanup()
        prox4.cleanup()
        prox5.cleanup()
        prox6.cleanup()
        prox7.cleanup()
        prox8.cleanup()
        prox9.cleanup()
        prox10.cleanup()
        prox11.cleanup()
