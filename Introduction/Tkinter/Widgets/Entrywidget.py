"""
Parameters: 
 
1) Parent:      The Parent window or frame in which the widget to display.
2) Options:     The various options provided by the entry widget are: 
 

bg :            The normal background color displayed behind the label and indicator. 
bd :            The size of the border around the indicator. Default is 2 pixels. 
font :          The font used for the text. 
fg :            The color used to render the text. 
justify :       If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT. 
relief :        With the default value, relief=FLAT. You may set this option to any of the other styles like : SUNKEN, RIGID, RAISED, GROOVE 
show :          Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show=”*”. 
textvariable :  In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.
Methods:        The various methods provided by the entry widget are: 

get() :         Returns the entry’s current text as a string. 
delete() :      Deletes characters from the widget 
insert ( index, ‘name’) : Inserts string ‘name’ before the character at the given index. 
"""

import tkinter as tk

root=tk.Tk()
root.title('First Tkinter Window')
root.geometry('600x400')

name_var=tk.StringVar()
passw_var=tk.StringVar()

def submit():
    name=name_var.get()
    password=passw_var.get()

    print('The name is:'+name)
    print('The password is:'+password)

    name_var.set('')
    passw_var.set('')

name_label=tk.Label(root,text='Username')
name_entry=tk.Entry(root,textvariable=name_var)

pass_label=tk.Label(root,text='Password')
pass_entry=tk.Entry(root,textvariable=passw_var, show='*')

sub_btn=tk.Button(root,text='Submit',command=submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
pass_label.grid(row=1,column=0)
pass_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()
