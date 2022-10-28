from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pinkUpper = (200,240,229)
pinkLower = (3,160,107)

pts = deque(maxlen=args["buffer"])
counter = 0


vs = cv2.VideoCapture(0)

time.sleep(2.0) #why is the sleep here so... long??

def get_coordinates():
	x = 0
	y = 0
	_, frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
	if frame is None:
		return 0 ,0
	frame = frame[0:480,0:480]
	width = 480
	height = 480

	blurred = cv2.GaussianBlur(frame, (11, 11),0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)							
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		if radius > 10:
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			pts.appendleft(center)
			cv2.putText(frame, "x: {}, y: {}".format(round(x)-width/2, (-1*(round(y)-height/2))),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
	else:
		x_coord = 0
		y_coord = 0
	x_coord = width - round(x)
	y_coord = (-1*(round(y)-height))
	cv2.line(frame, (240,0), (240,480), (0, 0, 255), 1)
	cv2.line(frame, (0,240), (480,240), (0, 0, 255), 1)
	#cv2.imshow("Frame", frame)
	#cv2.imshow("Mask", mask)		#Display mask window
	#key = cv2.waitKey(1) & 0xFF
	#counter += 1
	return x_coord, y_coord
# if not args.get("video", False):
# 	vs.stop()
# else:
# 	vs.release()
# cv2.destroyAllWindows()

if __name__ == "__main__":
	while(True):
		x = 0
		y = 0
		_, frame = vs.read()
		frame = frame[1] if args.get("video", False) else frame
		if frame is None:
			continue
		frame = frame[0:480,0:480]
		width = 480
		height = 480

		blurred = cv2.GaussianBlur(frame, (11, 11),0)
		hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv, greenLower, greenUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		center = None
		if len(cnts) > 0:
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)							
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			if radius > 10:
				cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
				pts.appendleft(center)
				cv2.putText(mask, "x: {}, y: {}".format(round(x)-width/2, (-1*(round(y)-height/2))),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
		else:
			x_coord = 0
			y_coord = 0
		x_coord = round(x)-width/2
		y_coord = (-1*(round(y)-height/2))
		cv2.line(frame, (240,0), (240,480), (0, 0, 255), 1)
		cv2.line(frame, (0,240), (480,240), (0, 0, 255), 1)
		#cv2.imshow("Frame", frame)
		cv2.imshow("Mask", mask)		#Display mask window
		key = cv2.waitKey(1) & 0xFF
		#counter += 1
	# if not args.get("video", False):
	# 	vs.stop()
	# else:
	# 	vs.release()
	# cv2.destroyAllWindows()