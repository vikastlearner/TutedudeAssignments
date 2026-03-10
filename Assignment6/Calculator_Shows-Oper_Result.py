# Step1: importing

import tkinter as tk
import tkinter.font as tfont
import tkinter.ttk as ttk
from textwrap import fill

# GUI interaction
window = tk.Tk()
window.title("My Calculator")
window.geometry('500x500')

# Adding inputs

# Entry box

label1 = ttk.Label(window, text="My First Calculator", font=tfont.Font(family="Times New Roman", weight="bold", size=10)    )
label1.pack()

e = ttk.Entry(width=30, font=tfont.Font(family="Times New Roman", weight="bold", size=20))
e.place(x=10, y=30)
#e.pack(pady=20)

# Result Box

label2 = ttk.Label(window, text="Result", font=tfont.Font(family="Times New Roman", weight="bold", size=10)    )
label2.place(y=80)

r = ttk.Entry(width=30, font=tfont.Font(family="Times New Roman", weight="bold", size=20))
r.place(x=10, y=100)
#r.pack(pady=10)

# Buttons

def click(num):
    result = e.get()
    e.delete(0, tk.END)
    e.insert(0,str(result) + str(num))

b=ttk.Button(text = "1", width=12, command=lambda:click(1))
b.place(x=10, y=150)

b=ttk.Button(text = "2", width=12, command=lambda:click(2))
b.place(x=90, y=150)

b=ttk.Button(text = "3", width=12, command=lambda:click(3))
b.place(x=170, y=150)

b=ttk.Button(text = "4", width=12, command=lambda:click(4))
b.place(x=10, y=190)

b=ttk.Button(text = "5", width=12, command=lambda:click(5))
b.place(x=90, y=190)

b=ttk.Button(text = "6", width=12, command=lambda:click(6))
b.place(x=170, y=190)

b=ttk.Button(text = "7", width=12, command=lambda:click(7))
b.place(x=10, y=230)

b=ttk.Button(text = "8", width=12, command=lambda:click(8))
b.place(x=90, y=230)

b=ttk.Button(text = "9", width=12, command=lambda:click(9))
b.place(x=170, y=230)

b=ttk.Button(text = "0", width=12, command=lambda:click(0))
b.place(x=10, y=270)

# Operators
def add():
    global n1
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, tk.END)
    e.insert(0,f"{n1}+")


b=ttk.Button(text = "+", width=12, command = add)
b.place(x=90, y=270)

def sub():
    global n1
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, tk.END)
    e.insert(0, f"{n1}-")

b=ttk.Button(text = "-", width=12, command = sub)
b.place(x=170, y=270)

def mul():
    global n1
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, tk.END)
    e.insert(0, f"{n1}x")

b=ttk.Button(text = "*", width=12, command = mul)
b.place(x=10, y=300)

def div():
    global n1
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, tk.END)
    e.insert(0, f"{n1}/")

b=ttk.Button(text = "/", width=12, command = div)
b.place(x=90, y=300)

def equal():
    n2 = e.get()
    j=n2[len(n1)+1:]
    if math == "addition":
        r.insert(0,i + int(j))
    elif math == "subtraction":
        r.insert(0,i - int(j))
    elif math == "multiplication":
        r.insert(0,i * int(j))
    elif math == "division":
        print(i)
        print(j)
        r.insert(0,i / int(j))


b=ttk.Button(text = "=", width=12, command=equal)
b.place(x=170, y=300)

def clear():
    e.delete(0, tk.END)
    r.delete(0, tk.END)

b=ttk.Button(text = "clear", width=12, command=clear)
b.place(x=10, y=340)




# mainloop

window.mainloop()