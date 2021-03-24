"""
Following are commonly used Option can be used with this widget :-

activebackground:       This option used to represent the background color when the checkbutton is under the cursor.
activeforeground:       This option used to represent the foreground color when the checkbutton is under the cursor.
bg:                     This option used to represent the normal background color displayed behind the label and indicator.
bitmap:                 This option used to display a monochrome image on a button.
bd:                     This option used to represent the size of the border around the indicator and the default value is 2 pixels.
command:                This option is associated with a function to be called when the state of the checkbutton is changed.
cursor:                 By using this option, the mouse cursor will change to that pattern when it is over the checkbutton.
disabledforeground:     The foreground color used to render the text of a disabled checkbutton. The default is a stippled version of the default foreground color.
font:                   This option used to represent the font used for the text.
fg:                     This option used to represent the color used to render the text.
height:                 This option used to represent the number of lines of text on the checkbutton and it’s default value is 1.
highlightcolor:         This option used to represent the color of the focus highlight when the checkbutton has the focus.
image:                  This option used to display a graphic image on the button.
justify:                This option used to control how the text is justified: CENTER, LEFT, or RIGHT.
offvalue:               The associated control variable is set to 0 by default if the button is unchecked. We can change the state of an unchecked variable to some other one.
onvalue:                The associated control variable is set to 1 by default if the button is checked. We can change the state of the checked variable to some other one.
padx:                   This option used to represent how much space to leave to the left and right of the checkbutton and text. It’s default value is 1 pixel.
pady:                   This option used to represent how much space to leave above and below the checkbutton and text. It’s default value is 1 pixel.
relief:                 The type of the border of the checkbutton. It’s default value is set to FLAT.
selectcolor:            This option used to represent the color of the checkbutton when it is set. The Default is selectcolor=”red”.
selectimage:            The image is shown on the checkbutton when it is set.
state:                  It represents the state of the checkbutton. By default, it is set to normal. We can change it to DISABLED to make the checkbutton unresponsive. The state of the checkbutton is ACTIVE when it is under focus.
text:                   This option used use newlines (“\n”) to display multiple lines of text.
underline:              This option used to represent the index of the character in the text which is to be underlined. The indexing starts with zero in the text.
variable:               This option used to represents the associated variable that tracks the state of the checkbutton.
width:                  This option used to represents the width of the checkbutton. and also represented in the number of characters that are represented in the form of texts.
wraplength:             This option will be broken text into the number of pieces.

Methods:

deselect():             This method is called to turn off the checkbutton.
flash():                The checkbutton is flashed between the active and normal colors.
invoke():               This method will invoke the method associated with the checkbutton.
select():               This method is called to turn on the checkbutton.
toggle():               This method is used to toggle between the different Checkbuttons.
"""

from tkinter import *

root=Tk()
root.geometry('300x200')

w=Label(root,text='Welcome',font='55')
w.pack()

Checkbutton1= IntVar()
Checkbutton2= IntVar()
Checkbutton3= IntVar()

Button1=Checkbutton(root,text='Tutorial',
                    variable=Checkbutton1,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10)

Button2=Checkbutton(root,text='Student',
                    variable=Checkbutton2,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10)

Button3=Checkbutton(root,text='Courses',
                    variable=Checkbutton3,
                    onvalue=1,
                    offvalue=0,
                    height=2,
                    width=10)

Button1.pack()
Button3.pack()
Button2.pack()

mainloop()