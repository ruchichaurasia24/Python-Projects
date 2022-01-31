import turtle
x=turtle.Turtle()
y=turtle.Screen()
y.bgcolor("black")
x.speed(0)
list=["purple","red","orange","blue","green"]
for i in range(200):
    x.color(list[i%5])
    x.pensize(i/10+1)
    x.forward(i)
    x.left(59)
