from colorTracking_v3 import *
from math import *
from adafruit_servokit import ServoKit
import time
import signal

pca = ServoKit(channels=16)
top_servo = pca.servo[4]
bl_servo = pca.servo[5]
br_servo = pca.servo[6]

kp = 1
kd = 0
ki = 0

def handler(signum, frame):
    print("Terminating program. Stopping servos")
    top_servo.angle = None
    bl_servo.angle = None
    br_servo.angle = None
    exit(1)

#def pxs_to_deg(x):
#    step_size = 90/240
#    return step_size * x

def top_px_to_deg(x):
    step_size = 180/480
    return 180 - step_size * x
#sdfcgvbhnjmesxrctfvgybhunjimko,l.w4sexcrvtbynhmjiko,l.;/edrfcvgbhnp-[oiukyjtgfhdwzqaxsdcftvgybhunyjimko,lp.o[;/xerctvftygbyhunujimoik,pol.;;;;jnmbnyrfctvysex4rzxwe4crtvfygbhunjimoik,pol.[p;/'t76uyghjfvb68yiughjkb80ui[o;jlmnzxwsdrrfctgvybuhynijmoik,pol.[;]]]]]
def br_px_to_deg(x):
    if(x < 240):
        return 90
    else:
        step_size = 180/480
        return 180 - step_size * x

def bl_px_to_deg(x):
    if(x > 240):
        return 90
    else:
        step_size = 180/480
        return step_size * x      

signal.signal(signal.SIGINT,handler)
while(1):
    x, y = get_coordinates()
    print(f"Coordinate are: {x}\t {y}")
    #print(abs(pxs_to_deg(x)))
    top_servo.angle = int(abs(top_px_to_deg(y)))
    bl_servo.angle = int(abs(br_px_to_deg(x)))
    br_servo.angle = int(abs(bl_px_to_deg(x)))
    #print(top_servo.angle)
    #time.sleep(0.25)
