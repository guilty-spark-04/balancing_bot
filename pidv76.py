from colorTracking_v3 import *
from math import *
from adafruit_servokit import ServoKit
from simple_pid import PID
import time
import signal
import csv

pca = ServoKit(channels=16)
y_servo = pca.servo[4]
x_servo = pca.servo[6]
pidx = PID(0.9, 0.5, 0.5, setpoint=240)
pidy = PID(0.9, 0.5, 0.5, setpoint=240)
PID.output_limits = (-480, 480)

timer = 0

def handler(signum, frame):
    print("Terminating program. Stopping servos")
    y_servo.angle = 85
    x_servo.angle = 85
    #br_servo.angle = 90

    y_servo.angle = None
    x_servo.angle = None
    #br_servo.angle = None

    exit(1)

#def pxs_to_deg(x):
#    step_size = 90/240
#    return step_size * x

HARD_LIMIT = 10

def top_px_to_deg(x):
    step_size = HARD_LIMIT/480
    return 85 - step_size * (240-x)

def PID_controlx(x):
    if (220<x<260):
        return 85
    else:
        PID_cal = pidx(x)
        step_size = HARD_LIMIT/480
        return 85 - step_size * PID_cal
def PID_controly(x):
    if (220<x<260):
        return 85
    else:
        PID_cal = pidy(x)
        step_size = HARD_LIMIT/480
        return 85 - step_size * PID_cal
    #theoretically
    #p_control = error * kp
    #accumError += error * ki
    #d_control = (prev_error - error) * kd
    #pid_out = p_control + accumError + d_control
    #convert pid_out to an angular value
#    if(x > 240):
#        step_size = HARD_LIMIT/480
#        return 90 + step_size*(240-x)
#    else:
#        step_size = HARD_LIMIT/480
#        return 90 - step_size * (240-x)

def bl_px_to_deg(x):
        step_size = HARD_LIMIT/480
        return 85 - step_size*(240-x)    

signal.signal(signal.SIGINT,handler)

while(1):
    x, y = get_coordinates()
    print(f"Coordinate are: {PID_controlx(x)}\t {PID_controly(y)}")
    #print(abs(pxs_to_deg(x)))
#     y_servo.angle = int(abs(top_px_to_deg(y)))
    y_servo.angle = int(abs(PID_controly(y)))
#     x_servo.angle = int(abs(bl_px_to_deg(x)))
    x_servo.angle = int(abs(PID_controlx(x)))
    #print(top_servo.angle)
    #time.sleep(0.25)
