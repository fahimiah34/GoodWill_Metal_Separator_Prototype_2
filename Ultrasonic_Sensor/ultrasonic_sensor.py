from gpiozero import DistanceSensor
import time

ultrasonic = DistanceSensor(echo=19, trigger=26)

while True:
    print(ultrasonic.distance) #prints the distance in m
    time.sleep(0.25)
