import random
#----------------------------------------------------------------------------------------------------------
PlayerRaces =('Elf','Dwarf','Human','Teifling','Halfling','Gnome','Dragonborn','Aasimar','Orc','Goaliath')
PlayerClass=('Fighter','Wizard','Warlock','Rogue','Druid','Ranger','Sorceror','Cleric','Paladin','Barbarian','Monk')
CharAttr=('Strength','Charisma','Dexterity','Wisdom','Intelligence','Constitution')


RacialMod={'Elf':'','Dwarf':'','Human':'','Teifling':'','Halfling':'','Gnome':'','Dragonborn':'','Aasimar':'','Orc':'','Goaliath':''}
stack=[] #final stat stack
RollHist={} #log of rolls
'''Overal goal is to build a new character stat generator that will roll initial numbers, then select initial player race.
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
while len(stack)<6:
    total=sum(roll_dice())
    rolls=0
    stack.append(total)
    if len(stack)==6:
        print('Your character will start with the following player stats '+str(stack)+'\n')
    if len(stack)>6:
        print('there was an error. re-set to 0')
        stack=[]
#------------------------------------------------------------------------------------

SelectRace=input('Select one of the following Races.\n' + str(PlayerRaces)+'\n').lower()

print('You have selected '+str(SelectRace).title())
print(str(SelectRace).title() + ' recieves the following Racial bonuses')

