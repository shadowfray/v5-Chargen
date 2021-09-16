#set your skills

from Character import character
import printsheet

def buildtype():
    #picks the build type from the three kinds avaliable
    #returns them as a Dict where the keys are the skill levels
    
    skillSpread = {1:0,2:0,3:0,4:0}
    
    print('What build type would you like?')
    print('[J]ack of all trades: One skill at 3, eight skills at 2, ten skills at 1.')
    print('[B]alanced: Three skills at 3, five skills at 2, seven skills at 1.')
    print('[S]pecialist: One skill at 4, three skills at 3, three skills at 2, three skills at 1.')
    while True:
        spreadinput = str(input('> ')).lower()
        if spreadinput == 'j':
            skillSpread[3] = 1
            skillSpread[2] = 8
            skillSpread[1] = 10
        if spreadinput == 'b':
            skillSpread[3] = 3
            skillSpread[2] = 5
            skillSpread[1] = 7
        if spreadinput == 's':
            skillSpread[4] = 1
            skillSpread[3] = 3
            skillSpread[2] = 3
            skillSpread[1] = 3
        return skillSpread
        
def assignSkills(vampire, skillSpread):
    skillval = 4
    #Handles non Specialist spreads to avoid infinite loops
    if skillSpread[4] == 0:
        skillval = 3
        
    choice = ''
    skills = ['academics', 'animalken', 'athletics', 'awareness',
              'brawl', 'etiquette', 'craft', 'insight', 'finance',
              'drive', 'intimidation', 'investigation', 'firearms',
              'leadership', 'medicine', 'larceny', 'performance',
              'occult', 'melee', 'persuasion', 'politics',
              'stealth', 'streetwise', 'science', 'survival',
              'subterfuge', 'technology']

    print('')
    print('Assign Skills:')
    print('Input "skills" to see all skills.')
    print('Input "sheet" to see your current sheet.')

    while skillSpread != {1:0,2:0,3:0,4:0}:
        print()

        if choice == 'skills':
            for i in skills:
                print(i,',',end='')
            print()

        elif choice == 'sheet':
            printsheet.printcharsheet(vampire)

        #Handles setting a skill to 4 dots
        if skillSpread[4] > 0 and skillval == 4:
            if choice in skills:
                checker = improveSkills(choice, 4, vampire, True)
                if checker == True:
                    skillSpread[4] -= 1
                if skillSpread[4] == 0:
                    skillval -= 1

        #Handles setting skills to 3 dots
        elif skillSpread[3] > 0 and skillval == 3:
            if choice in skills:
                checker = improveSkills(choice, 3, vampire, True)
                if checker == True:
                    skillSpread[3] -= 1
                if skillSpread[3] == 0:
                    skillval -= 1

        #Handles setting skills to 2 dots           
        elif skillSpread[2] > 0 and skillval == 2:
            if choice in skills:
                checker = improveSkills(choice, 2, vampire, True)
                if checker == True:
                    skillSpread[2] -= 1
                if skillSpread[2] == 0:
                    skillval -= 1

        #Handles setting skills to 1 dot
        elif skillSpread[1] > 0 and skillval == 1:
            if choice in skills:
                checker = improveSkills(choice, 1, vampire, True)
                if checker == True:
                    skillSpread[1] -= 1

        #debugging message:
        #print('skill spread', skillSpread)

        #handles a case where there are no more skill points but bc of the set up
        #it asks one more time but that last ask does nothing
        if skillSpread[1] == 0:
            break
        
        print(f'Please choose a skill to set to {skillval}')
        print(f'You have {skillSpread[skillval]} choice(s) remaining')
        #We put the input down here so that our messages print in the proper orders
        choice = str(input('> ')).lower()

    #pick specialities
    spec_skills = []
    if vampire.academics > 0:
        spec_skills.append('academics')
    if vampire.craft > 0:
        spec_skills.append('craft')
    if vampire.performance > 0:
        spec_skills.append('performance')
    if vampire.science > 0:
        spec_skills.append('science')

    while True:
            print('Please write in a specialty of your choosing to be recorded.')
            print('What skill should this be in?')
            skillchoice = str(input('> ')).lower()
            if skillchoice in skills:
                print('What is your specialty?')
                specinput = str(input('> ')).lower()
                vampire.specialties[skillchoice] = specinput
                break
        
    while len(spec_skills) >0:
        print(f'Please pick a specialty for {spec_skills[0]}')
        specChoice = str(input('> ')).lower()
        vampire.specialties[spec_skills[0]] = specChoice
        spec_skills.pop(0)

