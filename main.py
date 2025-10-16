import shutil
import time
import sys
import time
import random
import colorama
from colorama import Fore, Back, Style, Cursor
from dir.func import heal, levelup
from dir.vis import slow_text, col_input, col_intinput, slash_animation
import os
from dir.riddles import answers, riddles

def clear_screen():
     os.system('cls')

colorama.init()
colour_text_menu = Fore.RED + Style.BRIGHT + Back.WHITE


#def prnt_below(text):
#    terminal_size = shutil.get_terminal_size()
#    width = terminal_size.columns
#    horizontal_padding = (width -len(text)) // 2
#    slow_text(" " * horizontal_padding + text)

stats = {
   
}

slow_text(colour_text_menu)

clear_screen()
slow_text(f'''before you start, you must choose a class,
          
            choose 1 for the priestess class - which has higher healing, but significantly lower attack and maxhealth,
          
            choose 2 for the tank class - which has alot of health, average attack, but can not heal,
          
            choose 3 for the warrior class - which has high attack, mediocre health, and mediocre healing

          
           ''')



classchoice = int(col_input(''))

while True:
  if classchoice == 1:
   stats = {
      'attack': 6,
      'maxhealth': 80,
      'heal': 30
   }
   break
  elif classchoice == 2:
     stats = {
        'attack': 10,
        'maxhealth': 300,
        'heal': 0

     }
     break
  elif classchoice == 3:
     stats = { 
        'attack': 20,
        'maxhealth': 100,
        'heal': 10
     }
     break
  else:
     print('invalid choice, please only enter 1, 2 or 3')
     classchoice = int(col_input(''))
  



print(stats)




#stats = {
#  'maxhealth' : 100,
#  'attack' : 10,
#  'heal' : 20
#
#}
health = stats['maxhealth']



money = 500
game = True
vchoice = False
while game == True and health > 0:
  dummy = {
    'health' : 50,
    'attack' : 1 
  }
  tutorial_text = f"""
                  .--.
                 /.  .l  
                 ||   \_)
          /^\     . --,
          _|_ .     ()
       <   |   >    ||
        \_____/     ||
         /a a\      ||
        /-.^.-\   (_|
      .  wwwww-._/|;
     /   wwwww  /; || |
    /` - wwwww- ;  || |
   ; ` =| www|=  _/|| |
   |   \| |~| |  |/ || |
   |\   \ | | |  ;  || |
   | \   ||=| |=<\  || |
   | /\_/\| | |  \`-||_/
   -| `; | | |  |  ||
    |  | | | |  |  ||
     |  |+| |+|  |  ||
     |    |  ||
     |_ _ _ _ _ _|  ||
     |,;,;,;,;,;,|  ||
      |||||||||||  ||
      |||||||||||   || """
  slash_animation(tutorial_text)

  tutorial_text = f"""
    
    Sensei:

    Welcome to zadonia, traveller

    Here you will learn to fight back against the demons that have been terrorising us

    But first, allow me to guide you through

    When in combat, you have the choice to either attack, defend, run, or heal (you can not heal past your max health)

    You will practice on this dummy
    You currently deal { stats['attack'] } damage per shot, the dummies health is 50


    """
  slow_text(tutorial_text)
  vheal = False
  chheal = ''

  while dummy['health'] > 0:

    slow_text('')

    while vchoice == False:
      
      

      print('The dummies health is', dummy['health'],'yours is', health, 'what would you like to do? ')
      
      slow_text('')
      
      choice = col_input('')
      if choice.lower() == 'attack':
        print('attack successful, you have done ', stats['attack'], 'damage',)
        dummy['health'] -= stats['attack']
        vchoice = True
      
      elif choice.lower() == 'heal':
        health = heal(health, stats, classchoice)
        vchoice = True
      
      elif choice.lower() == 'run':
        slow_text('you can not run in the tutorial fight, please choose again')
      
      elif choice.lower() == 'defend':
        print('the dummy attacks you, dealing', dummy['attack'] / 2, 'damage ')
        print()
        slow_text('defence successful')
        vchoice = True
        health -= dummy['attack'] / 2
      
      else: 
        slow_text('invalid choice')
        print()
    
    print()
    
    if choice != 'defend' and dummy['health'] > 0:
      print('the dummy attacks you, dealing', dummy['attack'], 'damage ')
      print()
      health -= dummy['attack']
      print()

    vchoice = False
  
    if health <= 0:
      slow_text('You died, the demon king lives on, the kingdom waits for their true hero ')
      exit()
      
    




  game = False


stats = levelup(stats, classchoice)



