# Flower excercise (4.2) from Week 0

# Name: Brian Yee

from sib_polygon import arc
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
def drawFlower(t, r, theta, petals):
    for petal in range(petals):
        drawPetal(t, r, theta)
        lt(t, 360./petals)

def drawPetal(t, r, theta):
    for i in range(2):
        arc(t, r, theta)
        rt(t, 180-theta)
    
#drawPetal(bob, 100, 45)
#drawFlower(bob, 60., 60., 7)
#drawFlower(bob, 60., 80., 10)
#drawFlower(bob, 150., 30., 20)



wait_for_user()					

