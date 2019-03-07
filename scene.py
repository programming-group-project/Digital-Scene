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
speed(0)
# Variable List
canvas_height = 400
canvas_width = 600
water_height = 100

# No Touch
def drawCanvas(height, width):
    penup()
    setposition(-width/2, -height/2)
    pendown()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    penup()
    setposition(0, 0)
    pendown()
def inf_Circle():
    speed(0)
    penup()
    setposition(0,-canvas_height/2 - 5)
    while 1 == 1:
        simple_circle(5)
# Make Touch Here
#---------------------------------------------------------------------
def shimmer(length, width, x, y): # Gabe
    #This draws the shimmers in the water
    penup()
    setposition(x, y)
    
def draw_water(water_height): # Gabe
    # This draws the water at the bottom of the canvas
    penup()
    setposition(-canvas_width/2, -canvas_height/2)
    pendown()
    color("#006994")
    begin_fill()
    left(90)
    forward(water_height)
    right(90)
    forward(canvas_width)
    right(90)
    forward(water_height)
    right(90)
    forward(canvas_width)
    end_fill()
    right(180)

def draw_large_building(height, width, col): # Sage
    # Draws Rectangle based on given parameters
    penup()
    backward(width/2)
    pendown()
    color(col)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
    penup()
    forward(width/2)
def draw_small_buidling(height, width, col): # Sage
    # Draws Rectangle based on given parameters and has roof
    penup()
    backward(width/2)
    pendown()
    color(col)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
    penup()
    forward(width/2)
#---------------------------------------------------------------------

# Compile Everything Here
def draw_scene():
    drawCanvas(canvas_height,canvas_width)
    draw_water(water_height)
    inf_Circle()

draw_scene()
