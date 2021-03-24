from tkinter import *
from tkinter.ttk import *

root=Tk()

progress=Progressbar(root, orient= HORIZONTAL, length=1000, mode='indeterminate')
progress.pack(pady=10)

def bar():
    import time
    progress['value']=0
    
    progress['value']=20
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=40
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=60
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=80
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=100
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=80
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=60
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=40
    root.update_idletasks()
    time.sleep(0.5)
    
    progress['value']=20
    root.update_idletasks()
    time.sleep(0.5)

    progress['value']=0

Button(root,text='Start?',command=bar).pack(pady=10)

root.mainloop()