#q 1 2
from tkinter import *


def write_s():
    print("Heyy there")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="Bye",
                   fg="purple",
                   command=quit)
button.pack(side=tk.LEFT)
s = tk.Button(frame,
                   text="Heyyyy",
                   command=write_s)
s.pack(side=tk.LEFT)

root.mainloop()

#q 3
root = Tk()
label = Label(root,text="hello friends")
def click():
    label.config(text="chai pee lo")

b1 = Button(root,text="Click here",command=click)
label.pack()
b1.pack()
root.mainloop()


#q 4

root=Tk()
def show():
   ee = v1.get()
   l = Label(root,text=ee).grid(row=2)
v1=IntVar()
bui=Button(root,text="Click",command=show).grid(row=1)
textbox=Entry(root,textvariable=v1).grid(row=0)
root.mainloop()