def improveSkills(skill_choice: str, val: int, vampire, chargen=False):
    #works the same way as improveAttributes()

    if skill_choice == 'athletics' and ((chargen != (vampire.athletics == 0))
                                           or (chargen and (vampire.athletics == 0)
                                               or ((not chargen) and (vampire.athletics == 0)))):
        vampire.athletics += val
        return True

    if skill_choice == 'animalken' and ((chargen != (vampire.animalKen == 0))
                                           or (chargen and (vampire.animalKen == 0)
                                               or ((not chargen) and (vampire.animalKen == 0)))):
        vampire.animalKen += val
        return True

    if skill_choice == 'academics' and ((chargen != (vampire.academics == 0))
                                           or (chargen and (vampire.academics == 0)
                                               or ((not chargen) and (vampire.academics == 0)))):
        vampire.academics += val
        return True

    if skill_choice == 'awareness' and ((chargen != (vampire.awareness == 0))
                                           or (chargen and (vampire.awareness == 0)
                                               or ((not chargen) and (vampire.awareness == 0)))):
        vampire.awareness += val
        return True

    if skill_choice == 'brawl' and ((chargen != (vampire.brawl == 0))
                                           or (chargen and (vampire.brawl == 0)
                                               or ((not chargen) and (vampire.brawl == 0)))):
        vampire.brawl += val
        return True

    if skill_choice == 'etiquette' and ((chargen != (vampire.etiquette == 0))
                                           or (chargen and (vampire.etiquette == 0)
                                               or ((not chargen) and (vampire.etiquette == 0)))):
        vampire.etiquette += val
        return True

    if skill_choice == 'craft' and ((chargen != (vampire.craft == 0))
                                           or (chargen and (vampire.craft == 0)
                                               or ((not chargen) and (vampire.craft == 0)))):
        vampire.craft += val
        return True

    if skill_choice == 'insight' and ((chargen != (vampire.insight == 0))
                                           or (chargen and (vampire.insight == 0)
                                               or ((not chargen) and (vampire.insight == 0)))):
        vampire.insight += val
        return True

    if skill_choice == 'finance' and ((chargen != (vampire.finance == 0))
                                           or (chargen and (vampire.finance == 0)
                                               or ((not chargen) and (vampire.finance == 0)))):
        vampire.finance += val
        return True
              
    if skill_choice == 'drive' and ((chargen != (vampire.drive == 0))
                                           or (chargen and (vampire.drive == 0)
                                               or ((not chargen) and (vampire.drive == 0)))):
        vampire.drive += val
        return True

    if skill_choice == 'intimidation' and ((chargen != (vampire.intimidation == 0))
                                           or (chargen and (vampire.intimidation == 0)
                                               or ((not chargen) and (vampire.intimidation == 0)))):
        vampire.intimidation += val
        return True

    if skill_choice == 'investigation' and ((chargen != (vampire.investigation == 0))
                                           or (chargen and (vampire.investigation == 0)
                                               or ((not chargen) and (vampire.investigation == 0)))):
        vampire.investigation = val
        return True

    if skill_choice == 'firearms' and ((chargen != (vampire.firearms == 0))
                                           or (chargen and (vampire.firearms == 0)
                                               or ((not chargen) and (vampire.firearms == 0)))):
        vampire.firearms += val
        return True

    if skill_choice == 'leadership' and ((chargen != (vampire.leadership == 0))
                                           or (chargen and (vampire.leadership == 0)
                                               or ((not chargen) and (vampire.leadership == 0)))):
        vampire.leadership += val
        return True

    if skill_choice == 'medicine' and ((chargen != (vampire.medicine == 0))
                                           or (chargen and (vampire.medicine == 0)
                                               or ((not chargen) and (vampire.medicine == 0)))):
        vampire.medicine += val
        return True

    if skill_choice == 'larceny' and ((chargen != (vampire.larceny == 0))
                                           or (chargen and (vampire.larceny == 0)
                                               or ((not chargen) and (vampire.larceny == 0)))):
        vampire.larceny += val
        return True

    if skill_choice == 'performance' and ((chargen != (vampire.performance == 0))
                                           or (chargen and (vampire.performance == 0)
                                               or ((not chargen) and (vampire.performance == 0)))):
        vampire.performance += val
        return True

    if skill_choice == 'occult' and ((chargen != (vampire.occult == 0))
                                           or (chargen and (vampire.occult == 0)
                                               or ((not chargen) and (vampire.occult == 0)))):
        vampire.occult += val
        return True

    if skill_choice == 'melee' and ((chargen != (vampire.melee == 0))
                                           or (chargen and (vampire.melee == 0)
                                               or ((not chargen) and (vampire.melee == 0)))):
        vampire.melee += val
        return True

    if skill_choice == 'persuasion' and ((chargen != (vampire.persuasion == 0))
                                           or (chargen and (vampire.persuasion == 0)
                                               or ((not chargen) and (vampire.persuasion == 0)))):
        vampire.persuasion += val
        return True

    if skill_choice == 'politics' and ((chargen != (vampire.politics == 0))
                                           or (chargen and (vampire.politics == 0)
                                               or ((not chargen) and (vampire.politics == 0)))):
        vampire.politics += val
        return True

    if skill_choice == 'stealth' and ((chargen != (vampire.stealth == 0))
                                           or (chargen and (vampire.stealth == 0)
                                               or ((not chargen) and (vampire.stealth== 0)))):
        vampire.stealth += val
        return True

    if skill_choice == 'streetwise' and ((chargen != (vampire.streetwise == 0))
                                           or (chargen and (vampire.streetwise == 0)
                                               or ((not chargen) and (vampire.streetwise== 0)))):
        vampire.streetwise += val
        return True

    if skill_choice == 'science' and ((chargen != (vampire.science == 0))
                                           or (chargen and (vampire.science == 0)
                                               or ((not chargen) and (vampire.science== 0)))):
        vampire.science += val
        return True

    if skill_choice == 'survival' and ((chargen != (vampire.survival == 0))
                                           or (chargen and (vampire.survival == 0)
                                               or ((not chargen) and (vampire.survival== 0)))):
        vampire.survival += val
        return True

    if skill_choice == 'subterfuge' and ((chargen != (vampire.subterfuge == 0))
                                           or (chargen and (vampire.subterfuge == 0)
                                               or ((not chargen) and (vampire.subterfuge== 0)))):
        vampire.subterfuge += val
        return True

    if skill_choice == 'technology' and ((chargen != (vampire.technology == 0))
                                           or (chargen and (vampire.technology == 0)
                                               or ((not chargen) and (vampire.technology== 0)))):
        vampire.technology += val
        return True
    return False
