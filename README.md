# balancing_bot
Final Project for Control Systems class by Allison DeWeese, Carlos Espinal, Stefanus Komala-Noor, Lauren Kerno, and Long Vu
# What is it?
A device that balances an object on a plate.
# What does it do?
This robot consists of a plate that is controlled by two rods connecting to two servo motors. These rods will control the position of the plate so that the plate will tilt at an angle opposite to the position of the object until the object stays at the center of the plate. To identify the position of the object, a camera will record the top view of the plate and track the object as it moves on the plate. The position of the object then translates into a specific rotation of each servo motor using a Proportional Integral Derivative [PID] control system. All the controlling and processing will be done using Raspberry Pi and the image processing will be analyzed using python's OpenCV library.
#Challenges we ran into
Various problems were encountered during the course of developing this project. One example is the hue saturation value. Once this value was found, rather than hard-coding a single color value, a range was used so that multiple objects of varying colors could be used. Another issue encountered is the delay from picking up the location of the ball to the change in orientation of the plate, which was mitigated by increasing the Kd value of the PID controller, which increased the rate of change for the plate.

While some problems were able to be mitigated through various means, there are some natural limitations that were encountered. One of these limitations is the type of motor used. A DC Brush motor would have more precise control of the plate's movement. Another limitation is the velocity of the ball, which is difficult to predict and control and affects the ability of the robot to get the ball to the center of the plate.

# What we learned
This project mainly helped reinforce the concepts of PID control that we learned during our Control Systems class. Through actual physcial application of a system, we were able to not only visually observe the effects each part of a PID controller had on the system itself, but we also learned how to tune it to get a response as close as what we expect to see. 