poisonturns = 0
game = True
while game == True:
  lvl1text1 = f''' 
    
    Sensei:

    Impressive, it has been a long time since I have seen a warrior with such potential, maybe we will finally be freed from the demon king's reign after all...


    Alas, you must leave though, take this horse, go, fight the demon king, save our country.
    



    You get on the horse and ride off into the countryside, with the city you just left slowly fading into the distance.




    After travelling for hours the sun starts to set and you realise you must rest, luckily you see a cave in the side of the mountain nearby, you grab some wood for 
    

    Exhausted and weary from your travel, you decide to take your respite in the cold embrace of the cave.

    
    You don't notice the allure of sleep claiming you, and wake up the gentle light of dawn beating against your face 

    
    This warmth, however, is broken by the startling sight of a furry eight legged creature crawling towards you.



    '''
  slow_text(lvl1text1)
  lvl1text1 = f'''
              (
               )
              (
        /\  .-"""-.  /|
       //\\/  ,,,  \//\\
       |/\| ,;;;;;, |/\|
       //\\\;-"""-;/// \\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-(() ())-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/


    ''' 
  
  slash_animation(lvl1text1)

  
  spider = {
    'attack' : 15,
    'health' : 150,
    'poison' :  4
  }

  pchance = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
  while spider['health'] > 0:
    vchoice = False
    print()
    print('The spiders health is', spider['health'],'yours is', health, 'what would you like to do? ')
      
    slow_text('')

    if poisonturns > 0:
        health -= spider['poison']
        poisonturns -= 1
        print('You have taken', spider['poison'], 'poison damage, you now have', poisonturns, 'turns left of poison')


    vpois = random.choice(pchance)

    while vchoice == False:
        choice = col_input('')
        if choice.lower() == 'attack':
            print('attack successful')
            spider['health'] -= stats['attack']
            vchoice = True

        elif choice.lower() == 'heal':
            health = heal(health, stats, classchoice)
            vchoice = True
      
        elif choice.lower() == 'run':
            print('you can not run in a boss fight, please choose again')
      
        elif choice.lower() == 'defend':
            print('the spider attacks you, dealing', spider['attack'] / 2, 'damage ')
            
            
            print('')
            slow_text('defence successful')
            vchoice = True
            health -= spider['attack'] / 2
      
        else: 
            slow_text('invalid choice')
            print()
            print()
    print()
    if choice != 'defend' and spider['health'] > 0:
        print('the spider attacks you, dealing', spider['attack'], 'damage ')
        stats['maxhealth'] -= spider['attack']
        print()
        if vpois == 1:
            slow_text('The spider has poisoned you, you will take an extra 4 damage per turn, the only way to cure poison is by healing')
            
            poisonturns = 2   
            print() 
        health -= spider['attack']

    if health <= 0:
        slow_text('you died, the demon king lives on, the kingdom waits for their true hero to arrive')
        exit()

        health -= spider['attack']

    if poisonturns > 0:
        print('You have', poisonturns, 'turns left of poison')
    vchoice = False
  
  
  
  
  
    




  game = False


stats = levelup(stats, classchoice)
slow_text(f'''

      idfk cuh u fall through floor explore floor and find sphinx, answer the riddle type shit  
          
          ''')
riddle, answer = random.choice(list(zip(riddles, answers)))
print(riddle)
print()
print('what is your answer? ')
temp = col_intinput('')
if temp == answer:
    print('Congratulations, you have got it correct, you may pass, be careful, it is dangerous up ahead ')
else:
    print('Incorrect, you are not worthy, now be punished '
    '')
    sphinx = {
       'attack': 25,
       'health': 200  
    }
    while sphinx['health'] > 0:
      vchoice = False
      
      print('The sphinx health is', sphinx['health'],'yours is', health, 'what would you like to do? ')
      
      slow_text('')


      while vchoice == False:
          choice = col_input('')
          if choice.lower() == 'attack':
              print('attack successful')
              sphinx['health'] -= stats['attack']
              vchoice = True

          elif choice.lower() == 'heal':
            health = heal(health, stats, classchoice)
            vchoice = True
      
          elif choice.lower() == 'run':
            print('you can not run in a boss fight, please choose again')
      
          elif choice.lower() == 'defend':
            print("the sphinx's attacks you, dealing", sphinx['attack'] / 2, 'damage ')
            
            
            print('')
            slow_text('defence successful')
            vchoice = True
            health -= sphinx['attack'] / 2
      
          else: 
            slow_text('invalid choice')
  
            print()
    
      if choice != 'defend' and sphinx['health'] > 0:
          print('the sphinx attacks you, dealing', sphinx['attack'], 'damage ')
          print()
          print() 

          health -= sphinx['attack']
      if health <= 0:
         slow_text('you have died, the demon king lives on, the kingdom waits for their true hero')
         exit()
     
  
