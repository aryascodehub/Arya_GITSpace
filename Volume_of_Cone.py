# VOLUME OF A CONE:πr2h

import math

userRadius = float(input("Enter a radius "))
userHeight = float(input("Enter a height for the cone"))
pi = 3.14

myPi = math.pi
formula = myPi * userRadius ** 2 * (userHeight / 3)
print("The volume of your cone is" + str(formula))


