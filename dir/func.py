import sys
import time
import random
import colorama
from colorama import Fore, Back, Style
from dir.vis import slow_text

def heal(health, stats):
    health += stats['heal']
    if health > stats['maxhealth']:
        health = stats['maxhealth']
    return health



def levelup(stats):
  lvlvalid = False
  levels = ''
  temp = f''' 
  
    Congratulations, you have leveled up after defeating the dummy, please choose between upgrading either maxhealth, attack or your healing ability, 

    please choose either maxhealth, attack or heal.

    '''
  slow_text(temp)
  while lvlvalid == False:
    slow_text('')
    levels = input(Fore.BLUE + '')
    slow_text(Fore.GREEN + '')
    levels = levels.lower()
    if levels in stats:
      stats[levels] += 5
    
      lvlvalid = True
    else:
      slow_text(' You did not make a valid choice, please only choose maxhealt, attack or heal ')


  levels  = ''
  lvlvalid = False
  temp = f''' 

    Your max health is now {stats['maxhealth']},

    Your attack is now {stats['attack']}, 

    Your healing power is now {stats['heal']}
  

  '''
  return(stats)
  slow_text(temp)
