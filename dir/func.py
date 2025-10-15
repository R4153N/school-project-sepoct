import sys
import time
import random
import colorama
from colorama import Fore, Back, Style, Cursor
from dir.vis import slow_text, col_input

def heal(health, stats, classchoice):
  if classchoice != 2:
    health += stats['heal']
    if health > stats['maxhealth']:
        health = stats['maxhealth']
    return health
  
  else:
    print('you have chosen the tank class and thus can not heal')
    return health



def levelup(stats, classchoice):
  levels = ''
  temp = f''' 
  
    Congratulations, you have leveled up after defeating the dummy, please choose between upgrading either maxhealth, attack or your healing ability, 

    please choose either maxhealth, attack or heal.

    '''
  slow_text(temp)
  while True:
    slow_text('')
    levels = col_input(Fore.BLUE + '')
    slow_text(Fore.RED + '')
    levels = levels.lower()
    if classchoice == 2 and levels == 'heal':
      print('you have chosen the tank class and have attempted to upgrade healing, which you can not do, despite your ignorance I will allow you to choose again')
    elif levels == 'heal':
      stats[levels] += 5
      break
    elif levels == 'attack':
      stats[levels] += 5
      break
    elif levels == 'maxhealth':
      stats['maxhealth'] += 10
      break
    else:
      slow_text(' You did not make a valid choice, please only choose maxhealth, attack or heal ')


  levels  = ''
  lvlvalid = False
  temp = f''' 

    Your max health is now {stats['maxhealth']},

    Your attack is now {stats['attack']}, 

    '''
  print(temp)
  if classchoice != 2:
    print('Your healing power is now', stats['heal'])

  

  return(stats)
