#Defines the v5 character

class character():
    def __init__(self):
        self.clan = ''

        self.strength = 0
        self.dexterity = 0
        self.stamina = 0
        self.charisma = 0
        self.manipulation = 0
        self.composure = 0
        self.intelligence = 0
        self.wits = 0
        self.resolve = 0
        
        self.athletics = 0
        self.brawl = 0
        self.craft = 0
        self.drive = 0
        self.firearms = 0
        self.larceny = 0
        self.melee = 0
        self.stealth = 0
        self.survival = 0

        self.animalKen = 0
        self.etiquette = 0
        self.insight = 0
        self.intimidation = 0
        self.leadership = 0
        self.performance = 0
        self.persuasion = 0
        self.streetwise = 0
        self.subterfuge = 0

        self.academics = 0
        self.awareness = 0
        self.awareness = 0
        self.finance = 0
        self.investigation = 0
        self.medicine = 0
        self.occult = 0
        self.politics = 0
        self.science = 0
        self.technology = 0

        self.specialties = {}

        self.wp = 0
        self.health = 0
        self.humanity = 0
        self.generation = 0
        self.bp = 0

        self.clanDisciplines = []
        self.animalism = 0
        self.auspex = 0
        self.celerity = 0
        self.dominate = 0
        self.fortitude = 0
        self.obfuscate = 0
        self.oblivion = 0
        self.potence = 0
        self.presence = 0
        self.protean = 0
        self.bloodSorcery = 0
        self.TBalchemy = 0

        self.advantages = {}
        self.convictions = []
        self.touchstones = []

    def calculations(self):
        self.health = 3 + self.stamina
        self.wp = self.composure + self.resolve

    def resetAttributes(self):
        self.strength = 0
        self.dexterity = 0
        self.stamina = 0
        self.charisma = 0
        self.manipulation = 0
        self.composure = 0
        self.intelligence = 0
        self.wits = 0
        self.resolve = 0

    def resetSkills(self):
        self.athletics = 0
        self.brawl = 0
        self.craft = 0
        self.drive = 0
        self.firearms = 0
        self.larceny = 0
        self.melee = 0
        self.stealth = 0
        self.survival = 0

        self.animalKen = 0
        self.etiquette = 0
        self.insight = 0
        self.intimidation = 0
        self. leadership = 0
        self.performance = 0
        self.persusasion = 0
        self.streetwise = 0
        self.subterfuge = 0

        self.academics = 0
        self.awareness = 0
        self.awareness = 0
        self.finance = 0
        self.investigation = 0
        self.medicine = 0
        self.occult = 0
        self.politics = 0
        self.science = 0
        self.technology = 0

    def setDisciplines(self, clan):
        if clan == 'banu haqim':
            self.clanDisciplines = ['celerity', 'presence', 'blood sorcery']
        if clan == 'brujah':
            self.clanDisciplines = ['celerity', 'presence', 'potence']
        if clan == 'gangrel':
            self.clanDisciplines = ['animalism', 'fortitude', 'protean']
        if clan == 'hecata':
            self.clanDisciplines = ['auspex', 'fortitude', 'oblivion']
        if clan == 'lasombra':
            self.clanDisciplines = ['dominate', 'oblivion', 'potence']
        if clan == 'malkavian':
            self.clanDisciplines = ['auspex', 'dominate', 'obfuscate']
        if clan == 'ministry':
            self.clanDisciplines = ['obfuscate', 'presence', 'protean']
        if clan == 'nosferatu':
            self.clanDisciplines = ['animalism', 'obfuscate', 'potence']
        if clan == 'ravnos':
            self.clanDisciplines = ['animalism', 'obfuscate', 'presence']
        if clan == 'toreador':
            self.clanDisciplines = ['auspex', 'celerity', 'presence']
        if clan == 'tremere':
            self.clanDisciplines = ['auspex', 'dominate', 'blood sorcery']
        if clan == 'tzimisce':
            self.clanDisciplines = ['animalism', 'dominate', 'protean']
        if clan == 'ventrue':
            self.clanDisciplines = ['dominate', 'fortitude', 'presence']
        if clan == 'thinblood':
            self.clanDisciplines = ['TBalchemy']
        
            
        
        
