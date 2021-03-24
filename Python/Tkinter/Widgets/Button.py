from tkinter import *
from tkinter.ttk import *

root=Tk()
root.geometry('350x100')

style=Style()
style.configure('W.TButton',font=
                    ('calibri',10,'bold','underline'),
                    foreground='red')#TButton for all available buttons W.TButton for specific
style.map('TButton',foreground=[('active','!disabled','green')],
                    background=[('active','black')])#hover commands

btn1=Button(root, text='Quit!',style='W.TButton',command=root.destroy)
btn1.grid(row=0,column=3,padx=100)

btn2=Button(root,text='Click Me!', command=None)
btn2.grid(row=1,column=3,pady=10,padx=100)

photo=PhotoImage(file=r"D:\Personal\Python\Tkinter\Widgets\Button.png")
photoimage=photo.subsample(3,3)#resize module

btn3=Button(root,text='Click Me!',image=photoimage,compound=LEFT)
btn3.grid(row=2,column=3,padx=100,pady=100)

root.mainloop()