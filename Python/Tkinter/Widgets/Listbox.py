"""
root – root window.
bg – background colour
fg – foreground colour
bd – border
height – height of the widget.
width – width of the widget.
font – Font type of the text.
highlightcolor – The colour of the list items when focused.
yscrollcommand – for scrolling vertically.
xscrollcommand – for scrolling horizontally.
cursor – The cursor on the widget which can be an arrow, a dot etc.
Common methods

yview – allows the widget to be vertically scrollable.
xview – allows the widget to be horizontally scrollable.
get() – to get the list items in a given range.
activate(index) – to select the lines with a specified index.
size() – return the number of lines present.
delete(start, last) – delete lines in the specified range.
nearest(y) – returns the index of the nearest line.
curseselection() – returns a tuple for all the line numbers that are being selected.
"""
from tkinter import *

root=Tk()

listbox=Listbox(root,height=10, width=15,bg='green',activestyle='dotbox',font='Courier', fg='yellow')

root.geometry('300x250')

label=Label(root, text='FOOD ITEMS')

listbox.insert(1, "Nachos") 
listbox.insert(2, "Sandwich") 
listbox.insert(3, "Burger") 
listbox.insert(4, "Pizza") 
listbox.insert(5, "Burrito")

label.pack()
listbox.pack()

root.mainloop()