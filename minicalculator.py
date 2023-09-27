from tkinter import *


from math import *

root = Tk()
root.title("simple calculator")

e = Entry(root, width=50, borderwidth=10)
e.grid(row=0, column=0, columnspan=5, padx=9, pady=9)
def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) +str(number))

def buttonclear():
    e.delete(0, END)


def buttonadd():
    num1 = e.get()
    global fnum
    global math
    math = "addition"
    fnum = int(num1)
    e.delete(0, END)

def buttonequal():
    num2 = e.get()
    e.delete(0, END)
    if math == "addition":
       e.insert(0, fnum + int(num2))
    elif math == "subtraction":
         e.insert(0, fnum - int(num2))
    elif math == "multiplication":
         e.insert(0, fnum * int(num2))
    elif math == "division":
         e.insert(0, fnum / int(num2))
    elif math == "raise to power":
        e.insert(0, pow(fnum, int(num2)))
    elif math == "square root":
        e.insert(0, sqrt(fnum))


def buttonsub():
    num1 = e.get()
    global fnum
    global math
    math = "subtraction"
    fnum = int(num1)
    e.delete(0, END)

def buttonmult():
    num1 = e.get()
    global fnum
    global math
    math = "multiplication"
    fnum = int(num1)
    e.delete(0, END)

def buttondiv():
    num1 = e.get()
    global fnum
    global math
    math = "division"
    fnum = int(num1)
    e.delete(0, END)

def buttonraisetopower():
    num1 = e.get()
    global fnum
    global math
    math = "raise to power"
    fnum = int(num1)
    e.delete(0, END)

def buttonsqrt():
    num1 = e.get()
    global fnum
    global math
    math = "square root"
    fnum = int(num1)
    e.delete(0, END)


button1 = Button(root, text="1", padx=40, pady=25, command=lambda: buttonclick(1), bg="black", fg="white")
button2 = Button(root, text="2", padx=40, pady=25, command=lambda: buttonclick(2), bg="black", fg="white")
button3 = Button(root, text="3", padx=40, pady=25, command=lambda: buttonclick(3), bg="black", fg="white")
button4 = Button(root, text="4", padx=40, pady=25, command=lambda: buttonclick(4), bg="black", fg="white")
button5 = Button(root, text="5", padx=40, pady=25, command=lambda: buttonclick(5), bg="black", fg="white")
button6 = Button(root, text="6", padx=40, pady=25, command=lambda: buttonclick(6), bg="black", fg="white")
button7 = Button(root, text="7", padx=40, pady=25, command=lambda: buttonclick(7), bg="black", fg="white")
button8 = Button(root, text="8", padx=40, pady=25, command=lambda: buttonclick(8), bg="black", fg="white")
button9 = Button(root, text="9", padx=40, pady=25, command=lambda: buttonclick(9), bg="black", fg="white")
button0 = Button(root, text="0", padx=40, pady=25, command=lambda: buttonclick(0), bg="black", fg="white")


buttonadd = Button(root, text="+", padx=39, pady=25, command=buttonadd, bg="green", fg="white")
buttonsub = Button(root, text="-", padx=39, pady=25, command=buttonsub, bg="green", fg="white")
buttonmult = Button(root, text="x", padx=39, pady=25, command=buttonmult, bg="green", fg="white")
buttondiv= Button(root, text="/", padx=39, pady=25, command=buttondiv, bg="green", fg="white")
buttonequal = Button(root, text="=", padx=39, pady=25, command=buttonequal, bg="red", fg="white")
buttonclear = Button(root, text="Clear", padx=32, pady=25, command=buttonclear, bg="blue", fg="white")
buttonraisetopower= Button(root, text="^", padx=39, pady=25, command=buttonraisetopower, bg="green", fg="white")
buttonsqrt= Button(root, text="a^(1/2)", padx=27, pady=25, command=buttonsqrt, bg="green", fg="white")
# put buttons on screen

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonadd.grid(row=5, column=0)
buttonclear.grid(row=4, column=2)
buttonequal.grid(row=5, column=2 )

buttonsub.grid(row=6, column=0)
buttonmult.grid(row=6, column=1)
buttondiv.grid(row=6, column=2)
buttonraisetopower.grid(row=4, column=1)
buttonsqrt.grid(row=5, column=1)

root.mainloop()







