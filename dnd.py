import random

stack=[]
#create list of 6 values made by rolling 4d6 and dropping the lowest. sum values from each roll.

def roll_dice():
    rolls=[]
    for i in range(1,5):
        roll=random.randint(1,6)
        rolls.append(roll)
    if len(rolls)>3:
        rolls.sort(reverse=True)
        rolls.pop()
    #print(rolls)
    return rolls
while len(stack)<6:
    total=sum(roll_dice())
    rolls=0
    stack.append(total)
    if len(stack)==6:
        print(stack)
    if len(stack)>6:
        print('there was an error. re-set to 0')
        stack=[]