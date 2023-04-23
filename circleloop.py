import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
i = 0

colors = ["red","blue","green","yellow"]
t.speed(100)
t.pencolor(colors[i])
for x in range(150):
    t.left(91)
    t.circle(2*x)
turtle.done()