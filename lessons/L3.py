from tkinter import *
import random 

btn_list = ['blue', 'white', 'pink', 'grey']
text_list = ['push me', 'dont click', 'press me' ]

def button_click():
    button1.configure( bg = random.choice(btn_list))

def btn2_click():
    btn2.configure (text = random.choice(text_list))

root= Tk()
root.title('buttons')
root.geometry('1024x1000')

button1 = Button(text = "click me", bg = "violet", font = ("Times New Roman", 14), command = button_click)
button1.pack()

btn2 = Button(text = "push em", bg = "pink", font =  ("Times New Roman", 14), command = btn2_click )
btn2.pack()

root.mainloop()