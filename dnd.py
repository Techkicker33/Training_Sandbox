import random

#----------------------------------------------------------------------------------------------------------
PlayerRaces =['Elf','Dwarf','Human','Tiefling','Halfling','Gnome','Dragonborn','Aasimar','Orc','Goaliath']
PlayerClass=['Fighter','Wizard','Warlock','Rogue','Druid','Ranger','Sorceror','Cleric','Paladin','Barbarian','Monk']
CharAttr=['Strength','Charisma','Dexterity','Wisdom','Intelligence','Constitution']
CurCha={}
RacialMod={
    'Elf': '[0,0,2,0,0,0]',
    'Dwarf': '[0,0,0,0,0,2]',
    'Human': '[1,1,1,1,1,1]',
    'Tiefling': '[0,0,0,0,1,0]',
    'Halfling': '[0,0,2,0,0,0]',
    'Gnome': '[0,0,0,0,2,0]',
    'Dragonborn': '[2,0,0,0,0,1]',
    'Aasimar': '[0,1,0,0,0,2]',
    'Orc': '[2,0,0,0,0,1]',
    'Goaliath': '[2,0,0,1,0,0]'
}
stack=[] #final stat stack

'''Overall goal is to build a new character stat generator that will roll initial numbers, then select initial player race.
After Race, select class.  With this information, then create the final list of Player Stats.'''
#----------------------------------------------------------------------------------------------------------
#create list of 6 values made by rolling 4d6 and dropping the lowest. sum values from each roll.

def roll_dice():
    rolls=[]
    for i in range(1,5):
        roll=random.randint(1,6)
        rolls.append(roll)
    if len(rolls)>3:
        rolls.sort(reverse=True) #sort highest to lowest
        rolls.pop() #remove lowest of four numbers
    #print(rolls)
    return rolls
#-------------------------------------------------------------------------------------------------------------

def updatelog(rolled_numbs):
    filename ='rolledhistory.csv'
    with open(filename,'a') as file_object:
        file_object.write(str(rolled_numbs)+ '\n')
    
#-------------------------------------------------------------------------------------------------------------
total_roll = int(input('Enter the number of groups you\'d like to roll: '))

all_stats = []  # List to hold all groups
current_group = []  # Temporary list for each group

while len(all_stats) < total_roll:
    total = sum(roll_dice())
    current_group.append(total)
    if len(current_group) == 6:
        print('Your character will start with the following player stats ' + str(current_group) + '\n')
        updatelog(current_group)
        all_stats.append(current_group)
        current_group = []
#-------------------------------------------------------------------------------------------------------------
"""
SelectRace=input('Select one of the following Races.\n' + str(PlayerRaces)+'\n').lower()

print('You have selected '+str(SelectRace).title())

print(str(SelectRace).title() + ' recieves the following Racial bonuses '+str(RacialMod[SelectRace.title()]))
"""