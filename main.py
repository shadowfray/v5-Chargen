#Shadowfray
#V5 Character Generator
#A character generator based on the rules for Vampire 5th Edition by Paradox

from pathlib import Path
import os
from Character import character
import attributes
import skills
import printsheet
import disciplines
import predatorType
import advantagesInc

def main():
    print('WELCOME TO THE V5 CHARACTER GENERATOR')
    print('')

    #creates the vampire object we will be using
    vampire = character()

    printsheet.printcharsheet(vampire)
    
    vampire.clan = pickClan()
    vampire.setDisciplines(vampire.clan)

    #Handles attributes
    attributes.assignAttributes(vampire)
    vampire.calculations()

    #Handles skills
    buildchoice = skills.buildtype()
    skills.assignSkills(vampire, buildchoice)

    #convictions
    convictions(vampire)
    
    #disciplines - 2 dots in one, 1 dot in one
    disciplines.disciplinesChoice(vampire)
    
    #predator type
    predatorType.predatorPicker(vampire)

    #sets advantages
    #TO DO
    #advantagesInc.pickAdv(vampire)

    #advantages (7 pts), flaws (2 pts)

    #XP applied
    #TO DO

    printsheet.printcharsheet(vampire)

    #save a file of the character autoamtically
    #TO DO

def pickClan():
    #Pick clan for the character
    clans = ['banu haqim', 'brujah', 'gangrel', 'hecata', 'caitiff',
             'lasombra', 'malkavian', 'ministry', 'nosferatu', 'ravnos',
             'toreador', 'tremere', 'tzimisce', 'ventrue', 'thinblood']
    
    while True:
        print('Please pick your clan')
        print('Input "clans" to see all clans')
        claninput = str(input('> ')).lower()

        if claninput in clans:
            clanchoice = claninput
            break
        elif claninput == 'clans':
            for i in clans:
                print(i.capitalize() ,',',end='')
            print()

    return clanchoice

def convictions(vampire):
    print()
    while True:
        print('Please write one to three convictions. Enter "quit" when you are finished')
        convictioninput = str(input('> ')).lower()
        print()
        
        if convictioninput == 'quit' and len(vampire.convictions) > 0:
            break

        elif convictioninput != 'quit':
            vampire.convictions.append(convictioninput)

    while len(vampire.convictions) != len(vampire.touchstones):
        print('Please write a touchstone for each conviction  the order you wish them to relate')
        TSinput = str(input('> ')).lower()
        print()
        
        vampire.touchstones.append(TSinput)

    vampire.humanity = 7

    
#main()

