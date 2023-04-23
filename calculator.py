from tkinter import *

def multiplyNumbers():
    res = int(e1.get())*int(e2.get())
    myText.set(res)

def substractNumbers():
    res = int(e1.get())-int(e2.get())
    myText.set(res)

def divideNumbers():
    res = int(e1.get())/int(e2.get())
    myText.set(res)
    
def addNumbers():
    res = int(e1.get())+int(e2.get())
    myText.set(res)
    
     
master = Tk()
myText = StringVar()
Label(master,text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=2, sticky=W)
result = Label(master, text="",textvariable=myText).grid(row=3, column=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

a = Button(master, text="Calculate", command= addNumbers )
a.grid(row=0, column=2, columnspan=1, rowspan=1, sticky=W+E+N+S, padx=5, pady=5)

b = Button(master, text="/", command= divideNumbers )
b.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=W+E+N+S, padx=5, pady=5)

c = Button(master, text="-", command= substractNumbers )
c.grid(row=2, column=2, columnspan=1, rowspan=1, sticky=W+E+N+S, padx=5, pady=5)

d = Button(master, text="+", command= addNumbers )
d.grid(row=3, column=2, columnspan=1, rowspan=1, sticky=W+E+N+S, padx=5, pady=5)
e = Button(master, text="x", command= multiplyNumbers )
e.grid(row=4, column=2, columnspan=1, rowspan=1, sticky=W+E+N+S, padx=5, pady=5)


mainloop()