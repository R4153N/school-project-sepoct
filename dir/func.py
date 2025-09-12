import sys
import time
import random



def slow_text(text, min_delay=0.005, max_delay=0.1, newLine = False):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(random.uniform(min_delay, max_delay))

  if newLine:
      print()

def heal(health, stats):
    health += stats['heal']
    if health > stats['maxhealth']:
        health = stats['maxhealth']
    return health



def levelup():
  lvlvalid = False
  levels = ''
  temp = f''' 
  
    Congratulations, you have leveled up after defeating the dummy, please choose between upgrading either maxhealth, attack or your healing ability, 

    please choose either maxhealth, attack or heal.

    '''
  print(temp)
  while lvlvalid == False:
    print('')
    levels = input('')
    levels = levels.lower()
    if levels in stats:
      stats[levels] += 5
    
      lvlvalid = True
    else:
      print(' You did not make a valid choice, please only choose maxhealt, attack or heal ')


  levels  = ''
  lvlvalid = False
  temp = f''' 

    Your max health is now {stats['maxhealth']},

    Your attack is now {stats['attack']}, 

    Your healing power is now {stats['heal']}
  

  '''
  print(temp)
