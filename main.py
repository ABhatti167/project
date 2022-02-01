from tkinter import *
from tkinter import messagebox
import sqlite3



root = Tk()

root.geometry("500x500")


windows = Toplevel()

r = IntVar
var = IntVar()
varz = StringVar

def add():
    global vars
    vars = 5
    vars+=1
    lists.insert(lists.size(), varz)

lists = Listbox(root, font="Arial", bg="lightgreen", selectmode=MULTIPLE)
lists.insert(1, "pizza")
lists.insert(2,"Big Pizza")
lists.insert(3,"Extra Big Pizza")
lists.insert(4,"Super Big Pizza")
lists.insert(5,"Thicc Pizza")
lists.pack()

def submit():
    global var
    var = lists.get(lists.curselection())





submit = Button(root, text="submit", command = submit).pack()



label = Label(root, text="hello").pack()

entry1 = Entry(root, textvariable=varz).pack()






add = Button(root, text = "add", command= add).pack()

def delete():
    for index in reversed(lists.curselection()):
        lists.delete(index)

delete = Button(root, text="Delete", command = delete).pack()




def something():
    myLabel = Label(root, text= var.get()).pack()


check_ = Checkbutton(root, text="I dare you to check this box", variable = var, command = something).pack()

options = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 'Saturday']

myLabel = Label(root, text= var.get()).pack()

clicked = StringVar()
clicked.set("Hello")

def get():
    Labels = Label(root, text=clicked.get()).pack()


dropdown = OptionMenu(root, clicked, *options).pack()

buttons = Button(root, text="Click it", command= get).pack()

Labels = Label(root,text= clicked.get()).pack()

root.mainloop()

