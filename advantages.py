#Merits, Flaws & Backgrounds

class advt:
    def __init__(self, ratingMax: int = 5, flaws={}, merits = {}, reverse: bool = False):
        self.ratingMax = ratingMax
        self.flaws = flaws
        self.merits = merits
    
class backgrounds(advt):
    def __init__(self, ratingMax: int = 5, flaws={}, merits = {}, reverse: bool = False):
        super().__init__(self, ratingMax, flaws, merits)

linguistics = advt(5,{'Illiterate': 2})

looks = advt(0, flaws = {'Repulsive': 2, 'Ugly': 1},
                   merits = {'Beautiful': 2, 'Stunning': 4})

substanceUse = advt(0, {'Hopeless Addiction':2, 'Addiction': 1},
                {'High-Funcitoning Addict': 1})

archaic = advt(0, {'Archaic' : 2, 'Living in the Past': 1})

bonding = advt(0, {'Bondslave': 2, 'Bond Junkie': 1, 'Long bond': 1},
           {'Bond Resistance': 1, 'Short Bond': 2, 'Unbondable':5})

feeding = advt(0, {'Vegan': 2, 'Organavore': 2, "Methuselah's Thirst": 1,
                       'Prey Exclusion': 1},
           {'Bloodhound' : 1, 'Iron Gullet': 3})

mythic = advt(0, {'Stake Bait': 2, 'Folkloric Bane': 1, 'Folkloric Block': 1,
              'Stigmata': 2}, {'Eat Food': 2})

thinblood = advt(0, {'Baby Teeth': 1, 'Bestial Temper': 1, 'Branded by the Camarilla':1,
                 'Clan Curse': 1, 'Dead Flesh': 1, 'Mortal Frailty': 1,
                 'Shunned by the Anarchs': 1, 'Vitae Dependency': 1},
             {'Anarch Comrades': 1, 'Camarilla Contact': 1, 'Catenating Blood': 1,
              'Day Drinker': 1, 'Discipline Affinity': 1, 'Lifelike': 1,
              'Thinblood Alchemist': 1, 'Vampiric Resilience': 1})


#Backgrounds

allies = backgrounds(5, {'Gifted Mortal Foe': 1, 'Deadly Mortal Foe': 2})

contacts = backgrounds(3)

fame = backgrounds(5, {'Bloodhunted':3, 'Minor hunted':1}, {}, True)

influence = backgrounds(5, {'Despised': 2, 'Disliked':1})

haven = backgrounds(3,
                    {'No Haven':1, 'Compromised Haven': 2, 'Creepy Haven': 1, 'Haunted Haven': 1},
                    {'Hidden Armory':1, 'Cell':1, 'Watchmen':1, 'Laboratory':1, 'Library':1,
                     'Location':1, 'Luxury':1, 'Postern':1, 'Security System':1, 'Surgery':1, 'Warding': 1})

herd = backgrounds(5)

loresheets = backgrounds(0)
#TO DO

mask = backgrounds(2, {'Known Blankbody': 2, 'Known corpse': 2}, {'Zeroed': 1, 'Cobbler': 1})

mawla = backgrounds(5, {}, {}, True)

resources = backgrounds(5, {'Destitute': 1})

retainers = backgrounds(3, {'Stalkers': 1})

status = backgrounds(5, {'Shunned': 2, 'Suspect': 1})
   
#Allies
    #Split points between Effectiveness (1-4) & Reliability (1-3)
    #Enemies are the same but a flaw (-2 cheaper effectiveness
#Contacts
    #0-3 dots
#Fame
    #0-5 dots
    #Flaw version of fame
    #Flaw: Dark secret
        #Blood hunted/hunted 3 flaw
        #minor annoyance 1 flaw
#Influence
    #0-5 dots
    #Flaw: Despised 2
    #Flaw: Disliked 1
#Haven
    #1-3 dots
    #Flaw: No Haven (1)
    #Haven Merits and Flaws:
    #Flaw: Compromised haven 2
    #Flaw: Creepy haven   1 
    #Flaw: Haunted haven  1
    #MERITS:
        #Hidden Armory, Cell, watchmen, Laboratory
        #Library, Location, Luxury, Postern
        #Security system, surgery, warding
#Herd
    #Rating 1 - 5
#Lore sheets
    #A mess
#Mask
    #Rating 0-2
    #Flaw Known blankbody (2)
    #Flaw Known corpse (2)
    #Merits if R=2
        #Merit: Zeroed (1)
        #Merit: Cobbler (1)
#Mawla
    #0-5 rating
    #Can be taken as flaw Adversary
#Resources
    #0-5 rating
    #Flaw: Destitue (1)
#Retainers
    #0-3
    #Flaw: Stalkers (1)
#Status
    #0-5 rating
    #Flaw: Shunned (2)
    #Flaw: Suspect (1)
    
    
