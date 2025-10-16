import colorama
from colorama import Fore, Back, Style, Cursor
import time 
import sys
import random
import shutil 
import os

def slow_text(text, min_delay=0.05, max_delay=0.07, newLine = False, vertical_padding=True):
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

def slash_animation(art, delay=0.04, slash_char='/'):
    lines = art.strip().splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)

    term_width = shutil.get_terminal_size().columns

    print("\n" * height) 

    for step in range(width + height):
        print(Cursor.UP(height), end="")
        print(Cursor.FORWARD(0), end="")   
        for y, line in enumerate(lines):
            chars = list(line.ljust(width))
            pos = step - y
            if 0 <= pos < width:
                chars[pos] = slash_char
            line_str = "".join(chars)
            padding = max((term_width - len(line_str)) // 2, 0)
            print(" " * padding + line_str)
        time.sleep(delay)