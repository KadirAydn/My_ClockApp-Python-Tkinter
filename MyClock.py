from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from time import strftime
from turtle import back

root = Tk()
root.title("My Clock - Coded by KA")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 50), background="black", foreground="#11ddee")
label.pack(anchor='se')

time()

mainloop()