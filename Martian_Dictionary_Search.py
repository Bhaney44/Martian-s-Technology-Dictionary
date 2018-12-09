#Martian's Technology Dictionary Search

import csv
from tkinter import *
import tkinter.messagebox as box

master = Tk()

#First Interface

label1 = Label(master, text = 'Word', relief = 'groove', width = 40)
label2 = Label(master, text = 'Definition', relief = 'groove', width = 40)

e1 = Entry(master, relief = 'groove', width = 40)
e2 = Text(master, relief = 'groove', width = 40, height = 10, borderwidth = 2)

def search():
        csvfile = open('MTD.csv', 'r')
        read = csv.reader(csvfile)
        contains_keyword = False
        for row in read:
                if str(e1.get()) in row:
                        contains_keyword = True
                        break
        if contains_keyword:
                e2.insert("1.0", row, 'r')
        else:
                box.showinfo('Search Result', 'Not Found')
                master.mainloop()


def clear():
        e1.delete(0, END)
        e2.delete(1.0, END)

#Button for command function search
b1 = Button(master, text = 'Search', relief = 'groove', command=search)
b2 = Button(master, text = 'Clear', relief = 'groove', command=clear)

#Geometry
label1.grid( row = 1, column = 1, padx = 10 )
e1.grid( row = 2, column = 1, padx = 10 )
b1.grid( row = 3, column = 1, columnspan = 1)

label2.grid( row = 1, column = 2, padx = 10 )
e2.grid( row = 2, column = 2, padx = 10 )
b2.grid( row = 3, column = 2, columnspan = 2)










#Static Properties
master.title('Martian Language Search')
