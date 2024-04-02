import random

def Battle(state : bool):
    
    InBattle : bool = state
    
    capibara = {HP : 30, ATK : 3, DEF : 0}
    capibaraBonus = {HPb : 0, ATKb : 0, DEFb : 0}
    
    player = {HP : 30, ATK : 3, DEF : 0}
    playerBonus = {HPb : 0, ATKb : 0, DEFb : 0}
    
    while InBattle:
        capibara[HP] += capibaraBonus[HPb]
        capibara[ATK] += capibaraBonus[ATKb]
        capibara[DEF] += capibaraBonus[DEFb]
        
        player[HP] += capibaraBonus[HPb]
        player[ATK] += capibaraBonus[ATKb]
        player[DEF] += capibaraBonus[DEFb]