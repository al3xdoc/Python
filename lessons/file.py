import turtle
import random
      
t = turtle.Turtle()
turtle.Screen().bgcolor("grey")

colours = ["cyan", "purple", "white", "blue"]

t.color(random.choice(colours))

r = 10
  
for i in range(10):
    for i in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.right(36)


