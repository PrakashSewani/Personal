from tkinter import *

root=Tk()
root.geometry('300x300')
root.title('Q&A')

def Take_Input():
    INPUT=inputtxt.get('1.0','end-1c')
    print(INPUT)

    if(INPUT=='120'):
        Output.insert(END,'Correct Answer')
    else:
        Output.insert(END,"Weong Answer")

l=Label(root,text="What is 24*5?")
inputtxt=Text(root,height=10,width=25,bg='light yellow')

Output=Text(root,height=5,width=25,bg='cyan')

Display=Button(root,height=2,width=25,text='Show',command=lambda:Take_Input())

l.pack() 
inputtxt.pack() 
Display.pack() 
Output.pack() 
  
root.mainloop() 