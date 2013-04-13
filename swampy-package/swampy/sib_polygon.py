# Polygon excercise from Week 0

# Name: Brian Yee

from math import pi
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
def polygon(t, l, n):
    angle = 360./n
    drawSides(t, n, l, angle)

def circle(t, r):
    circumference = 2*pi*r
    n = r
    l = circumference / n
    polygon(t, l, n)

def arc(t, r, theta):
    circumference = 2*pi*r
    length = circumference*abs(theta)/360
    n = int(length/4)
    l = length / n
    angle = float(theta) / n
    drawSides(t, n, l, angle)

def drawSides(t, n, l, angle):
    for i in range(n):
        fd(t, l)
        rt(t, angle)

#polygon(bob, 100, 5)
#circle(bob, 100)
#arc(bob, 100, 90)



wait_for_user()					
