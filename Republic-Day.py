import turtle
x=turtle.Turtle()
y=turtle.Screen()
y.bgcolor("black")
x.speed(1)
def rect(color):
    x.begin_fill()
    x.fillcolor(color)
    for i in range(2):
        x.forward(400)
        x.right(90)
        x.forward(100)
        x.right(90)
    x.end_fill()
x.up()
x.goto(0,-300)
x.color("white")
x.down()
x.goto(0,300)
rect("orange")
x.goto(0,200)
x.forward(200)
x.color("blue")
x.circle(-50)
x.setheading(270)
x.forward(50)
x.setheading(0)
for i in range(24):
    x.forward(45)
    x.bk(45)
    x.left(15)
x.setheading(90)
x.forward(50)
x.setheading(0)
x.color("black")
x.forward(200)
x.right(90)
x.forward(100)
x.right(90)
x.forward(400)
x.right(90)
x.forward(100)
x.right(90)
x.goto(0,100)
rect("green")
x.hideturtle()
