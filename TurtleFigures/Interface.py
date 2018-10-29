#import modules

from tkinter import *
from tkinter.ttk import Entry, OptionMenu
from turtlefigure import *
from turtle import *
from random import randint
import math


root  = Tk()
root.title("Turtle Drawer")
root.geometry("400x200+300+300")

shapes = ["tree", "tree4", "fern", "koch", "flake", "gasket", "swiss", "squareGasket", "circle2", "circle3", "colorTree", "colorSquare", "flower" ]

pen = Pen()
pen.color("white")
pen.speed(0)
pen.width(1)
tp = pen.pos()



screen = Screen()
screen.bgcolor("black")


#make the interface

#========================
#clear the textbox
#========================
def clearF(): 
    #empty the selections of shapes
    orderStr.set("")
    lengthStr.set("")
#end clearF

#========================
#setcolor
#========================

def ColorF():
    penCoStr = penColorStr.get()
    bgCoStr = bgColorStr.get()
    print(penCoStr + ","+ bgCoStr)
    pen.color(penCoStr)
    screen.bgcolor(bgCoStr)
    
#end ColorF
    
#========================
#draw the turtles
#========================
def DrawF():
    #get the order and length
    print(str(orderStr),str(lengthStr),str(turtleStr))
    n = int(orderStr.get())
    l = int(lengthStr.get())
    #get the turtleName
    turtleName = turtleStr.get()
    print(n,l,turtleName)
    SetPos()
    print(pen.pos())
    pen.color("white")
    #draw the turtles
    ColorF()
    if turtleName == "tree":
        tree(n, l, pen)
    elif turtleName == "tree4":
        tree4(n, l, pen)
    elif turtleName == "fern":
        fern(n, l, pen)
    elif turtleName == "koch":
        koch(n, l, pen)
    elif turtleName == "flake":
        flake(n, l, pen)
    elif turtleName == "gasket":
        gasket(n, l, pen)       
    elif turtleName == "swiss":
        swiss(n, l, pen)
    elif turtleName == "squareGasket":
        squareGasket(n, l, pen)
    elif turtleName == "circle2":
        circle2(n, l, pen)
    elif turtleName == "circle3":
        circle3(n, l, pen)
    elif turtleName == "colorTree":
        my_tree(n, l, pen)
    elif turtleName == "colorSquare":
        my_square(n, l, pen)
    elif turtleName == "flower":
        my_leaf(n, l, pen)
    
    #endif
#end DrawF
            
#=======
#setInfo
#=======
def infoF():
    turtleName = turtleStr.get()
    if turtleName == "tree":
        infoLabel.config(text = "This is tree")
    elif turtleName == "tree4":
        infoLabel.config(text = "This is tree4")
    elif turtleName == "fern":
        infoLabel.config(text = "This is fern")
    elif turtleName == "koch":
        infoLabel.config(text = "This is koch")
    elif turtleName == "flake":
        infoLabel.config(text = "This is flake")
    elif turtleName == "gasket":
        infoLabel.config(text = "This is gasket")       
    elif turtleName == "swiss":
        infoLabel.config(text = "This is swiss")
    elif turtleName == "squareGasket":
        infoLabel.config(text = "This is squareGasket")
    elif turtleName == "circle2":
        infoLabel.config(text = "This is circle2")
    elif turtleName == "circle3":
        infoLabel.config(text = "This is circle3")
    elif turtleName == "colorTree":
        infoLabel.config(text = "This is colorTree")
    elif turtleName == "colorSquare":
        infoLabel.config(text = "This is colorSquare")
    elif turtleName == "flower":
        infoLabel.config(text = "This is flower")
#end infoF

#=============        
#Clear Screen
#=============
def ClearScrF():
    infoF()
    ColorF()
    #pen.clear()
    pen.reset()
    pen.setpos(tp)
    ColorF()
    
#end resetscreen


#====================
#setStartPosition
#====================
def SetPos():
    pen.color("black")
    x = float(xSpinbox.get())
    y = float(xSpinbox.get())
    pen.setx(x)
    pen.sety(y)
#end SetPos



#=============================
#make the interface components
#=============================
#title component
titleLabel = Label(root, text = "Turtle")
titleLabel.grid(row = 0, column = 0, columnspan = 2)

#order 
orderLabel = Label(root, text = "Order")
orderLabel.grid(row = 1, column = 0)

orderStr = StringVar()
orderEntry = Entry(root, width = 10, textvariable = orderStr)
orderEntry.grid(row = 1, column = 1)

#length 
lengthLabel = Label(root, text = "Length")
lengthLabel.grid(row = 2, column = 0)

lengthStr = StringVar()
lengthEntry = Entry(root, width = 10, textvariable = lengthStr)
lengthEntry.grid(row = 2, column = 1)

#xposition
xLabel = Label(root, text = "PenX")
xLabel.grid(row = 1, column = 2)

xSpinbox =  Spinbox(root, from_=0, to=500)
xSpinbox.grid(row = 1, column = 3)

#xposition
yLabel = Label(root, text = "PenY")
yLabel.grid(row = 2, column = 2)

YSpinbox =  Spinbox(root, from_=0, to=500)
YSpinbox.grid(row = 2, column = 3)

#pencolor 
penColorLabel = Label(root, text = "PenColor")
penColorLabel.grid(row = 3, column = 0)

penColorStr = StringVar()
penColorEntry = Entry(root, width = 10, textvariable = penColorStr)
penColorEntry.grid(row = 3, column = 1)

#backgroundColor 
bgColorLabel = Label(root, text = "BackgroundColor")
bgColorLabel.grid(row = 3, column = 2)

bgColorStr = StringVar()
bgColorEntry = Entry(root, width = 10, textvariable = bgColorStr)
bgColorEntry.grid(row = 3, column = 3)

#optionMenu
figureLabel = Label(root, text = "Figure")
figureLabel.grid(row = 4, column = 0)

turtleStr = StringVar()
turtleMenu = OptionMenu(root, turtleStr, shapes[0], *shapes)
turtleMenu.grid(row = 4, column = 1)


#button
clearButton = Button(root, text = "Clear", command = clearF)
clearButton.grid(row = 5, column = 0)

drawButton = Button(root, text = "Draw", command = DrawF)
drawButton.grid(row = 5, column = 1)

clearScrButton = Button(root, text = "ClearScreen", command = ClearScrF)
clearScrButton.grid(row = 5, column = 2)

#labelInformation
infoLabelT = Label(root, text = "Info:")
infoLabelT.grid(row = 6, column = 0)
infoLabel = Label(root, text = "Please clear the screen before you draw the figure")
infoLabel.grid(row = 7, column = 0, columnspan = 12)
#=========catchevent===========
mainloop()








