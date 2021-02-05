#from tkinter import *
#from random import *

#c=0
#n=1

#def count(n):
#    global c
#    c += n 
#    entry.delete(0, 'end')
#    entry.insert(0,c)
#    print(f" {n}")

#def clickpurschase_1(n):
#    global c, entry
#    if c < 1:
#        print("Not enough clicks!")
#    elif c >= 10:
#        c = c - 10
#        print(f"Double Clicks Purchased!  {n}")
#    return n



#root=Tk()
#root.geometry('500x700')
#M=Menu(root)
#root.config(menu=M)

#m1=Menu(M,tearoff=0)
#M.add_cascade(label='Click Upgrader', menu=m1)
#m1.add_command(label='+1 points per click',command=lambda:clickpurschase_1(2))
#button = Button(text="CLICK",command=lambda:count(n))
#label = Label(text="SCORE",font = 'arial 20',bg = 'red')
#entry = Entry(root)
#label.pack(side = TOP , pady = 5)
#entry.pack(side = TOP , pady = 5)
#button.pack(side=TOP , pady = 5)
#root.mainloop()
from tkinter import *
import time

root=Tk()
root.geometry('500x700')
M=Menu(root)
root.config(menu=M)

def uiPrint():
    info()
    print("")
    print(click)
    blankLine()

def info():
    print("Double click purchases need 100 clicks!")

info()

click = 0
mult = 1
dcp1 = 0

def blankLine():
    for i in range(20):
        print("")

def purchaseDoubleClicksCommand():
    global click
    global mult
    if click < 10:
        print("Not enough clicks!")
        blankLine()
    elif click >= 10:
        mult = mult+1
        click = click - 10
        print("Double Clicks Purchased!")
        blankLine()


def count():
    global click
    global mult
    click += mult 
    entry.delete(0, 'end')
    entry.insert(0,c)


    if click == 200:
        print('''Achievement Unlocked: Junior Clicker!
        BONUS 100 clicks!''')
        click += 100

    elif click == 1000:
        print ('''Achievement Unlocked: Little Ninja Clicks!
        BONUS 200!''')
        click += 200

    elif click == 5000:
        print ('''Achievement Unlocked: Click Ninja Master!
        QUADRO CLICKS!''')
        mult = mult * 4

    elif click == 15000:
        print ('''Achievement Unlocked:  Jackie Chan Style!
        8 x Score Per Click!''')
        mult = mult * 8


root.title("Clicker! v0.1")

m1=Menu(M,tearoff=0)
M.add_cascade(label='Click Upgrader', menu=m1)
m1.add_command(label='+1 points per click',command=lambda:purchaseDoubleClicksCommand)
button = Button(text="CLICK",command=lambda:count)
label = Label(text="SCORE",font = 'arial 20',bg = 'red')
entry = Entry(root)
label.pack(side = TOP , pady = 5)
entry.pack(side = TOP , pady = 5)
button.pack(side=TOP , pady = 5)
root.mainloop()