import turtle

t = turtle.Turtle()

t.shape('turtle')
t.pensize(3)

t.speed(90)

turtle.bgcolor('violet')
t.fillcolor('pink')
t.pencolor('white')
t.begin_fill()

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.left(140)
t.forward(113)
curve()
t.left(120)
curve()
t.forward(112)

t.end_fill()

turtle.exitonclick()
