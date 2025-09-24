import shutil
import time
import sys
import time
import random
import colorama
from colorama import Fore, Back, Style
from dir.func import heal, levelup
from dir.vis import slow_text
import os
from dir.riddles import answers, riddles

def clear_screen():
     os.system('cls')

colorama.init()
colour_text_menu = Fore.GREEN + Style.BRIGHT + Back.BLACK


#def prnt_below(text):
#    terminal_size = shutil.get_terminal_size()
#    width = terminal_size.columns
#    horizontal_padding = (width -len(text)) // 2
#    slow_text(" " * horizontal_padding + text)


slow_text(colour_text_menu)

clear_screen()
  


stats = {
  'maxhealth' : 100,
  'attack' : 10,
  'heal' : 20

}
health = int(100)



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
  print(tutorial_text)

  tutorial_text = f"""
    
    Sensei:

    Welcome to gameville, traveller

    Here you will learn to fight back against the demons that have been terrorising us

    But first, allow me to guide you through

    When in combat, you have the choice to either attack, defend, run, or heal (you can not heal past your max health)

    You will practice on this dummy
    You currently deal { stats['attack'] } damage per shot, the dummies health is 5.0


    """
  slow_text(tutorial_text)
  vheal = False
  chheal = ''

  while dummy['health'] > 0:

    slow_text('')

    while vchoice == False:
      
      

      print('The dummies health is', dummy['health'],'yours is', health, 'what would you like to do? ')
      
      slow_text('')
      
      choice = input(Fore.BLUE + '')
      slow_text(Fore.GREEN + '')
      if choice.lower() == 'attack':
        print('attack successful, you have done ', stats['attack'], 'damage',)
        dummy['health'] -= stats['attack']
        vchoice = True
      
      elif choice.lower() == 'heal':
        health = heal(health, stats)
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
    
    if choice != 'defend' and dummy['health'] > 0:
      print('the dummy attacks you, dealing', dummy['attack'], 'damage ')
      print()
      health -= dummy['attack']
      print()

    vchoice = False
  
  if health <= 0:
    slow_text('You died, the demon king lives on... ')
    break  
  
  game = False


stats = levelup(stats)



poisonturns = 0
game = True
while game == True:
  lvl1text1 = f''' 
    
    Sensei:

    Impressive, it has been a long time since I have seen a warrior with such potential, maybe we will finally be freed from the demon king's reign after all...


    Alas, you must leave though, take this horse, go, fight the demon king, save our country.
    



    You get on the horse and ride off into the countryside, with the city you just left slowly fading into the distance.




    After travelling for hours the sun starts to set and you realise you must rest, luckily you see a cave in the side of the mountain nearby, you grab some wood for 
    
    
    You feel exhau

    #more text to be added# 

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
  
  print(lvl1text1)

  
  spider = {
    'attack' : 5,
    'health' : 150,
    'poison' :  4
  }

  pchance = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
  while spider['health'] > 0:
    vchoice = False
      
    print('The dumspidersmies health is', spider['health'],'yours is', health, 'what would you like to do? ')
      
    slow_text('')

    if poisonturns > 0:
        health -= spider['poison']
        poisonturns -= 1
        print('You have taken', spider['poison'], 'poison damage, you now have', poisonturns, 'turns left of poison')


    vpois = random.choice(pchance)

    while vchoice == False:
        choice = input(Fore.BLUE + '')
        slow_text(Fore.GREEN + '')
        if choice.lower() == 'attack':
            print('attack successful')
            spider['health'] -= stats['attack']
            vchoice = True

        elif choice.lower() == 'heal':
            health = heal(health, stats)
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
    
    if choice != 'defend' and spider['health'] > 0:
        print('the spider attacks you, dealing', spider['attack'], 'damage ')
        print()
        if vpois == 1:
            slow_text('The spider has poisoned you, you will take an extra 4 damage per turn, the only way to cure poison is by healing')
            poisonturns = 2   
            print() 

        health -= spider['attack']

    if poisonturns > 0:
        print('You have', poisonturns, 'turns left of poison')
    vhoice = False
  game = False


guessleft = 1
riddle = random.randint(0, 5)
print(riddles[riddle])
answer = answers[riddle]
print()
print('what is your answer? ')
temp = input()
if temp == answer:
    print('Congratulations, you have got it correct, you may pass, be careful, it is dangerous up ahead ')
else:
    print('Incorrect, you are not worthy, now be punished '
    '')
#sphinx type shit