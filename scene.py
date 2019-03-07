import turtle
draw = turtle.Turtle()
# QOL Functions
def forward(dist):
    draw.forward(dist)
def backward(dist):
    draw.backward(dist)
def left(dist):
    draw.left(dist)
def right(dist):
    draw.right(dist)
def penup():
    draw.penup()
def pendown():
    draw.pendown()
def simple_circle(rad):
    draw.circle(rad)
def circlenostep(rad,ext):
    draw.circle(rad,ext)
def circle(rad,ext,step):
    draw.circle(rad,ext,step)
def setposition(x, y):
    draw.setposition(x, y)
def speed(sped):
    draw.speed(sped)
def color(color):
    draw.color(color)
def pensize(size):
    draw.pensize(size)
def begin_fill():
    draw.begin_fill()
def end_fill():
    draw.end_fill()
def clear():
    draw.clear()