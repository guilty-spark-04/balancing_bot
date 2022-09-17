from colorTracking_v3 import *
from adafruit_servokit import ServoKit

pca = ServoKit(channels=16)
servo1 = pca.servo[0]
servo2 = pca.servo[1]
servo3 = pca.servo[2]


while(1):
    x, y = get_coordinates()
    if(x > 0):
        servo1.angle = 180
    elif(x<0): servo1.angle = 0
    if(y >0):
        servo2.angle = 180
    elif(y<0):servo2.angle = 0