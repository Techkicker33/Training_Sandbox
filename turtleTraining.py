import turtle as t
from math import sqrt


def square(size):
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)

def triangle(a,b,):
    c=sqrt(a**2+b**2)
    print(c)
    t.forward(a)
    t.left(180-90)
    t.forward(b)
    t.left(180-30)
    t.forward(c)

#square(55)
side = 0

def drawSquare():
    while side<101:
        side+=3
        square(side)
        print(side)
#drawSquare()

triangle(30,40)
    


