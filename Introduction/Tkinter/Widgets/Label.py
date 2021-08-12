"""
Parameters:
master: This represents the parent window
options: Below is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas:

Various Options are:

anchor: This options is used to control the positioning of the text if the widget has more space than required for the text. The default is anchor=CENTER, which centers the text in the available space.
bg:This option is used to set the normal background clior displayed behind the label and indicator.
height:This option is used to set the vertical dimension of the new frame.
width:Width of the label in characters (not pixels!). If this option is not set, the label will be sized to fit its contents.
bd:This option is used to set the size of the border around the indicator. Default bd value is set on 2 pixels.
font:If you are displaying text in the label (with the text or textvariable option), the font option is used to specify in what font that text in the label will be displayed.
cursor:It is used to specify what cursor to show when the mouse is moved over the label. The default is to use the standard cursor.
textvariable: As the name suggests it is associated with a Tkinter variable (usually a StringVar) with the label. If the variable is changed, the label text is updated.
bitmap:It is used to set the bitmap to the graphical object specified so that, the label can represent the graphics instead of text.
fg:The label clior, used for text and bitmap labels. The default is system specific. If you are displaying a bitmap, this is the clior that will appear at the position of the 1-bits in the bitmap.
image: This option is used to display a static image in the label widget.
padx:This option is used to add extra spaces between left and right of the text within the label.The default value for this option is 1.
pady:This option is used to add extra spaces between top and bottom of the text within the label.The default value for this option is 1.
justify:This option is used to define how to align multiple lines of text. Use LEFT, RIGHT, or CENTER as its values. Note that to position the text inside the widget, use the anchor option. Default value for justify is CENTER.
relief: This option is used to specify appearance of a decorative border around the label. The default value for this option is FLAT.
underline:This
wraplength:Instead of having only one line as the label text it can be broken itno to the number of lines where each line has the number of characters specified to this option.
"""
from tkinter import *

top=Tk()
top.geometry('450x450')

user_name=Label(top,text='Username').place(x=40,y=60)

user_password=Label(top,text='Password').place(x=40,y=100)

submit_button=Button(top,text='Submit').place(x=40,y=130)

user_name_input=Entry(top,width=30).place(x=110,y=60)

user_password_input=Entry(top,width=30).place(x=110,y=100)

"""
Label_frame=LabelFrame(top,text='This is Label Frame')
Label_frame.pack(expand='yes',fill='both')

label1=Label(Label_frame,text='1. This is a Label')
label1.place(x=0,y=5)
label2=Label(Label_frame,text='2. This is second Label')
label2.place(x=0,y=35)
label3=Label(Label_frame,text='3. This is 3rd Label')
label3.place(x=0,y=65)
"""

top.mainloop()