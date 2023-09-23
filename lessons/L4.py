from tkinter import * 

window = Tk()
window.title('canvas')
window.geometry ('1024x1024')

paper = Canvas(bg = 'lightblue', width = 500, height = 500)
paper.pack()
paper.create_oval((5,5,100,100), outline = 'yellow', fill = 'yellow')
paper.create_oval((150,150,350,250) , outline = "white", fill = 'white')
paper.create_oval((200,200,400,300) , outline = "white", fill = 'white')
paper.create_oval((100,200,300,300) , outline = "white", fill = 'white')

window.mainloop()