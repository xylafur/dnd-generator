import termios
import tty
import os
import sys

from util.parser_util import parser_util

class DNDShellException(Exception):pass

"""**************************Globals**************************"""
STDIN_FILENO = 0

FUNCTIONS = [
    "chargen", 
    "namer", 
    "diceroll",
    "avg",
    "stats"
]

PROMPT = "dnd> "

old_term = None 
height = 0
width = 0

def move_cursor(x, y):
    print("\033[0;0H".format(y, x), end="")

def clear_screen():
    global height; global width
    move_cursor(0, 0)
    for _ in range(height):
        for _ in range(width):
            print(' ', end='')

def set_terminal_mode(mode):
    global old_term
    if mode == "canonical":
        termios.tcsetattr(STDIN_FILENO, termios.TCSANOW, old_term)
    elif mode == "non-canonical":
        tty.setraw(STDIN_FILENO)
    else:
        raise DNDShellException("Invalid Terminal Mode")
    clear_screen()
    move_cursor(0, 0)
    
def run_interactive():
    global old_term; global height; global width
    height, width = list(map(int, os.popen('stty size', 'r').read().split()))
    old_term = termios.tcgetattr(STDIN_FILENO)
    set_terminal_mode("non-canonical")
    print("running in interactive mode.  Type help for help, quit to quit")
    cur_char = sys.stdin.read(1)
    set_terminal_mode("canonical")


