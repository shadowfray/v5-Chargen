#Prints the character sheet

def printcharsheet(vampire):
    #TO DO: FINISH SHEET
    print(f'STR: {vampire.strength}  CHA: {vampire.charisma}  INT: {vampire.intelligence}')
    print(f'DEX: {vampire.dexterity}  MAN: {vampire.manipulation}  WIT: {vampire.wits}')
    print(f'STA: {vampire.stamina}  CMP: {vampire.composure}  RES: {vampire.resolve}')
    print()
    print(f'Athletics: {vampire.athletics}  \t Animal Ken: {vampire.animalKen}  \t Academics: {vampire.academics}')
    print(f'Brawl: {vampire.brawl}  \t Etiquette: {vampire.etiquette}     \t Awareness: {vampire.awareness}')
    print(f'Craft: {vampire.craft}  \t Insight: {vampire.insight}         \t Finance: {vampire.finance}')
    print(f'Drive: {vampire.drive}  \t Intimidation: {vampire.intimidation} \t Investigation: {vampire.investigation}')
    print(f'Firearms: {vampire.firearms} \t Leadership: {vampire.leadership}      \t Medicine: {vampire.medicine}')
    print(f'Larceny: {vampire.larceny} \t Performance: {vampire.performance}  \t Occult: {vampire.occult}')
    print(f'Melee: {vampire.melee}  \t Persuasion: {vampire.persuasion}  \t Politics: {vampire.politics}')
    print(f'Stealth: {vampire.stealth}  \t Streetwise: {vampire.streetwise}  \t Science: {vampire.science}')
    print(f'Survival: {vampire.survival}  \t Subterfuge: {vampire.subterfuge}  \t Technology: {vampire.technology}')
    print()
    
    #prints specialties
    print('Specialties:')
    spec_keys = vampire.specialties.keys()
    for k in spec_keys:
        print(f'{k}: {vampire.specialties[k]}')
    
    print()
    print(f'Health: {vampire.health} \t Willpower: {vampire.wp}')
    print(f'Humanity: {vampire.humanity}')
    print(f'Generation: {vampire.generation} \t Blood Potency: {vampire.bp}')
    
    #prints convictions and touchstones if they have any
    if len(vampire.convictions) > 0:
        print('Convictions and Touchstones:')
        for i in range(len(vampire.convictions)):
            print(f'{i+1}. {vampire.convictions[i]}: {vampire.touchstones[i]}')

    #disciplines
    discipline_namelist = ['animalism', 'auspex', 'celerity', 'dominate', 'fortitude', 'obfuscate', 'oblivion',
                       'potence', 'presence', 'protean', 'bloodSorcery', 'TBalchemy']
    disciplines = [vampire.animalism, vampire.auspex, vampire.celerity, vampire.dominate, vampire.fortitude, vampire.obfuscate,
                   vampire.oblivion, vampire.potence, vampire.presence, vampire.protean, vampire.bloodSorcery, vampire.TBalchemy]
    
    for i in range(len(discipline_namelist)):
        if disciplines[i] > 0:
            print(f'{discipline_namelist[i]}: {disciplines[i]}')

    #TODO: advantages

    print()
    
