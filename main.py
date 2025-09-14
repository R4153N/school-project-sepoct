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

def clear_screen():
     os.system('cls')

colorama.init()
colour_text_menu = Fore.GREEN + Style.BRIGHT + Back.BLACK


def prnt_below(text):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    horizontal_padding = (width -len(text)) // 2
    slow_text(" " * horizontal_padding + text)


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
      .  {'wwwww'}-._/|;
     /   {'wwwww'}  /; || |
    /` - {'wwwww'}- ;  || |
   ; ` =| {'www'}|=  _/|| |
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
  slow_text(tutorial_text, vertical_padding=False)
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
        slow_text('attack successful, you have done ', stats['attack'], 'damage',)
        dummy['health'] -= stats['attack']
        vchoice = True
      
      elif choice.lower() == 'heal':
        health = heal(health, stats)
        vchoice = True
      
      elif choice.lower() == 'run':
        slow_text('you can not run in the tutorial fight, please choose again')
      
      elif choice.lower() == 'defend':
        slow_text('the dummy attacks you, dealing', dummy['attack'] / 2, 'damage ')
        slow_text()
        slow_text('defence successful')
        vchoice = True
        health -= dummy['attack'] / 2
      
      else: 
        slow_text('invalid choice')
    
    slow_text()
    
    if choice != 'defend' and dummy['health'] > 0:
      slow_text('the dummy attacks you, dealing', dummy['attack'], 'damage ')
      slow_text()
      health -= dummy['attack']
      slow_text()

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
       //\\\;-"""-;///\\
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
      
    slow_text('The dumspidersmies health is', spider['health'],'yours is', health, 'what would you like to do? ')
      
    slow_text('')

    if poisonturns > 0:
        health -= spider['poison']
        poisonturns -= 1
        slow_text('You have taken', spider['poison'], 'poison damage, you now have', poisonturns, 'turns left of poison')


    vpois = random.choice(pchance)

    while vchoice == False:
        choice = input(Fore.BLUE + '')
        slow_text(Fore.GREEN + '')
        if choice.lower() == 'attack':
            slow_text('attack successful, you have done ', stats['attack'], 'damage',)
            spider['health'] -= stats['attack']
            vchoice = True

        elif choice.lower() == 'heal':
            health = heal(health, stats)
            vchoice = True
      
        elif choice.lower() == 'run':
            slow_text('you can not run in a boss fight, please choose again')
      
        elif choice.lower() == 'defend':
            slow_text('the spider attacks you, dealing', spider['attack'] / 2, 'damage ')
            
            
            slow_text()
            slow_text('defence successful')
            vchoice = True
            health -= spider['attack'] / 2
      
        else: 
            slow_text('invalid choice')
    
            slow_text()
    
    if choice != 'defend' and spider['health'] > 0:
        slow_text('the spider attacks you, dealing', spider['attack'], 'damage ')
        slow_text()
        if vpois == 1:
            slow_text('The spider has poisoned you, you will take an extra 4 damage per turn, the only way to cure poison is by healing')
            poisonturns = 2   
            slow_text() 

        health -= spider['attack']

    if poisonturns > 0:
        slow_text('You have', poisonturns, 'turns left of poison')
    vhoice = False
  game = False

#sphinx type shit