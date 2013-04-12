# Hello excercise from Week 0

# Name: Brian Yee


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
def drawHello(t):
    lt(t, 90)
    fd(t, 100)
    bk(t, 50)
    rt(t, 90)
    fd(t, 50)
    lt(t, 90)
    fd(t, 50)
    bk(t, 100)
    pu(t)
    rt(t, 90)
    fd(t, 20)
    pd(t)
    fd(t, 50)
    bk(t, 50)
    lt(t, 90)
    fd(t, 50)
    rt(t, 90)
    fd(t, 25)
    bk(t, 25)
    lt(t, 90)
    fd(t, 50)
    rt(t, 90)
    fd(t, 50)
    pu(t)
    fd(t, 25)
    pd(t)
    rt(t, 90)
    fd(t, 100)
    lt(t, 90)
    fd(t, 50)
    pu(t)
    fd(t, 25)
    pd(t)
    fd(t, 50)
    bk(t, 50)
    lt(t, 90)
    fd(t, 100)
    rt(t, 90)
    pu(t)
    fd(t, 75)
    pd(t)
    fd(t, 50)
    rt(t, 90)
    fd(t, 100)
    rt(t, 90)
    fd(t, 50)
    rt(t, 90)
    fd(t, 100)

drawHello(bob)





wait_for_user()					
