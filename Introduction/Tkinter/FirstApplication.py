from tkinter import *

root=Tk()

root.title("Welcome to my Application")

root.geometry('350x200')

menu=Menu(root)
item=Menu(root)
item.add_command(label='New')
menu.add_cascade(label='File',menu=item)
root.config(menu=menu)

lbl=Label(root,text="Are you ready for an adventure? ")
lbl.grid(column=0,row=0)

txt=Entry(root,width=20)
txt.grid(column=0,row=1)

def Clicked():
    res=text='You wrote '+txt.get()
    lbl.configure(text=res)

btn=Button(root, text="Click me!",fg='red',command=Clicked)
btn.grid(column=2,row=1)

root.mainloop()