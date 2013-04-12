# Polygon excercise from Week 0

# Name: Brian Yee

from math import pi
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
def polygon(t, l, n):
    angle = 360./n
    for sides in range(n):
        drawSide(t, l, angle)

def circle(t, r):
    circumference = 2*pi*r
    n = r / 2
    l = circumference / n
    polygon(t, l, n)

def arc(t, r, theta):
    circumference = 2*pi*r
    n = r / 2
    l = circumference / n
    angle = 360. / n
    for sides in range(int(theta/angle)):
        drawSide(t, l, angle)

def drawSide(t, l, angle):
    fd(t, l)
    rt(t, angle)

#polygon(bob, 100, 10)
#circle(bob, 100)
#arc(bob, 100, 90)



wait_for_user()					
