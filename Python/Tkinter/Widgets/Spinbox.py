"""
ollowing are commonly used Option can be used with this widget :-

activebackground: This option used to represent the background color when the slider and arrowheads is under the cursor.
bg: This option used to represent the normal background color displayed behind the label and indicator.
bd: This option used to represent the size of the border around the indicator and the default value is 2 pixels.
command: This option is associated with a function to be called when the state is changed.
cursor: By using this option, the mouse cursor will change to that pattern when it is over the type.
disabledforeground: This option used to represent the foreground color of the widget when it is disabled..
disabledbackground: This option used to represent the background color of the widget when it is disabled..
font: This option used to represent the font used for the text.
fg: This option used to represent the color used to render the text.
format: This option used to formatting the string and it’s has no default value.
from_: This option used to represent the minimum value.
justify: This option used to control how the text is justified: CENTER, LEFT, or RIGHT.
relief: This option used to represent the type of the border and It’s default value is set to SUNKEN.
repeatdelay: This option is used to control the button auto repeat and its default value is in milliseconds.
repeatinterval: This option is similar to repeatdelay.
state: This option used to represent the represents the state of the widget and its default value is NORMAL.
textvariable: This option used to control the behaviour of the widget text.
to: It specify the maximum limit of the widget value. The other is specified by the from_ option.
validate: This option is used to control how the widget value is validated.
validatecommand: This option is associated to the function callback which is used for the validation of the widget content.
values: This option used to represent the tuple containing the values for this widget.
vcmd: This option is same as validation command.
width: This option is used to represents the width of the widget.
wrap: This option wraps up the up and down button the Spinbox.
xscrollcommand: This options is set to the set() method of scrollbar to make this widget horizontally scrollable.
Methods:
Methods used in this widgets are as follows:

delete(startindex, endindex): This method is used to delete the characters present at the specified range.
get(startindex, endindex): This method is used to get the characters present in the specified range.
identify(x, y): This method is used to identify the widget’s element within the specified range.
index(index): This method is used to get the absolute value of the given index.
insert(index, string): This method is used to insert the string at the specified index.
invoke(element): This method is used to invoke the callback associated with the widget.
"""
from tkinter import *

root=Tk()
root.geometry('300x200')

w=Label(root, text='Spinbox Demo', font='50')
w.pack()

sp=Spinbox(root, from_=0, to=20)
sp.pack()

mainloop()