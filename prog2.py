'''
Adriana Frias
A program that displays the height and distace of a projectile at any given moment
at any given time for any given takeoff (in degrees) and at any given velocity.
'''

#IMPORT sine AND cosine EQUATIONS
import math

# nested input for angle, second and velocity

angle = 0
velocity = 0
seconds = 0




while userInput:


    try:
        angle = float(input('Enter angle (in degrees): '))
        continue
    except ValueError:
        print('Please enter a valid character.')
        break

    try:
        velocity = float(input('Enter the velocity (in meters): '))
        continue
    except ValueError:
        print('Please enter a valid character.')
        break

    try:
        seconds = float(input('Enter seconds in decimal form (ex 1.00): '))
    except ValueError:
        print('Please enter a valid character.')



'''
Python reads line by line, in descending order/top to bottom. At least, that's how it works here. So
in order to properly run this program, referenced variables like "Pi", "radians", and "gravity_constant",
must be defined before execution or referencing later on.
'''

# calculate gravity constant
gravity_constant = 9.8*seconds

# equation for radians
radians = angle*math.pi/180.0

# equation for distance
distance = velocity*math.cos(radians)*seconds

# calculate velocity factor
velocity_factor = velocity*math.sin(radians)*seconds

# equation for height
height = -0.5*gravity_constant*seconds**2+velocity_factor



# print f statement
print(f'After {seconds} seconds, the projectile is at (in meters): \nHeight: {height:.2f} \nDistance: {distance:.2f}')
