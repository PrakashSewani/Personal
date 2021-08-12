"""
ollowing are commonly used Option can be used with this widget :-

activebackground: This option is used to represent the background color of the widget when it has the focus.
bg: This option is used to represent the background color of the widget.
bd: This option is used to represent the border width of the widget.
command: This option can be set to the procedure associated with the list which can be called each time when the scrollbar is moved.
cursor: In this option, the mouse pointer is changed to the cursor type set to this option which can be an arrow, dot, etc.
elementborderwidth: This option is used to represent the border width around the arrow heads and slider. The default value is -1.
Highlightbackground: This option is used to focus highlighcolor when the widget doesn’t have the focus.
highlighcolor: This option is used to focus highlighcolor when the widget has the focus.
highlightthickness: This option is used to represent the thickness of the focus highlight.
jump: This option is used to control the behavior of the scroll jump. If it set to 1, then the callback is called when the user releases the mouse button.
orient: This option can be set to HORIZONTAL or VERTICAL depending upon the orientation of the scrollbar.
repeatdelay: This option tells the duration up to which the button is to be pressed before the slider starts moving in that direction repeatedly. The default is 300 ms.
repeatinterval: The default value of the repeat interval is 100.
takefocus: You can tab the focus through a scrollbar widget
troughcolor: This option is used to represent the color of the trough.
width: This option is used to represent the width of the scrollbar.
Methods:
Methods used in this widgets are as follows:

get(): This method is used to returns the two numbers a and b which represents the current position of the scrollbar.
set(first, last): This method is used to connect the scrollbar to the other widget w. The yscrollcommand or xscrollcommand of the other widget to this method.
"""
from tkinter import *

root=Tk()
root.geometry('150x250')

w=Label(root,text='Scrollbar')
w.pack()

scroll_bar=Scrollbar(root)
scroll_bar.pack(side=RIGHT,fill=Y)

Mylist=Listbox(root,yscrollcommand=scroll_bar.set)

for line in range(1,26):
    Mylist.insert(END, 'Prakash' +str(line))

Mylist.pack(side=LEFT,fill=BOTH)

scroll_bar.config(command=Mylist.yview)

root.mainloop()