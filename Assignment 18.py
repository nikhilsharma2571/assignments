#question1
import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title("info")
dict={'name':'nikhil','mobile_number':8146394427}
scrollbar=Scrollbar(root)
scrollbar.pack(side=LEFT,fill=Y)
mylist=Listbox(root,yscrollcommand= scrollbar.set)
for key in dict.__iter__():
        mylist.insert(END,key)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
def mad():
    root.quit()
b=Button(root,text="enter",command=mad)
b.pack()
root.mainloop()


#question2

def show():
    dict.update({"age":21})
    print(dict)
button1=Button(root,text='good',command=show)
button1.pack()
root.mainloop()