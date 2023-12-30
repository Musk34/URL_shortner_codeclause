import pyshorteners
from tkinter import *

win = Tk()
win.geometry('400x280')
win.configure(bg="pink")

def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry2.delete(0, END)  
    entry2.insert(END, s)

Label(win, text="Enter your Url Link", font="impack 17 bold", bg="black", fg="white").pack(fill="x")
entry1 = Entry(win, font="10", bd=3, width="40")
entry1.pack(pady=30)
Button(win, text="Click Me", font="impack 12 bold", bg="blue", fg="white", width="14", command=short).pack()
entry2 = Entry(win, font="impack 16 bold", bg="pink", width=25, bd=0)
entry2.pack(pady=30)

win.mainloop()
