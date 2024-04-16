import random
from time import sleep
import AsciiImgs

#basic stats
capybaramax = {'MAX_HP' : 30, 'MAX_ATK' : 3, 'DEF' : 0}
capybara = {'HP' : 30, 'ATK' : 3}
    
playermax = {'MAX_HP' : 30, 'MAX_ATK' : 3, 'DEF' : 0}
player = {'HP' : 30, 'ATK' : 3}

def SelTitle():
    adjectiveList = ('Fat', 'Unyielding', 'Smiling', 'Classy', 'Discreet', 'Amused', 'Stern', 'Exalted', 'Air Head', 
                      'Billowy', 'Fluffy', 'Willful', 'Jealous', 'Cautious', 'Nasty', 'Mean', 'Hairless', 'Baby', 
                      'Poor', 'Bright', 'Shaman', 'Electric', 'Worthless', 'Clueless', 
                      'Rat', 'Saint', 'Thin', 'Old', 'Strong', 'Envious', 'Animated', 'Decomposing', 
                      'Quirky', 'Nutritious', 'Shallow', 'Obscene', 'Ablaze', 'Valuable', 'Elated')
    lottery = random.randint(0, 39)
    
    subject =  f'{adjectiveList[lottery]} Capybara'
    
    return subject

def BattleScreen(capybara : dict, capybaramax : dict, player : dict, playermax : dict, capybaratitle : str):
    
    GUI = f"""
-------------------------------------------------------------------
                        {capybaratitle}
    {capybara['HP']}/{capybaramax['MAX_HP']} Health             {capybara['ATK']}/{capybaramax['MAX_ATK']} Attack                {capybaramax['DEF']} Defense
-------------------------------------------------------------------
{AsciiImgs.capybaraImg}
-------------------------------------------------------------------
                            Player
    {player['HP']}/{playermax['MAX_HP']} Health               {player['ATK']}/{playermax['MAX_ATK']} Attack                  {playermax['DEF']} Defense
-------------------------------------------------------------------"""
    return AsciiImgs.printUTF8(GUI)

def Flee():
    
    roll = random.randint(1, 10)
    
    if roll == 10:
        return True
    else:
        return False
    
def Restart(Gameover : bool):
    Restart : str = ''
    if Gameover:
        while Restart != 'YES' or Restart != 'NO':
            Restart = input('\nYou lost, do you wanna play again Yes|No\n')
            Restart = Restart.upper()
            if Restart == 'YES':
                print('\nLets begin anew them\n')
                #placeholder for stat reset
                capybara['HP'], capybaramax['MAX_ATK'] = capybaramax['MAX_HP'], capybaramax['MAX_ATK']
                player['HP'], player['ATK'] = playermax['MAX_HP'], playermax['MAX_ATK']
                sleep(1)
                break
            elif Restart == 'NO':
                print('\nThank you for playing. Goodbye!\n')
                GameOn = False
                sleep(1)
                break
            else:
                print(f"\n{Restart} is not a valid option, try again\n")
    else:
        while Restart != 'YES' or Restart != 'NO':
            Restart = input('\nDo you wish to end your run now? Yes|No\n')
            Restart = Restart.upper()
            if Restart == 'NO':
                print('\nTo the next battle then!\n')
                #placeholder for level up
                capybara['HP'], capybaramax['MAX_ATK'] = capybaramax['MAX_HP'], capybaramax['MAX_ATK']
                player['HP'], player['ATK'] = playermax['MAX_HP'], playermax['MAX_ATK']
                sleep(1)
                break
            elif Restart == 'YES':
                print('\nThank you for playing. Goodbye!\n')
                GameOn = False
                sleep(1)
                break
            else:
                print(f"\n{Restart} is not a valid option, try again\n")
# main Function
def StartBattle(BattleOn : bool):
    capybaratitle = SelTitle()
    capybaraDefending = False
    playerDefending = False
# main loop
    while BattleOn:
# print screen
        sleep(0.5)
        BattleScreen(capybara, capybaramax, player, playermax, capybaratitle)
# selection process
        while True:
            Choice = input("\nA foe has appeared, what do you do\n> 1: Attack (a simple attack)\n> 2: Defend (diminish damage equal to your Defense attribute)\n> 3: Flee (1/10 change o skipping this fight, but you dont level up)\n")
            
            Choice = Choice.upper()
            
            if Choice in ("1", "ATTACK", "2", "DEFEND", "3", "FLEE"):
                break
            elif Choice in ("CLOSE","BREAK", "EXIT"):
                print("\nGoodbye.\n")
                GameOn = False
                break
            else:
                print(f"\n[{Choice}] is not a valid option choose a valid option\n")
# player logic
        match Choice:
            case "1" | "ATTACK":
                if capybaraDefending == True:
                    capybara['HP'] -= (player['ATK'] - capybaramax['DEF'])
                else:
                    capybara['HP'] -= player['ATK']
                playerDefending = False
            case "2" | "DEFEND":
                playerDefending = True
            case "3" | "FLEE":
                roll = Flee()
                if roll == True:
                    break
                else:
                    continue
# enemy logic
        enemyai = random.randint(0, 100)
        if capybara['HP'] <= 0:
            print('\nCongratulations you won!\n')
            Restart(False)
        elif enemyai < 70:
            if playerDefending == True:
                player['HP'] -= (capybara['ATK'] - playermax['DEF'])
            else:
                player['HP'] -= capybara['ATK']
            capybaraDefending = False
        else:
            capybaraDefending = True
#death logic
        if player['HP'] < 0:
            Restart(True)
            
StartBattle(True)