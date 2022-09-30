from colorTracking_v3 import *
from math import *
from adafruit_servokit import ServoKit
import time
pca = ServoKit(channels=16)
servo1 = pca.servo[0]
servo2 = pca.servo[1]
servo3 = pca.servo[2]

def pxs_to_deg(x):
    step_size = 90/240
    return step_size * x

while(1):
    x, y = get_coordinates()
    print(f"Coordinate are: {x}\t {y}")
    print(abs(pxs_to_deg(x)))
    servo1.angle = int(abs(pxs_to_deg(x)))
    time.sleep(0.25)
