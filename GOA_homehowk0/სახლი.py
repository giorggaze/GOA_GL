import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(3)
t.width(2)

def rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Front wall
move(-150, -100)
rectangle(200, 150, "#e6cfa7")

# Side wall (3D)
move(50, -100)
t.fillcolor("#d4b896")
t.begin_fill()
t.goto(150, -50)
t.goto(150, 100)
t.goto(50, 50)
t.goto(50, -100)
t.end_fill()

# Roof front
move(-150, 50)
t.fillcolor("#8b3a3a")
t.begin_fill()
t.goto(-50, 150)
t.goto(50, 50)
t.goto(-150, 50)
t.end_fill()

# Roof side
move(50, 50)
t.fillcolor("#732626")
t.begin_fill()
t.goto(150, 100)
t.goto(50, 150)
t.goto(-50, 150)
t.goto(50, 50)
t.end_fill()

# Door
move(-60, -100)
rectangle(50, 80, "#5a3b1e")

# Windows
move(-130, -10)
rectangle(40, 40, "lightblue")

move(-20, -10)
rectangle(40, 40, "lightblue")

# Sun
move(200, 150)
t.fillcolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

t.hideturtle()
turtle.done()
