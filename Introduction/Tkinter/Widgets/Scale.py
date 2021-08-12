"""
Optional parameters
root – root window.
bg – background colour
fg – foreground colour
bd – border
orient – orientation(vertical or horizontal)
from_ – starting value
to – ending value
troughcolor – set colour for trough.
state – decides if the widget will be responsive or unresponsive.
sliderlength – decides the length of the slider.
label – to display label in the widget.
highlightbackground – the colour of the focus when widget is not focused.
cursor – The cursor on the widget ehich could be arrow, circle, dot etc.
Methods

set(value) – set the value for scale.
get() – get the value of scale.
"""
from tkinter import *

root=Tk()
root.geometry('300x800')

v1=DoubleVar()
v2=DoubleVar()

def show1():
    sel='Horizontal Scale Value='+ str(v1.get())
    l1.config(text=sel,font=('Courier',14))

def show2():
    sel='Vertical Scale Value='+ str(v2.get())
    l2.config(text=sel)

s1=Scale(root, variable=v1,from_=1, to=100,length=300, orient=HORIZONTAL)
l3=Label(root,text='Horizontal Scaler')
b1=Button(root, text='Display Horizontal Scale Value',command=show1)

s2 = Scale( root, variable = v2,from_ = 50, to = 1,orient = VERTICAL)   
l4 = Label(root, text = "Vertical Scaler") 
b2 = Button(root, text ="Display Vertical",command = show2)

l1=Label(root)
l2 = Label(root)

s1.pack(anchor = CENTER)  
l3.pack() 
b1.pack(anchor = CENTER) 
l1.pack()

s2.pack(anchor = CENTER)  
l4.pack() 
b2.pack() 
l2.pack()
  
root.mainloop()