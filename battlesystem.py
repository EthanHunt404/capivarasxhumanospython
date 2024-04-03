import random
import AsciiImgs

capybara = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
capybaraBonus = {'HPb' : 0, 'ATKb' : 0, 'DEFb' : 0}
capybaraTitle = {"" : ""}

player = {'HP' : 30, 'ATK' : 3, 'DEF' : 0}
playerBonus = {'HPb' : 0, 'ATKb' : 0, 'DEFb' : 0}

BattleScreen = f"""
--------------------------------------------------------------------------
{capybara['HP']}/Health {capybara['ATK']}/Attack {capybara['DEF']}/Defense
--------------------------------------------------------------------------
{AsciiImgs.capybaraImg}
----------------------------------------------------------------------

----------------------------------------------------------------------
"""

print(BattleScreen)