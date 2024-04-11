import random
import AsciiImgs

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
    {capybara['HP']}/{capybaramax['MAX_HP']} Health             {capybara['ATK']}/{capybaramax['MAX_ATK']} Attack                {capybara['DEF']}/{capybaramax['MAX_DEF']} Defense
-------------------------------------------------------------------
{AsciiImgs.capybaraImg}
-------------------------------------------------------------------
                            Player
    {player['HP']}/{playermax['MAX_HP']} Health               {player['ATK']}/{playermax['MAX_ATK']} Attack                  {player['DEF']}/{playermax['MAX_DEF']} Defense
----------------------------------------------1---------------------"""
    return print(GUI)

def Flee():
    
    roll = random.randint(1, 10)
    
    if roll == 10:
        return True
    else:
        return False

def StartBattle(BattleOn : bool):
    
    capybaratitle = SelTitle()
    
    capybaramax = {'MAX_HP' : 30, 'MAX_ATK' : 30, 'MAX_DEF' : 30}
    capybara = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}

    playermax = {'MAX_HP' : 30, 'MAX_ATK' : 30, 'MAX_DEF' : 30}
    player = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
    playerDefending = False
    
    while BattleOn:

        BattleScreen(capybara, capybaramax, player, playermax, capybaratitle)
        
        while True:
            Selection = input("A foe has appeared, what do you do\n> 1: Attack (a simple attack)\n> 2: Defend (diminish damage equal to your Defense attribute)\n> 3: Flee (1/10 change o skipping this fight, but you dont level up)\n")
            
            Selection = Selection.upper()
            
            if Selection in ("1", "ATTACK", "2", "DEFEND", "3", "FLEE"):
                break
            elif Selection in ("CLOSE","BREAK", "EXIT"):
                print("\nGoodbye.\n")
                GameOn = False
                break
            else:
                print(f"\n[{Selection}] is not a valid option choose a valid option\n")
    
        if Selection in ("1", "ATTACK"):
            capybara['HP'] = capybara['HP'] - player['ATK']
        elif Selection in ("2", "DEFEND"):
            playerDefending = True
        elif Selection in ("3", "FLEE"):
            roll = Flee()
            if roll == True:
                GameOn = False
                break
            else:
                continue
            
        

StartBattle(True)