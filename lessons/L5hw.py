from tkinter import *
import time 

def move_light(event):
    if event.keysym == 'Up':
        canvas.move(light, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(light, 0, 5)
    elif event.keysym == 'Right':
        canvas.move(light, 5, 0)
    elif event.keysym == 'Left':
        canvas.move(light, -5, 0)

root = Tk()
canvas = Canvas(bg = 'black', height = 500, width = 600)
canvas.pack()

light = canvas.create_oval((250,250,200,200), fill = 'white')

canvas.bind_all('<Up>', move_light)
canvas.bind_all('<Down>', move_light)
canvas.bind_all('<Right>', move_light)
canvas.bind_all('<Left>', move_light)

canvas.create_text((100,300), text = "you found me!", font = ("Ariel", 14,) )

root.mainloop()