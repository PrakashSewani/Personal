from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile

root=Tk()
root.geometry('200x100')

def open_file():
    file=askopenfile(mode='r',filetypes=[('Python Files','*.py')])
    if file is not None:
        content=file.read()
        print(content)

button=Button(root,text='Open File',command=open_file)
button.pack()

mainloop()