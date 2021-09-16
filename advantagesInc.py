import advantages
import Character
import advantages

def pickAdv(vampire):
    #TO DO: Add loresheets
    adv_list = ['linguistics', 'looks', 'substance use', 'archaic', 'bonding', 'feeding',
                'mythic', 'thinblood', 'allies', 'contacts', 'fame', 'influence', 'haven',
                'mask', 'mawla', 'resources', 'retainers', 'status']
    
    print('Pick 7 points of advantages and 2 points of flaws')
    adv_pts, flw_pts = 7, 2
    while (adv_pts > 0) and (flw_pts > 0):
        print(f'You have {adv_pts} points for advantages and {flw_pts} points for flaws left.')
        print("Input 'advantages' to see all possible categories")
        adv_choice = str(input('> ')).lower()

        if adv_choice == 'advantages':
            for i in adv_list:
                print(i,',',end='')
            print()

        elif adv_choice in adv_list:
                advFetcher(adv_choice, adv_pts, flw_pts,vampire)
            
def advFetcher(advChoice,
               adv_points: int,
               flw_points: int,
               vampire):
    
    if advChoice == 'linguistics':
        print(f'You may purchase up to {advantages.linguistics.maxRating} points in Linguistics.')
        print(f'Linguistics has the following flaws:')
        print(f'Illiterate: 2 points')
        print(f'')

def advIncrease(advantage_choice: 'str', adv, val: int, vampire):
    while True:
        print('How many points would you like to put in?')
        ptschoice = input('> ')
        try:
            ptschoice = int(ptschoice)
        except ValueError:
            print('Please input a number')
        if ptschoice <= adv_pts and (ptschoice <= advantages_list.adv.ratingMax):
            adv_pts -= ptschoice
            vampire.advantages.append[advantage_choice] = adv_choice
        else:
            print('Please input a proper value')

####


