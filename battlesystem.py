import random

capybara = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
capybaraBonus = {'HPb' : 0, 'ATKb' : 0, 'DEFb' : 0}
capybaraTitle = {"" : ""}

player = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
playerBonus = {'HPb' : 0, 'ATKb' : 0, 'DEFb' : 0}

capybaraImg = file.read('capybara.txt')
BattleScreen : str = f"""
--------------------------------------------------------------------------
{capybara['HP']}/Health {capybara['ATK']}/Attack {capybara['DEF']}/Defense
--------------------------------------------------------------------------
{capybaraImg}
----------------------------------------------------------------------

----------------------------------------------------------------------
"""

def Battle(state : bool):
    
    print("A battle has commenced")
        
    InBattle : bool = state
    
    while InBattle:
        capybara['HP'] += capybaraBonus['HPb']
        capybara['ATK'] += capybaraBonus['ATKb']
        capybara['DEF'] += capybaraBonus['DEFb']
        
        player['HP'] += capybaraBonus['HPb']
        player['ATK'] += capybaraBonus['ATKb']
        player['DEF'] += capybaraBonus['DEFb']
        
        