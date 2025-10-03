import colorama
from colorama import Fore, Back, Style
import time 
import sys
import random
import shutil 
import os

def slow_text(text, min_delay=0.01, max_delay=0.02, newLine = False, vertical_padding=True):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines
    
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
        
             
        
        
    if newLine:
            print()

def col_input(prompt, color = Fore.BLUE):
    print(Fore.BLUE)
    if prompt.strip != '':
        a = input(f'{prompt}')
        
    else:
        a = input(Fore.BLUE)
    print(Fore.RED)
    return a
def col_intinput(prompt):
     b = 0
     print(Fore.BLUE)
     if prompt.strip != '':
          while True:
                
                try:
                   a = int(input(prompt))
                   c = 1
                except:
                     print('please enter a number ')
                
                if c == 1:
                     c = 0
                     break
     else:
          while True:
                
                try:
                    a = int(input(Fore.BLUE))
                    c = 1
                except:
                     print('please enter a number')
                if c == 1:
                     c = 0
                     break
     print(Fore.RED)
     return a

