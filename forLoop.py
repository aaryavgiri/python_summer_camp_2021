import turtle

p = turtle.Pen()
turtle.bgcolor('black')
i = 0

colors = ["black"]

p.speed(100)

for x in range(1000):
        p.pencolor(colors[i])
        i = i+1
        if i > 3:
            i=0
        p.forward(1*x)
        p.right(-50)
        p.forward(100)
        p.left(-50)
        p.forward(100)
        p.right(100)
        p.forward(100)  
     
turtle.done()