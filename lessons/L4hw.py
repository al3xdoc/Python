from tkinter import * 

window = Tk()
window.title('canvas')
window.geometry ('1024x1024')

paper = Canvas(bg = '#AECBD6', width = 500, height = 500)
paper.pack()
paper.create_polygon((190,200, 150, 130, 150, 100, 170, 70, 190, 100, 210, 70, 230, 100, 230, 130) , outline = "#957DAD", fill = '#957DAD')

window.mainloop()