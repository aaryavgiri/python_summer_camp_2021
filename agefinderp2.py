from tkinter import *


class SimpleGUI:

    def calc(self):
        res = 2022 - int(self.year.get())
        print(res)
        self.text1.set(res)

    def __init__(self, master):
        self.master = master
        master.title('Simple GUI')


# main
master = Tk()  # creates an instance of GUI
self = SimpleGUI(master)
self.labelName = Label(master, text='Name')
self.labelName.grid(row=1, column=1)

self.name = Entry(master)
self.name.grid(row=1, column=5)

self.labelYear = Label(master, text='Year')
self.labelYear.grid(row=10, column=1)
self.year = Entry(master)
self.year.grid(row=10, column=5)


self.text1 = StringVar()

self.labelAgeText = Label(master, text='Age = ')
self.labelAgeText.grid(row=20, column=1)

self.labelAge = Label(master, text="",textvariable=self.text1)
self.labelAge.grid(row=20, column=2)

self.exit = Button(master, text='EXIT', command=master.quit)
self.exit.grid(row=30, column=2)

self.calculate = Button(master, text='Calculate', command=self.calc)
self.calculate.grid(row=30, column=1)
e1 = Entry(master)
e2 = Entry(master)


#self.root = Tk()

master.mainloop()  # makes the graphics window stay up