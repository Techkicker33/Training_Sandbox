import turtle as t
import math


def square(size):
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)

#square(55)
side = 0
def drawSquare():
    while side<101:
        side+=3
        square(side)
        print(side)
drawSquare()

"""def triangle(sideA,sideB):
    sideC=math.sqrt(sideA**2+sideB**2)
    t.forward(sideA)
    t.right(sideA*math.sin(sideB/sideC))
    t.forward(sideB)
    t.right(sideB*math.sin(sideC/sideA))
    t.forward(sideC)
    
    
print(triangle(30,40))"""
    


