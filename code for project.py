
import sys
import time
import random

#def slow_text(text, min_delay=0.02, max_delay=0.3, newLine = False):
#  for char in text:
#    sys.stdout.write(char)
#    sys.stdout.flush()
#    time.sleep(random.uniform(min_delay, max_delay))
#
#  if newLine:
#      print()


stats = {
  'maxhealth' : 100,
  'attack' : 10,
  'heal' : 20

}

health = 100

money = 500
game = True
vchoice = False
while game == True and health > 0:
  dummy = {
    'health' : 50,
    'attack' : 1 
  }
  tutorial_text = f"""
    Sensei:

    Welcome to gameville, traveller

    Here you will learn to fight back against the demons that have been terrorising us

    But first, allow me to guide you through

    When in combat, you have the choice to either attack, defend, run, or heal (you can not heal past your max health)

    You will practice on this dummy
    You currently deal { stats['attack'] } damage per shot, the dummies health is 5.0


    """
  #slow_text(tutorial_text)
  print(tutorial_text)
  vheal = False
  chheal = ''
  while dummy['health'] > 0:
    print('')
    while vchoice == False:
      print('The dummies health is', dummy['health'],'yours is', health, 'what would you like to do? ')
      print('')
      choice = input('')
      if choice.lower() == 'attack':
        print('attack successful, you have done ', stats['attack'], 'damage')
        dummy['health'] -= stats['attack']
        vchoice = True
      elif choice.lower() == 'heal':
        health += stats['heal']
        if health >stats['maxhealth']:
          health =stats['maxhealth']
        print('you have chosen to heal, your health is now', health)
        vchoice = True
      elif choice.lower() == 'run':
        print('you can not run in the tutorial fight, please choose again')
      elif choice.lower() == 'defend':
        print('the dummy attacks you, dealing', dummy['attack'] / 2, 'damage ')
        print()
        print('defence successful')
        vchoice = True
        health -= dummy['attack'] / 2
      else: 
        print('invalid choice')
    print()
    if choice != 'defend' and dummy['health'] > 0:
      print('the dummy attacks you, dealing', dummy['attack'], 'damage ')
      print()
      health -= dummy['attack']
      print()

    vchoice = False
  if health <= 0:
    print('You died, the demon king lives on... ')
    break  
  game = False


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

poison = ''
game = True
while game == True:
  lvl1text1 = f''' 
    
    All of your stats now have improved by 5


    Sensei:

    Impressive, it has been a long time since I have seen a warrior with such potential, maybe we will finally be freed from the demon king's reign after all...


    Alas, you must leave though, take this horse, go, fight the demon king, save our country.
    



    You get on the horse and ride off into the countryside, with the city you just left slowly fading into the distance.




    After travelling for hours the sun starts to set and you realise you must rest, luckily you see a cave in the side of the mountain nearby, you grab some wood for 
    
    ''' 
  
  spider = {
    'attack' : 5

  }



