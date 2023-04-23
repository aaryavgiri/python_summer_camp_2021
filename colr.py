import turtle

p = turtle.Pen()
turtle.bgcolor('black')
i = 0

colors = ["red","blue","green","yellow","orange","purple"]

p.speed(400)

for x in range(200):
    p.pencolor(colors[x%6])
    p.width(x/100 + 1)
    p.forward(x)
    p.right(59)
        
turtle.done()