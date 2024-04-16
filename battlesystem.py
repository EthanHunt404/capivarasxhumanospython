import random
from time import sleep
import AsciiImgs

#basic stats
capybaramax = {'MAX_HP' : 30, 'MAX_ATK' : 3, 'MAX_DEF' : 0}
capybara = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
    
playermax = {'MAX_HP' : 30, 'MAX_ATK' : 3, 'MAX_DEF' : 0}
player = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}

global BattleOn
BattleOn : bool = False

def SelTitle():
    adjectiveList = ('Fat', 'Unyielding', 'Smiling', 'Classy', 'Discreet', 'Amused', 'Stern', 'Exalted', 'Air Head', 
                      'Billowy', 'Fluffy', 'Willful', 'Jealous', 'Cautious', 'Nasty', 'Mean', 'Hairless', 'Baby', 
                      'Poor', 'Bright', 'Shaman', 'Electric', 'Worthless', 'Clueless', 
                      'Rat', 'Saint', 'Thin', 'Old', 'Strong', 'Envious', 'Animated', 'Decomposing', 
                      'Quirky', 'Nutritious', 'Shallow', 'Obscene', 'Ablaze', 'Valuable', 'Elated')
    lottery = random.randint(0, 38)

    subject =  f'{adjectiveList[lottery]} Capybara'
    return subject

def BattleScreen(capybara : dict, capybaramax : dict, player : dict, playermax : dict, capybaratitle : str):
    
    gui = f"""
-------------------------------------------------------------------
                        {capybaratitle}
    {capybara['HP']}/{capybaramax['MAX_HP']} Health             {capybara['ATK']} Attack                {capybara['DEF']} Defense
-------------------------------------------------------------------
{AsciiImgs.capybaraImg}
-------------------------------------------------------------------
                            Player
    {player['HP']}/{playermax['MAX_HP']} Health               {player['ATK']} Attack                  {player['DEF']} Defense
-------------------------------------------------------------------"""
    return AsciiImgs.printUTF8(gui)

def Flee():
    roll = random.randint(1, 10)
    if roll == 10:
        return True
    else:
        return False

# main Function
def StartBattle():
    capybaratitle = SelTitle()
    capybaraDefending = False
    playerDefending = False
    global BattleOn
# main loop of the main function
    while BattleOn:
# print screen
        BattleScreen(capybara, capybaramax, player, playermax, capybaratitle)
# selection process
        while True:
            Choice = input("\nA foe is in front of you, what do you do\n> 1: Attack (a simple attack)\n> 2: Defend (diminish damage equal to your Defense attribute)\n> 3: Flee (1/10 change o skipping this fight, but you dont level up)\n")
            Choice = Choice.upper()
            if Choice in ("1", "ATTACK", "2", "DEFEND", "3", "FLEE"):
                break
            elif Choice in ("CLOSE","BREAK", "EXIT"):
                print("\nGoodbye.")
                BattleOn = False
                break
            else:
                print(f"\n[{Choice}] is not a valid option choose a valid option")
# player logic
        match Choice:
            case "1" | "ATTACK":
                if capybaraDefending == True:
                    capybara['HP'] -= (player['ATK'] - capybara['DEF'])
                else:
                    capybara['HP'] -= player['ATK']
                playerDefending = False
            case "2" | "DEFEND":
                playerDefending = True
            case "3" | "FLEE":
                roll = Flee()
                if roll == True:
                    LevelUp(capybaramax, True)
                    capybara['HP'], capybara['ATK'], capybara['DEF'] = capybaramax['MAX_HP'], capybaramax['MAX_ATK'], capybaramax['MAX_DEF']
                    player['HP'], player['ATK'], player['DEF'] = playermax['MAX_HP'], playermax['MAX_ATK'], playermax['MAX_DEF']
                    print("\nYou were able to flee")
                    sleep(1)
                    break
                else:
                    print("\nYou weren't able to flee. The battle continues!")
                    sleep(1)
                    continue
# enemy logic
        enemyai = random.randint(0, 100)
        if capybara['HP'] <= 0:
            print('\nCongratulations you won!')
            Restart(False)
        elif enemyai < 70:
            if playerDefending == True:
                player['HP'] -= (capybara['ATK'] - player['DEF'])
            else:
                player['HP'] -= capybara['ATK']
            capybaraDefending = False
        else:
            capybaraDefending = True
# death logic
        if player['HP'] < 0:
            Restart(True)
# restart logic   
def Restart(GameOver : bool):
    global BattleOn
    Restart : str = ''
    if GameOver:
        while Restart != 'YES' or Restart != 'NO':
            Restart = input('\nYou lost, do you wanna play again Yes|No\n')
            Restart = Restart.upper()
            if Restart == 'YES':
                print('\nLets begin anew them')
                sleep(0.5)
                break
            elif Restart == 'NO':
                print('\nThank you for playing. Goodbye!')
                BattleOn = False
                sleep(0.5)
                break
            else:
                print(f"\n{Restart} is not a valid option, try again")
    else:
        while Restart != 'YES' or Restart != 'NO':
            Restart = input('\nDo you wish to end your run now? Yes|No\n')
            Restart = Restart.upper()
            if Restart == 'NO':
                print('To the next battle then!\n')
                LevelUp(capybaramax, True)
                LevelUp(playermax, False)
                capybara['HP'], capybara['ATK'], capybara['DEF'] = capybaramax['MAX_HP'], capybaramax['MAX_ATK'], capybaramax['MAX_DEF']
                player['HP'], player['ATK'], player['DEF'] = playermax['MAX_HP'], playermax['MAX_ATK'], playermax['MAX_DEF']
                sleep(0.5)
                break
            elif Restart == 'YES':
                print('\nThank you for playing. Goodbye!')
                BattleOn = False
                sleep(0.5)
                break
            else:
                print(f"\n{Restart} is not a valid option, try again")

def LevelUp(entitymax : dict, enemy : bool):
    rang = random.randint(1, 100)
    if enemy:
        if rang < 40:
            increment = random.randint(1,2)
            entitymax['MAX_HP'] += increment*10
            entitymax['MAX_ATK'] += increment
            entitymax['MAX_DEF'] += increment
            return entitymax
        elif rang < 80:
            increment = random.randint(2,4)
            entitymax['MAX_HP'] += increment*10
            entitymax['MAX_ATK'] += increment
            entitymax['MAX_DEF'] += increment
            return entitymax
        else:
            increment = random.randint(3,5)
            entitymax['MAX_HP'] += increment*10
            entitymax['MAX_ATK'] += increment
            entitymax['MAX_DEF'] += increment
            return entitymax
    else:
        if rang < 30:
            increment = random.randint(1,2)
            entitymax['MAX_HP'] += increment*10
            entitymax['MAX_ATK'] += increment
            entitymax['MAX_DEF'] += increment
            return entitymax
        elif rang < 60:
            increment = random.randint(1,3)
            entitymax['MAX_HP'] += increment*10
            entitymax['MAX_ATK'] += increment
            entitymax['MAX_DEF'] += increment
            return entitymax
        elif rang < 90:
            increment = random.randint(2,4)
            entitymax['MAX_HP'] += increment*10
            entitymax['MAX_ATK'] += increment
            entitymax['MAX_DEF'] += increment
            return entitymax
        else:
            increment = random.randint(3,5)
            entitymax['MAX_HP'] += increment*10
            entitymax['MAX_ATK'] += increment
            entitymax['MAX_DEF'] += increment
            return entitymax