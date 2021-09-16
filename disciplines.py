#does disciplines and predator types

from Character import character

def disciplinesChoice(vampire):

    disciplines_list = ['animalism', 'auspex', 'celerity',
                   'dominate', 'fortitude', 'obfuscate',
                   'oblivion', 'potence', 'presence',
                   'protean', 'blood sorcery']
    
    #TODO : THINBLOODS AND CAITIFFS
    choiceturn = 2
    while choiceturn > 0:
        print('Pick two disciplines to improve, one to 2 dots, one to 1 dot.')
        print('Your clan disciplines are:')
        for i in vampire.clanDisciplines:
            print(i.capitalize())
        if choiceturn == 2:
            print('Please choose a discipline to set to 2 dots.')
        if choiceturn == 1:
            print('Please choose a discipline to set to 1 dot.')

            
        discChoice = str(input('> ')).lower()
        if discChoice in disciplines_list:
            checker = increaseDiscipline(discChoice, choiceturn, vampire, True)
            if checker == True:
                choiceturn -= 1
            

def increaseDiscipline(disc_choice: str, val: int, vampire, chargen=False):
    #works the same way as improveAttributes()
    if disc_choice == 'animalism' and ((chargen != (vampire.animalism == 0))
                                           or (chargen and (vampire.animalism == 0)
                                               or ((not chargen) and (vampire.animalism == 0)))):
        vampire.animalism += val
        return True

    if disc_choice == 'auspex' and ((chargen != (vampire.auspex == 0))
                                           or (chargen and (vampire.auspex == 0)
                                               or ((not chargen) and (vampire.auspex == 0)))):
        vampire.auspex += val
        return True

    if disc_choice == 'auspex' and ((chargen != (vampire.auspex == 0))
                                           or (chargen and (vampire.auspex == 0)
                                               or ((not chargen) and (vampire.auspex == 0)))):
        vampire.auspex += val
        return True

    if disc_choice == 'celerity' and ((chargen != (vampire.celerity == 0))
                                           or (chargen and (vampire.celerity == 0)
                                               or ((not chargen) and (vampire.celerity == 0)))):
        vampire.celerity += val
        return True

    if disc_choice == 'dominate' and ((chargen != (vampire.dominate == 0))
                                           or (chargen and (vampire.dominate == 0)
                                               or ((not chargen) and (vampire.dominate == 0)))):
        vampire.dominate += val
        return True

    if disc_choice == 'fortitude' and ((chargen != (vampire.fortitude == 0))
                                           or (chargen and (vampire.fortitude == 0)
                                               or ((not chargen) and (vampire.fortitude == 0)))):
        vampire.fortitude += val
        return True

    if disc_choice == 'obfuscate' and ((chargen != (vampire.obfuscate == 0))
                                           or (chargen and (vampire.obfuscate == 0)
                                               or ((not chargen) and (vampire.obfuscate == 0)))):
        vampire.obfuscate += val
        return True

    if disc_choice == 'oblivion' and ((chargen != (vampire.oblivion == 0))
                                           or (chargen and (vampire.oblivion == 0)
                                               or ((not chargen) and (vampire.oblivion == 0)))):
        vampire.oblivion += val
        return True

    if disc_choice == 'potence' and ((chargen != (vampire.potence == 0))
                                           or (chargen and (vampire.potence == 0)
                                               or ((not chargen) and (vampire.potence == 0)))):
        vampire.potence += val
        return True

    if disc_choice == 'presence' and ((chargen != (vampire.presence == 0))
                                           or (chargen and (vampire.presence == 0)
                                               or ((not chargen) and (vampire.presence == 0)))):
        vampire.presence += val
        return True

    if disc_choice == 'protean' and ((chargen != (vampire.protean == 0))
                                           or (chargen and (vampire.protean == 0)
                                               or ((not chargen) and (vampire.protean == 0)))):
        vampire.protean += val
        return True

    if disc_choice == 'blood sorcery' and ((chargen != (vampire.bloodSorcery == 0))
                                           or (chargen and (vampire.bloodSorcery == 0)
                                               or ((not chargen) and (vampire.bloodSorcery == 0)))):
        vampire.bloodSorcery += val
        return True
