#set your attributes via two steps
from Character import character
import printsheet

def assignAttributes(vampire):
    #used to keep track of how many attributes have been set to 3 and to 2
    threeCounter, twoCounter = 0,0

    attributes = ['strength', 'dexterity', 'stamina',
                  'charisma', 'manipulation', 'composure',
                  'intelligence','wits','resolve']
    print('')
    print('Assign attributes:')
    print('Input "attributes" to see all attributes')
    print('Input "sheet" to see your current sheet')
          
    while True:
        print('Choose an attribute to set to 4')
        attchoice = str(input('> ')).lower()
        if attchoice in attributes:
            change = improveAttributes(attchoice, 4, vampire, True)
            if change == True:
                break
        elif attchoice == 'attributes':
            for i in attributes:
                print(i,',',end='')
            print()
        elif attchoice == 'sheet':
            printsheet.printcharsheet(vampire)
    print()
    
    while threeCounter < 3:
        print('Choose an attribute to set to 3')
        print(f'{3 - threeCounter} choices remain')
        attchoice = str(input('> ')).lower()
        if attchoice in attributes:
            change = improveAttributes(attchoice, 3, vampire, True)
            if change == True:
                threeCounter += 1
        elif attchoice == 'attributes':
            for i in attributes:
                print(i,',',end='')
            print()
        elif attchoice == 'sheet':
            printsheet.printcharsheet(vampire)
    print()
    
    while twoCounter < 4:
        print('Choose an attribute to set to 2')
        print(f'{4 - twoCounter} choices remain')
        attchoice = str(input('> ')).lower()
        if attchoice in attributes:
            change = improveAttributes(attchoice, 2, vampire, True)
            if change == True:
                twoCounter += 1
        elif attchoice == 'attributes':
            for i in attributes:
                print(i,',',end='')
            print()
        elif attchoice == 'sheet':
            printsheet.printcharsheet(vampire)
    print()

    while True:
        print('Choose an attribute to set to 1')
        attchoice = str(input('> ')).lower()
        if attchoice in attributes:
            change = improveAttributes(attchoice, 1, vampire, True)
            if change == True:
                break
        elif attchoice == 'attributes':
            for i in attributes:
                print(i,',',end='')
            print()
        elif attchoice == 'sheet':
            printsheet.printcharsheet(vampire)
    print()
    print('Are you happy with your results? [y/n]')
    happy = str(input('> ')).lower()
    if happy == 'no' or happy == 'n':
        vampire.resetAttributes()
        assignAttributes(vampire)
    print()

    printsheet.printcharsheet(vampire)

def improveAttributes(attribute_choice: str, val: int, vampire, chargen=False):
    #the zero attribute determines if a stat can only be changed if it is = 0.
    #chargen = False means we can simply edit them as we wish without restriction
    #we use the following logic gate to make sure that it is 0:
    #R and ((XOR P Q) or (P and Q) or (NOT P and Q))

    #Returns `True` if a change is made, otherwise it returns `False`
    if attribute_choice == 'strength' and ((chargen != (vampire.strength == 0))
                                           or (chargen and (vampire.strength == 0)
                                               or ((not chargen) and (vampire.strength == 0)))):
        vampire.strength += val
        return True
    if attribute_choice == 'dexterity' and ((chargen != (vampire.dexterity == 0))
                                           or (chargen and (vampire.dexterity == 0)
                                               or ((not chargen) and (vampire.dexterity == 0)))):
        vampire.dexterity += val
        return True
    if attribute_choice == 'stamina' and ((chargen != (vampire.stamina == 0))
                                           or (chargen and (vampire.stamina == 0)
                                               or ((not chargen) and (vampire.stamina == 0)))):
        vampire.stamina += val
        return True
    if attribute_choice == 'charisma' and ((chargen != (vampire.charisma == 0))
                                           or (chargen and (vampire.charisma == 0)
                                               or ((not chargen) and (vampire.charisma == 0)))):
        vampire.charisma += val
        return True
    if attribute_choice == 'manipulation' and ((chargen != (vampire.manipulation == 0))
                                           or (chargen and (vampire.manipulation == 0)
                                               or ((not chargen) and (vampire.manipulation == 0)))):
        vampire.manipulation += val
        return True
    if attribute_choice == 'composure' and ((chargen != (vampire.composure == 0))
                                           or (chargen and (vampire.composure == 0)
                                               or ((not chargen) and (vampire.composure == 0)))):
        vampire.composure += val
        return True
    if attribute_choice == 'intelligence' and ((chargen != (vampire.intelligence == 0))
                                           or (chargen and (vampire.intelligence == 0)
                                               or ((not chargen) and (vampire.intelligence == 0)))):
        vampire.intelligence += val
        return True
    if attribute_choice == 'wits' and ((chargen != (vampire.wits == 0))
                                           or (chargen and (vampire.wits == 0)
                                               or ((not chargen) and (vampire.wits == 0)))):
        vampire.wits += val
        return True
    if attribute_choice == 'resolve' and ((chargen != (vampire.resolve == 0))
                                           or (chargen and (vampire.resolve == 0)
                                               or ((not chargen) and (vampire.resolve == 0)))):
        vampire.resolve += val
        return True
    return False
