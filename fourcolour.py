import turtle

p = turtle.Pen()
turtle.bgcolor('black')
i = 0

colors = ["red","blue","green","yellow"]

p.speed(50)

for x in range(1000):
        p.pencolor(colors[i])
        i = i+1
        if i > 3:
            i=0
        p.forward(2*x)
        p.right(91)
        
turtle.done