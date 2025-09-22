import colorama
from colorama import Fore, Back, Style
import time 
import sys
import random
import shutil 
import os 
import shutil

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