"""
showinfo() – To display some important information .
showwarning() – To display some type of Warning.
showerror() –To display some Error Message.
askquestion() – To display a dialog box that asks with two options YES or NO.
askokcancel() – To display a dialog box that asks with two options OK or CANCEL.
askretrycancel() – To display a dialog box that asks with two options RETRY or CANCEL.
askyesnocancel() – To display a dialog box that asks with three options YES or NO or CANCEL.

messagebox.name_of_function(Title, Message, [, options])

name_of_function – Function name that which we want to use .
Title – Message Box’s Title.
Message – Message that you want to show in the dialog.
Options –To configure the options.
"""
from tkinter import *
from tkinter import messagebox

root=Tk()

def Submit():
    messagebox.askquestion("Form","Do you want to Submit?")

root.geometry('100x100')

B1=Button(root,text='Submit',command=Submit)
B1.pack()

mainloop()