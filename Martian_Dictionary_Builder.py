#Martian's Technology Dictionary Search

import csv
from tkinter import *
import tkinter.messagebox as box

master = Tk()

#First Interface - earch entry

label0 = Label(master, text = 'Number', relief = 'groove', width = 40)
Number = Entry(master, relief = 'groove', width = 40)

label1 = Label(master, text = 'Word', relief = 'groove', width = 40)
Word = Entry(master, relief = 'groove', width = 40)

label2 = Label(master, text = 'Definition', relief = 'groove', width = 40)
Definition = Entry(master, relief = 'groove', width = 40)

label3 = Label(master, text = 'Citation', relief = 'groove', width = 40)
Citation = Entry(master, relief = 'groove', width = 40)

label4 = Label(master, text = 'Natural Use', relief = 'groove', width = 40)
Natural = Entry(master, relief = 'groove', width = 40)

#write to file function
def write():
    
    #Define Variavles
    Numbers = str(Number.get())
    Words = str(Word.get())
    Definitions = str(Definition.get())
    Citations = str(Citation.get())
    Naturals = str(Natural.get())
    
    #Openfile
    with open('MTD.csv', 'a') as csvfile:
    #define fieldnames
        fieldnames = ['Numbers', 'Words', 'Definitions', 'Citations', 'Naturals']
    #define writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #Write
        writer.writerow({'Numbers':Numbers, 'Words':Words, 'Definitions':Definitions, 'Citations':Citations, 'Naturals':Naturals})

#Button to run write
b1 = Button(master, text = 'Enter Information', relief = 'groove', width = 25, command=write)

#function two to clear the entry widgets
def clear():
    Number.delete(0, END)
    Word.delete(0, END)
    Definition.delete(0, END)
    Citation.delete(0, END)
    Natural.delete(0, END)
                        
#button to run function clear
b2 = Button(master, text = 'Store New Word', relief = 'groove', width = 25, command=clear)

#Geometry
label0.grid( row = 1, column = 1, padx = 10 )
label1.grid( row = 2, column = 1, padx = 10 )
label2.grid( row = 3, column = 1, padx = 10 )
label3.grid( row = 4, column = 1, padx = 10 )
label4.grid( row = 5, column = 1, padx = 10 )
Number.grid( row = 1, column = 2, padx = 10 )
Word.grid( row = 2, column = 2, padx = 10 )
Definition.grid( row = 3, column = 2, padx = 10 )
Citation.grid( row = 4, column = 2, padx = 10 )
Natural.grid( row = 5, column = 2, padx = 10 )
b1.grid( row = 6, column = 1, columnspan = 2)
b2.grid( row = 7, column = 1, columnspan = 2)

#Static Properties
master.title('Martian Language Database')
