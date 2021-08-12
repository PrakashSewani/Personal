from tkinter import *

root=Tk()
root.title("Paint App")
root.geometry('500x500')

def display(event):
    x1,y1,x2,y2=(event.x-3),(event.y-3),(event.x+3),(event.y+3)

    Colour='#000fff000'

    w.create_line(x1,y1,x2,y2,fill=Colour)

w=Canvas(root,width=5000,height=5000)

w.bind('<B1-Motion>',display)

l=Label(root,text="Double Click and Drag to draw")

l.pack()
w.pack()

root.mainloop()

#Aur karne ho canvas ke visit link in Canvas.py