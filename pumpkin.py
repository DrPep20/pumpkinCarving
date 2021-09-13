import turtle as trtl
import math

# create turtle object and create screen object
painter = trtl.Turtle()
wn = trtl.Screen()
wn.title("Pumpkin Carving Time!")
wn.bgcolor("#0c1445")
painter.shape("turtle")
painter.pensize(2)

eye = wn.textinput("Eye Type: ", "Triangles or Circles? ")
mouth = wn.textinput("Mouth Type: ", "Do You Want Spooky or Friendly Pumpkin? ")
if mouth == "Friendly":  
    friendly = wn.textinput("Mouth Type: ", "No Teeth, One Tooth, Two Teeth")
elif mouth == "Spooky":
    spooky = wn.textinput("Mouth Type: ", "Half Spiked, Full Spiked, Vampire")

def penMove(x,y):
    painter.penup()
    painter.goto(x,y)
    painter.pendown()

def square(x):
    for i in range(4):
        painter.forward(x)
        painter.left(90)

def colorTriangle(s):
    painter.seth(0)
    painter.begin_fill()
    for i in range(3):
        painter.forward(s)
        painter.left(120)
    painter.end_fill()

def invertedTriangle(s):
    painter.seth(0)
    for i in range(3):
        painter.forward(s)
        painter.right(120)

