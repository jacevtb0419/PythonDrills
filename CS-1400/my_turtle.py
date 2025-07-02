'''
Section 1) Documentation

This program generates a drawing of _____A Share a Coke with Christer Bottle_______________________
______________________________________________________________________________.

I have neither given nor received unauthorized assistance on this assignment.
Signed: ____Christer Cunow__________________
'''

# Section 2) Set-up
# Import the turtle library
import turtle
# Setup the graphics window

turtle.setup(1000, 1000, None, None)
turtle.title("Share a Coke with Christer")
turtle.reset()
turtle.shape('turtle')
turtle.penup()
# Section 3) Drawing
# Your code goes here


#Set base line
turtle.goto(-100, -400)
print("Corner 1", turtle.position())
turtle.pendown()
turtle.color('black')
turtle.setx(100)
print("Corner 2", turtle.position())

#Draw right side
turtle.circle(50, 90)
turtle.circle(90, 50)
turtle.circle(-60, 100)
turtle.circle(50, 20)
turtle.circle(70, 20)
turtle.circle(1000, 20)
turtle.circle(80, 20)
turtle.circle(80, 20)
turtle.circle(80, 20)
turtle.circle(-80, 80)
print("Corner 3", turtle.position())

#turn 90 degrees and draw for bottle cap
turtle.seth(90)
turtle.fd(30)

#Finish bottle Cap
turtle.setheading(180)
turtle.fd(70)
turtle.pu()
#end right side

#go to starting point
turtle.goto(-100, -400)
turtle.setheading(180)
turtle.pd()

#left side
turtle.circle(-50, 90)
turtle.circle(-90, 50)
turtle.circle(60, 100)
turtle.circle(-50, 20)
turtle.circle(-70, 20)
turtle.circle(-1000, 20)
turtle.circle(-80, 20)
turtle.circle(-80, 20)
turtle.circle(-80, 20)
turtle.circle(80, 80)
print("Corner 4", turtle.position())

#vertical for bottle cap
turtle.seth(90)
turtle.fd(30)

#Center for name
turtle.pu()
turtle.home()
turtle.pd()
turtle.write("Christer", False, align="center", font=("Spencerian script", 24, "normal"))
turtle.pu()

#hide turtle
turtle.goto(-1000, 1000)
# Section 4) Wrap-up
# Tell the Turtle to stop accepting commands
turtle.done()
turtle.bye()
