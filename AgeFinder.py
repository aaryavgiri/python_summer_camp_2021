from tkinter import *

def age():
    res = int(2022) - int(e1.get())
    myText.set(res)



master=Tk()
myText = StringVar()

Label(master, text="birthyear").grid(row=0, sticky=W)
Label(master, text="result").grid(row=2, sticky=W)
result = Label(master, text="", textvariable = myText).grid(row=2, column=1, sticky=W)

e1 = Entry(master)
e1.grid(row=1, sticky=W)



b = Button(master, text="calculate", command=age)
b.grid(row=0, column=2, columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

mainloop()