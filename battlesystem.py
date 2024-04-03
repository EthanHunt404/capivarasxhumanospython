import random

def Battle(state : bool):
    
    InBattle : bool = state
    
    capybara = {HP : 30, ATK : 3, DEF : 0}
    capybaraBonus = {HPb : 0, ATKb : 0, DEFb : 0}
    
    player = {HP : 30, ATK : 3, DEF : 0}
    playerBonus = {HPb : 0, ATKb : 0, DEFb : 0}
    
    while InBattle:
        capybara[HP] += capybaraBonus[HPb]
        capybara[ATK] += capybaraBonus[ATKb]
        capybara[DEF] += capybaraBonus[DEFb]
        
        player[HP] += capybaraBonus[HPb]
        player[ATK] += capybaraBonus[ATKb]
        player[DEF] += capybaraBonus[DEFb]