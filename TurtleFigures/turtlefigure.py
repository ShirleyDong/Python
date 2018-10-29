from turtle import *
from random import randint
import math


def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end 

def tree4(n, l,pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(90)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)

#end

def fern(n,l,pen):
    #termination
    if n==0 or l<2:
        return
    #endif

    pen.forward(2*l/3)
    pen.right(45); fern(n-1, l/2, pen);pen.left(45)
    pen.forward(2*l/3)
    pen.left(30);fern(n-1, l/2, pen);pen.right(30);
    pen.forward(2*l/3)
    pen.right(10);fern(n-1,0.8*l, pen);pen.left(10)
    pen.backward(2*l)
#end

def koch(n,l,pen):
    #termination
    if n==0 or l<2:
        pen.forward(l)
        return
    #endif

    koch(n-1,l/3, pen)
    pen.left(60)
    koch(n-1, l/3, pen)
    pen.right(120)
    koch(n-1, l/3, pen)
    pen.left(60)
    koch(n-1, l/3, pen)
#enddef

def flake(n,l,pen):
    for i in range(3):
        koch(n, l, pen)
        pen.right(120)
    #end for
#end def

def gasket(n,l,pen):
    #termination
    if n==0 or l<2:
        for i in range(3):
            pen.forward(l)
            pen.left(120)
        #end for
        return
    #end if

    for i in range(3):
     gasket(n-1, l/2, pen)
     pen.forward(l)
     pen.left(120)
    #end for
#end def

     
def swiss(n,l,pen):
    #termination
    if n==0 or l<3:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        #end for
        return
    #end if

    for i in range(4):
     swiss(n-1, l/3, pen)
     pen.forward(l)
     pen.left(90)
    #end for
#end def

def squareGasket(n,l,pen):
    #termination
    if n==0 or l<2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        #end for
        return
    #end if

    for i in range(4):
     squareGasket(n-1, l/3, pen)
     pen.forward(l)
     pen.left(90)
    #end for
     pen.forward(l/3)
     pen.left(90)
     pen.forward(l/3)
     pen.right(90)
     squareGasket(n-1, l/3, pen)
     pen.right(90)
     pen.forward(l/3)
     pen.right(90)
     pen.forward(l/3)
     pen.right(180)
#end def


def circle2(n,l,pen):
     if n==0 or l<2:
        for i in range(4):
            pen.circle(l, 90)
        #end for
        return
    #end if
     for i in range(2):
          circle2(n-1, l/3, pen)
          pen.circle(l,90)
          circle2(n-1, l/2, pen)
          pen.circle(l,90)
     #end for
#end circle2

def circle3(n,l,pen):
     if n==0 or l<2:
          pen.circle(l)
        #end for
          return
    #end if
     for i in range(3):
          circle3(n-1,l/2,pen)
          pen.circle(l,120)
     #end for
#end circle3

#personal figures
def tree5(n, l, pen):
    if n==0 or l<2 :
        return
    #endif
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colormode(255)
    pen.color(r,g,b)
    pen.forward(l)
    pen.left(60)
    tree5(n-1, l/2, pen)
    pen.right(30)
    tree5(n-1, l/2, pen)
    pen.right(30)
    tree5(n-1, l/2, pen)
    pen.right(30)
    tree5(n-1, l/2, pen)
    pen.right(30)
    tree5(n-1, l/2, pen)
    pen.left(60)
    pen.backward(l)
#end

def treeUnit(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     if n==1:
         pen.color("green")
     else:
         pen.color("#a6363c")          
     pen.width(n)
     pen.forward(l)
     pen.right(20)
     treeUnit(n-1, l-9, pen)
     pen.left(40)
     treeUnit(n-1, l-9, pen)
     pen.right(20)
     if n==1:
         pen.color("green")
     else:
         pen.color("#a6363c")
     pen.backward(l)

#end 

def my_tree(n, l, pen):
    pen.left(90)
    pen.up()
    pen.backward(200)
    pen.down()
    treeUnit(n, l, pen)
#end my_tree

           
def my_square(n, l, pen):
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
    for x in range(n*4):
        pen.color(colors[x % 6])
        pen.width(x / 100 + 1)
        pen.forward(x + l)
        pen.left(91)
#end myTurtle


def leaf(l, r, g, b, pen):
    pen.color(r, g, b)
    pen.begin_fill()
    for i in range(360):
        length = (90 - abs(90 - float(i % 180))) / l
        pen.forward(length)
        pen.right(1)
    pen.end_fill()
#endleaf
    
def my_leaf(n, l, pen):
    colormode(255)
    for i in range(n):
        r = 255
        g = randint(0, 100)
        b = randint(0, 100)
        leaf(l, r, g, b, pen)
        pen.left(360 / n)
#end my_leaf



     
