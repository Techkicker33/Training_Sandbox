import turtle as t
import random
t.bgcolor("lightgrey")
t.pensize(3)
def tur_turn():
    direction=random.randint(1,6)
    if direction == 2:
        t.right(90)
        t.color("blue")
    elif direction == 3:
        t.left(90)
        t.color("red")
    elif direction == 4:
        t.right(180)
        t.color("orange")
    elif direction == 5:
        t.right(45)
        t.color("green")
    elif direction == 6:
        t.left(45)
        t.color("purple")
    else:
        print('move forward')
        t.color("black")
        t.stamp()

def tur_move():
    move=random.randint(0,10)
    t.forward(move*3.14159)
    return move
count = 0
while count <= 199:
    tur_turn()
    tur_move()
    count += 1
    print(count)
