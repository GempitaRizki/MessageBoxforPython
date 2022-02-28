from ast import Delete
from cProfile import label
from tkinter import *
from tkinter import messagebox


root =  Tk ()

root.geometry("500x300")
root.title("Gempita Rizki Ramadhan")
root.iconbitmap("icon.ico")

def pesan () : 
    messagebox.askquestion ("info masee","ini adalah info mase")

btn = Button (root,text = "click me", command = pesan)
btn.grid()

root.mainloop()