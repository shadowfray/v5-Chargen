import advantages
import Character

predatorList = ['Alleycat',
                'Bagger',
                'Blood Leech',
                'Cleaver',
                'Consentualist',
                'Farmer',
                'Osiris',
                'Sandman',
                'Scene Queen',
                'Siren']

predatorDesc = ['Attack and mug people for blood',
                'Drink cold bagged blood. Gross and stale.',
                'Drink from other vampires only. Difficult, no blood bond protection.',
                'Feed secretly from a family, perhaps even yours.',
                'Drink consetualy from mortals. This is a masquerade breach btw.',
                'Drink from animals only. Always hungry.',
                'A celebrity or church, drink from people who revere you.',
                'Drink from the sleeping, often by breaking and entering.',
                'Know a subculture well to feed from it, using your status often.',
                'Seduce people, make them think you slept together.']

def predatorPicker(vampire):
    predatorFinalized = True
    while predatorFinalized == True:
        print('Please pick your predator type.')
        print("Type 'help' for a list of types and brief description.")

        choice = input('> ').lower()

        if choice == 'help':
            for i in range(len(predatorList)):
                print(predatorList[i],':', predatorDesc[i])
                print()

        #If the player chooses Alleycat
        if choice == 'alleycat':
            print(predatorList[0],':',predatorDesc[0])
            print('Gain the following:')
            print('Add a specialty, Intimidation(Stickups) or Brawl (Grappling)')
            print('Gain a dot of celerity or potence')
            print('Lose 1 Humanity')
            print('Gain 3 dots of Criminal Contacts')
            print()
            print('Would you like to take this predator type? [y/n]')
            alleyChoice = input('> ').lower()

            if alleyChoice == 'y' or alleyChoice == 'yes':
                print('Predator Type set to Alleycat')
                
                while True:
                    print('Would you like a specialty in [1] intimdate(stickups)')
                    print('or in [2] Brawl(Grappling)?')
                    alleyspec = input('> ').lower()
                    if alleyspec == '1':
                        vampire.specialties['intimidate'] = 'stickups'
                        break
                    if alleyspec == '2':
                        vampire.specialties['brawl'] = 'grappling'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your celerity or potence?')
                    alleydisc = input('> ').lower()
                    if alleydisc == 'celerity':
                        vampire.celerity += 1
                        break
                    if alleydisc == 'potence':
                        vampire.potence += 1
                        break
                    else:
                        print('please input a proper value')
                        
                vampire.humanity -= 1
                vampire.advantages['criminal contacts'] = 3
                        
                predatorFinalized = False

        #if player chooses Bagger
        elif choice == 'bagger':
            print(predatorList[1],':',predatorDesc[1])
            print('Gain the following:')
            print('Add a specialty, larceny(lockpicking) or streetwise (black market)')
            print('Gain a dot of blood sorcery (Tremere only) or Obsfuscate')
            print('Gain the feeding merit: Iron Gullet (3)')
            print('Gain the enemy flaw (2)')
            print()
            print('Would you like to take this predator type? [y/n]')
            bagChoice = input('> ').lower()

            if bagChoice == 'y' or bagChoice == 'yes':
                print('Predator Type set to Bagger')
                
                while True:
                    print('Would you like a specialty in [1] larceny(lockpicking)')
                    print('or in [2] streetwise (black market)?')
                    bagspec = input('> ').lower()
                    if bagspec == '1':
                        vampire.specialties['larceny'] = 'lockpicking'
                        break
                    if bagspec == '2':
                        vampire.specialties['streetwise'] = 'black market'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    #handles subexception where it matters if player if Tremere
                    if vampire.clan == 'tremere':
                        print('Would you like to increase your Blood Sorcery or Obfuscate?')
                        bag_T_disc = input('> ').lower()
                        if bag_T_disc == 'blood sorcery':
                            vampire.bloodSorcery += 1
                            break
                        if bag_T_disc == 'obfuscate':
                            vampire.obfuscate += 1
                            break
                        else:
                            print('please input a proper value')
                            print('bagger')
                    else:
                        print('Obfuscate increased by one.')
                        vampire.obfuscate += 1
                        break
                        
                vampire.advantages['Enemy Flaw'] = -2
                vampire.advantages['Iron Gullet'] = 3
                        
                predatorFinalized = False

        
        elif choice == 'blood leech':
            print(predatorList[2],':',predatorDesc[2])
            print('Gain the following:')
            print('Add a specialty, brawl(kindred) or stealth(kindred).')
            print('Gain a dot of celerity or protean.')
            print('Lose 1 Humanity.')
            print('Increase blood potency by 1.')
            print('Gain dark secret flaw: Diablerist (2) or Shunned (2).')
            print('Gain the feeding flaw (2): Prey exclusion(mortals).')
            print()
            print('Would you like to take this predator type? [y/n]')
            leechChoice = input('> ').lower()

            if leechChoice == 'y' or leechChoice == 'yes':
                print('Predator Type set to Blood Leech')
                
                while True:
                    print('Would you like a specialty in [1] brawl(kindred)')
                    print('or in [2] stealth(kindred)?')
                    leechspec = input('> ').lower()
                    if leechspec == '1':
                        vampire.specialties['brawl'] = 'kindred'
                        break
                    if leechspec == '2':
                        vampire.specialties['stealth'] = 'kindred'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your celerity or protean?')
                    leechdisc = input('> ').lower()
                    if leechdisc == 'celerity':
                        vampire.celerity += 1
                        break
                    if leechdisc == 'protean':
                        vampire.protean += 1
                        break
                    else:
                        print('please input a proper value')

                while True:
                    print('Which flaw would you like to take?')
                    print('[1] Diablerist (2)')
                    print('[2] Shunned (2)')
                    leechFlaw = input('> ').lower()
                    if leechFlaw == '1':
                        vampire.advantages['Diablerist'] = -2
                        break
                    if leechFlaw == '2':
                        vampire.advantages['Shunned'] = - 2
                        break
                        
                vampire.humanity -= 1
                print(f'Humanity decreased to {vampire.humanity}')
                vampire.bp += 1
                vampire.advantages['Prey Exclusion(mortals)'] = -2
                        
                predatorFinalized = False

                
        elif choice == 'cleaver':
            print(predatorList[3],':',predatorDesc[3])
            print('Gain the following:')
            print('Add a specialty, persuasion(gaslighting) or subterfuge(coverups).')
            print('Gain a dot of dominate or animalism.')
            print('Gain dark secret flaw: Clear(1).')
            print('Gain the Herd(2)advantage.')
            print()
            print('Would you like to take this predator type? [y/n]')
            cleaverChoice = input('> ').lower()

            if cleaverChoice == 'y' or cleaverChoice == 'yes':
                print('Predator Type set to Cleaver')
                
                while True:
                    print('Would you like a specialty in [1] persuasion(gaslighting)')
                    print('or in [2] subterfuge(coverups)?')
                    cleaverspec = input('> ').lower()
                    if cleaverspec == '1':
                        vampire.specialties['persuasion'] = 'gaslighting'
                        break
                    if cleaverspec == '2':
                        vampire.specialties['subterfuge'] = 'coverups'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your dominate or animalism?')
                    cleaverdisc = input('> ').lower()
                    if cleaverdisc == 'dominate':
                        vampire.dominate += 1
                        break
                    if cleaverdisc == 'animalism':
                        vampire.animalism += 1
                        break
                    else:
                        print('please input a proper value')

                
                vampire.advantages['Cleaver'] = -1
                vampire.advantages['Herd'] = 2
                        
                predatorFinalized = False

        #Concentualist
        elif choice == 'consentualist':
            print(predatorList[4],':',predatorDesc[4])
            print('Gain the following:')
            print('Add a specialty, medicine(phlebotomy) or Persuasion(Victims).')
            print('Gain a dot of Auspex or Forititude.')
            print('Gain a dot of humanity')
            print('Gain the Dark Secret: Masquerade Breacher')
            print('Gain feeding flaw: Prey Exclusion (non-consenting).')
            print()
            print('Would you like to take this predator type? [y/n]')
            farmChoice = input('> ').lower()

            if farmChoice == 'y' or farmChoice == 'yes':
                print('Predator Type set to consentualist.')
                
                while True:
                    print('Would you like a specialty in [1] medicine(phlebotomy)')
                    print('or in [2] Persuasion(Victims)?')
                    farmspec = input('> ').lower()
                    if farmspec == '1':
                        vampire.specialties['medicine'] = 'phlebotomy'
                        break
                    if farmspec == '2':
                        vampire.specialties['persuasion'] = 'victims'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your auspex or fortitude?')
                    farmdisc = input('> ').lower()
                    if farmdisc == 'auspex':
                        vampire.auspex += 1
                        break
                    if farmdisc == 'fortitude':
                        vampire.fortitude += 1
                        break
                    else:
                        print('please input a proper value')

                
                vampire.advantages['Dark Secret: Masqurade Breacher'] = 1
                vampire.advantages['Feeding Flaw: Prey Exclusion(non-consenting)'] = 1
                vampire.humanity += 1
                print(f'Humanity increased to {vampire.humanity}')
                        
                predatorFinalized = False

    
        #Farmer Predator Type
        elif choice == 'farmer':
            print(predatorList[5],':',predatorDesc[5])
            print('Gain the following:')
            print('Add a specialty, Animal Ken ([Specific Animal]) or Survival(hunting).')
            print('Gain a dot of Animalism or Protean.')
            print('Gain a dot of humanity')
            print('Gain feeding flaw: farmer (2).')
            print()
            print('Would you like to take this predator type? [y/n]')
            farmChoice = input('> ').lower()

            if farmChoice == 'y' or farmChoice == 'yes':
                print('Predator Type set to Farmer.')
                
                while True:
                    print('Would you like a specialty in [1] Animal Ken ([Specific Animal])')
                    print('or in [2] Survival(hunting)?')
                    farmspec = input('> ').lower()
                    if farmspec == '1':
                        print('Please choose what animal to specifically specialize in.')
                        animal_choice = input('> ').lower()
                        vampire.specialties['medicine'] = animal_choice
                        break
                    if farmspec == '2':
                        vampire.specialties['survival'] = 'hunting'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your animalism or protean?')
                    farmdisc = input('> ').lower()
                    if farmdisc == 'animalism':
                        vampire.animalism += 1
                        break
                    if farmdisc == 'protean':
                        vampire.protean += 1
                        break
                    else:
                        print('please input a proper value')

                
                vampire.advantages['feeding flaw: farmer'] = -2
                vampire.humanity += 1
                print(f'Humanity increased to {vampire.humanity}')
                        
                predatorFinalized = False

        
        #Osiris Predator Type
        elif choice == 'osiris':
            print(predatorList[6],':',predatorDesc[6])
            print('Gain the following:')
            print('Add a specialty, Occult([specific tradition]) or Persuasion([Specific entertainment field]).')
            print('Gain a dot of Presence or Blood Sorcery (Tremere only).')
            print('Spend three dots between fame and herd.')
            print('Spend two dots between Enemies and Mythic Flaws.')
            print()
            print('Would you like to take this predator type? [y/n]')
            osiChoice = input('> ').lower()

            if osiChoice == 'y' or osiChoice == 'yes':
                print('Predator Type set to Osiris.')
                
                while True:
                    print('Would you like a specialty in [1] Occult([specific tradition])')
                    print('or in [2] Persuasion([Specific entertainment field])?')
                    osispec = input('> ').lower()
                    if osispec == '1':
                        print('Please choose a specific tradition to specialize in.')
                        tradition_choice = input('> ').lower()
                        vampire.specialties['occult'] = tradition
                        break
                    if osispec == '2':
                        print('Please choose a specific entertainment field to specialize in.')
                        entertainment_choice = input('> ').lower()
                        vampire.specialties['persuasion'] = entertainment_choice
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    #handles subexception where it matters if player if Tremere
                    if vampire.clan == 'tremere':
                        print('Would you like to increase your blood sorcery or presence?')
                        osi_T_disc = input('> ').lower()
                        if osi_T_disc == 'blood sorcery':
                            vampire.bloodSorcery += 1
                            break
                        if osi_T_disc == 'presence':
                            vampire.presence += 1
                            break
                        else:
                            print('please input a proper value')
                    else:
                        print('Presence increased by one.')
                        vampire.presence += 1
                        break

                while True:
                    print('How many dots would you like to assign to fame?')
                    print('(0-3 dots)')
                    print('The remaining dots will be assigned to herd.')
                    fameHerdPoints = input('> ').lower()
                    try:
                        val = int(fameHerdPoints)
                        if (val > -1 and val < 4):
                            vampire.advantages['fame'] = val
                            vampire.advantages['herd'] = 3 - val
                            break
                        else:
                            print('please input a value between 0 and 3')
                    except ValueError:
                        print('please input a proper value')

                while True:
                    print('How many dots would you like to assign to Enemies?')
                    print('(0-3 dots)')
                    print('The remaining dots will be assigned to mythic flaws')
                    enemiesMythic = input('> ').lower()
                    try:
                        val = int(enemiesMythic)
                        if (val > -1 and val < 4):
                            vampire.advantages['Enemies'] = val
                            print('TO DO: Mythic Flaw Handler')
                        else:
                            print('please input a value between 0 and 3')
                    except ValueError:
                        print('please input a proper value')
                        
                predatorFinalized = False

        #Sandman predator type
        elif choice == 'sandman':
            print(predatorList[7],':',predatorDesc[7])
            print('Gain the following:')
            print('Add a specialty, medicine(anesthetics) or stealth(break-in).')
            print('Gain a dot of auspex or obfuscate.')
            print('Gain one dot of resources')
            print()
            print('Would you like to take this predator type? [y/n]')
            sandChoice = input('> ').lower()

            if sandChoice == 'y' or sandChoice == 'yes':
                print('Predator Type set to Sandman')
                
                while True:
                    print('Would you like a specialty in [1] medicine(anesthetics)')
                    print('or in [2] stealth(break-in)?')
                    sandspec = input('> ').lower()
                    if sandspec == '1':
                        vampire.specialties['medicine'] = 'anesthetics'
                        break
                    if sandspec == '2':
                        vampire.specialties['stealth'] = 'break-ins'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your auspex or obfuscate?')
                    sanddisc = input('> ').lower()
                    if sanddisc == 'auspex':
                        vampire.auspex += 1
                        break
                    if sanddisc == 'obfuscate':
                        vampire.obfuscate += 1
                        break
                    else:
                        print('please input a proper value')

                
                vampire.advantages['resources'] = 1
                        
                predatorFinalized = False

        #Scene Queen Predator Type
        elif choice == 'scene queen':
            print(predatorList[8],':',predatorDesc[8])
            print('Gain the following:')
            print('Add a specialty, etiquette(specific scene), leadership(specific scene),')
            print('or streetwise(specific scene).')
            print('Gain a dot of dominate or potence.')
            print('Gain one dot of the fame advantage.')
            print('Gain one dot of the contacts advantage.')
            print('Gain one of the following flaws:')
            print('- Disliked (outside your subculture)')
            print('- Prey Exclusion (a different subculture than yours)')
            print()
            print('Would you like to take this predator type? [y/n]')
            sceneChoice = input('> ').lower()

            if sceneChoice == 'y' or sandChoice == 'yes':
                print('Predator Type set to Scene Queen')

                print('Please select your subculture')
                subculture = input('> ').lower()
                
                while True:
                    print(f'Would you like a specialty in [1] etiquette({subculture}),')
                    print(f'[2] leadership({subculture}) or [3] steetwise({subculture})?')
                    scenespec = input('> ').lower()
                    if scenespec == '1':
                        vampire.specialties['etiquette'] = subculture
                        break
                    if scenespec == '2':
                        vampire.specialties['leadership'] = subculture
                        break
                    if scenespec == '3':
                        vampire.specialties['streetwise'] = subculture
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your dominate or potence?')
                    scenedisc = input('> ').lower()
                    if scenedisc == 'dominate':
                        vampire.dominate += 1
                        break
                    if scenedisc == 'potence':
                        vampire.potence += 1
                        break
                    else:
                        print('please input a proper value')

                while True:
                    print('Would you like [1] Disliked (outside your subculture),')
                    print('Or [2] Prey Exclusion (a different subculture than yours)')
                    flawChoice = input('> ').lower()
                    if flawChoice == '1':
                        vampire.advantages['disliked'] = 1
                        break
                    if flawChoice == '2':
                        print('Please select another subculture to be your prey exclusion')
                        exclusion_group = input('> ').lower()
                        vampire.advantages[f'Prey Exclusion: {exclusion_group}'] = 1
                        break
                            
                vampire.advantages['fame'] = 1
                vampire.advantages['contacts'] = 1
                        
                predatorFinalized = False

        #Siren Predator Type
        elif choice == 'siren':
            print(predatorList[9],':',predatorDesc[9])
            print('Gain the following:')
            print('Add a specialty, persuasion(seduction) or subterfuge(seduction).')
            print('Gain a dot of fortitude or presence.')
            print('Gain the looks merit: Beautiful')
            print('Gain the enemy flaw: a spurned lover or jealous partner')
            print()
            print('Would you like to take this predator type? [y/n]')
            sirenChoice = input('> ').lower()

            if sirenChoice == 'y' or sandChoice == 'yes':
                print('Predator Type set to Siren')
                
                while True:
                    print('Would you like a specialty in [1] persuasion(seduction)')
                    print('or in [2] subterfuge(seduction)?')
                    sirenspec = input('> ').lower()
                    if sirenspec == '1':
                        vampire.specialties['persuasion'] = 'seduction'
                        break
                    if sirenspec == '2':
                        vampire.specialties['subterfuge'] = 'seduction'
                        break
                    else:
                        print('please input a proper value')
                        
                while True:
                    print('Would you like to increase your fortitude or presence?')
                    sirendisc = input('> ').lower()
                    if sirendisc == 'fortitude':
                        vampire.fortitude += 1
                        break
                    if sirendisc == 'presence':
                        vampire.presence += 1
                        break
                    else:
                        print('please input a proper value')

                vampire.advantages['Looks: Beautiful'] = 1
                vampire.advantages['Enemy'] = 1
                        
                predatorFinalized = False

        else:
            print('Please give a valid input')
            print()