def oval(radius):
    painter.seth(-45)
    for i in range(2):
        painter.circle(radius,90)
        painter.circle(radius//2, 90)
    painter.seth(0)

def eyes():
    if eye == "Triangles":
        # triangle eyes
        penMove(-5,-100)
        colorTriangle(50)
        penMove(-90,-100)
        colorTriangle(50)
    elif eye == "Circles":
        # circle eyes
        penMove(5,-100)
        painter.begin_fill()
        painter.circle(35)
        painter.end_fill()
        penMove(-95,-100)
        painter.begin_fill()
        painter.circle(35)
        painter.end_fill()

def friendlyFace():
    if friendly == "No Teeth":
        # Friendly (No Teeth)
        painter.begin_fill()
        painter.seth(0)
        penMove(-80,-125)
        painter.forward(110)
        painter.seth(90)
        painter.circle(55,-180)
        painter.end_fill()

    elif friendly == "One Tooth":
        # Friendly(One Tooth)
        painter.begin_fill()
        painter.seth(0)
        penMove(-80,-125)
        painter.forward(110)
        painter.seth(90)
        painter.circle(55,-180)
        painter.end_fill()

        painter.fillcolor("white")
        penMove(-55,-125)
        painter.seth(270)
        painter.begin_fill()
        square(20)
        painter.end_fill()

    elif friendly == "Two Teeth":
        # Friendly (Two Teeth)
        painter.begin_fill()
        painter.seth(0)
        penMove(-80,-125)
        painter.forward(110)
        painter.seth(90)
        painter.circle(55,-180)
        painter.end_fill()

        painter.fillcolor("white")
        penMove(-55,-125)
        painter.seth(270)
        painter.begin_fill()
        square(20)
        painter.end_fill()

        penMove(-15,-125)
        painter.seth(270)
        painter.begin_fill()
        square(20)
        painter.end_fill()


def spookyFace():
    if spooky == "Vampire":
        # vampire teeth
        painter.begin_fill()
        painter.seth(0)
        penMove(-80,-125)
        painter.forward(110)
        painter.seth(90)
        painter.circle(55,-180)
        painter.end_fill()


        painter.fillcolor("white")
        penMove(-65,-125)
        painter.begin_fill()
        invertedTriangle(35)
        painter.end_fill()
        penMove(-15,-125)
        painter.begin_fill()
        invertedTriangle(35)
        painter.end_fill()

        # blood
        painter.color("#b30000","#b30000")
        penMove(-56.5,-137)
        painter.begin_fill()
        invertedTriangle(18)
        painter.end_fill()

        penMove(-6.5,-137)
        painter.begin_fill()
        invertedTriangle(18)
        painter.end_fill()
        # drop of blood
        penMove(-50, -190)
        painter.dot()
        penMove(-40, -210)
        painter.dot()
        penMove(0, -190)
        painter.dot()
        penMove(-10, -210)
        painter.dot()
    
    elif spooky == "Half Spiked":
        # Top Spike
        penMove(-115,-120)
        painter.begin_fill()
        painter.seth(-45)
        painter.forward(40)

        painter.seth(45)
        painter.forward(30)

        painter.seth(-45)
        painter.forward(30)

        painter.seth(45)
        painter.forward(30)

        painter.seth(-45)
        painter.forward(30)

        painter.seth(45)
        painter.forward(30)

        painter.seth(-45)
        painter.forward(30)

        painter.seth(45)
        painter.forward(40)

        painter.seth(90)
        painter.circle(92,-180)
        painter.end_fill()

    elif spooky == "Full Spiked":
         # Full Spiked Mouth
        painter.begin_fill()
        penMove(-115,-120)
        painter.begin_fill()
        painter.seth(-45)
        painter.forward(40)

        painter.seth(45)
        painter.forward(30)

        painter.seth(-45)
        painter.forward(30)

        painter.seth(45)
        painter.forward(30)

        painter.seth(-45)
        painter.forward(30)

        painter.seth(45)
        painter.forward(30)

        painter.seth(-45)
        painter.forward(30)

        painter.seth(45)
        painter.forward(40)

        painter.seth(240)
        painter.forward(60)

        painter.seth(135)
        painter.forward(30)

        painter.seth(225)
        painter.forward(30)

        painter.seth(135)
        painter.forward(30)

        painter.seth(225)
        painter.forward(30)

        painter.seth(135)
        painter.forward(30)

        painter.seth(225)
        painter.forward(30)

        painter.seth(119)
        painter.forward(60)
        painter.end_fill()

# adding the moon for the back ground
painter.hideturtle()
painter.speed(0)
painter.fillcolor("#F4F6F0")
penMove(-250,200)
painter.seth(-30)
painter.begin_fill()
painter.circle(50,180)
painter.seth(110)
painter.circle(65,-100)
painter.end_fill()

# adding stars in the background
painter.pencolor("white")
penMove(-230, 150)
painter.dot(4)
penMove(0,145)
painter.dot(4)
penMove(-150,250)
painter.dot(4)
penMove(230,230)
painter.dot(4)
penMove(150,140)
painter.dot(4)
penMove(300,80)
painter.dot(4)
penMove(-300,300)
painter.dot(4)
penMove(-400,50)
painter.dot(4)
penMove(400,-30)
painter.dot(4)
penMove(-390,200)
painter.dot(4)

penMove(150,350)
painter.seth(0)
painter.forward(20)
penMove(160,360)
painter.seth(270)
painter.forward(20)

penMove(0,250)
painter.seth(0)
painter.forward(20)
penMove(10,260)
painter.seth(270)
painter.forward(20)


# pumpkin outline
painter.showturtle()
painter.pencolor("black")
penMove(0,0)
painter.speed(6)
painter.fillcolor("#ff7518")
painter.begin_fill()
painter.seth(145)
painter.circle(110,75)
painter.seth(225)
painter.circle(150,100)

painter.seth(340)
painter.circle(50,60)
painter.seth(325)
painter.circle(65,60)
painter.seth(325)
painter.circle(65,60)

painter.seth(30)
painter.circle(150,100)
painter.seth(135)
painter.circle(110,75)
painter.end_fill()

# the pumpkin stem
painter.fillcolor("dark green")
penMove(-25,6)
painter.begin_fill()
painter.seth(60)
painter.circle(40,60)
painter.seth(145)
painter.circle(40,-75)
painter.end_fill()

# add curvature lines for pumpkin
penMove(0,0)
painter.seth(-220)
painter.circle(152,-100)

penMove(-26,6)
painter.seth(212)
painter.circle(155,100)

# Fill Color for eyes and mouth
painter.fillcolor("#381700")

#drawing eyes
eyes()

# drawing the mouth
if mouth == "Friendly":
    friendlyFace()

elif mouth == "Spooky":
    spookyFace()

penMove(-150, 100)
painter.pencolor("#b30000")
painter.write("Spooky Time! ", True, font = ("Chiller", 50, "bold"))

# hides turtly at the end
painter.hideturtle()

# make screen persist
wn.mainloop()