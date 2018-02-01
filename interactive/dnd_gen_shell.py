import termios
import tty
import os
import sys

from util.parser_util import parser_util, get_parser

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
    sys.stdout.write("\033[0;0H".format(y, x))

def clear_screen():
    global height; global width
    move_cursor(0, 0)
    for _ in range(height):
        for _ in range(width):
            sys.stdout.write(" ")
            sys.stdin.flush()

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

def get_command(starting_height):
    """ Function that grabs input until a newline or escape code is received
    """
    get_char = lambda: sys.stdin.read(1)
    command = ""
    while True:
        char = get_char()
        #ctrl ^ C
        if char == "\x03":
            return "quit"
        #escape char(exc, arrow keys)
        if char == '\x1b':
            if sys.stdin.read(1) == '[':
                next_char = sys.stdin.read(1)
                #up arrow
                if next_char == 'A':
                    pass
                #down arrow
                elif next_char == 'B':
                    pass
                #left arrow
                elif next_char == 'D':
                    pass
                #right arrow
                elif next_char == 'C':
                    pass
                #delete key
                elif next_char == '3' and sys.stdin.read(1) == '~':
                    pass
        #newline
        elif char == '\n' or char == '\r':
            return command
        #backspace
        elif char == "\x7f":
            command = command[:-1]
        #tab
        elif char == "\t":
            print("got tab!")
        #regular character
        else:
            command += char
        clear_screen()
        move_cursor(0, starting_height)
        print(command)

def run_command(command):
    if isinstance(command, str):
        command = command.split()
    parser = get_parser(program=command[0])
    args = parser.parse_args(command)
    parser_util(args.which, args)

def list_commands():
    print("listing all functions, for more info ask help")
    for function in FUNCTIONS:
        print(function)
    
def help(command=None):
    if not command:
        print("This is the dnd interactive cli shell.\n"
              "You can run commands in the same way you would directly from bash\n"
              "If you want help for a specific command, type help <command name>\n")
    else:
        pass

def run_interactive():
    global old_term; global height; global width
    height, width = list(map(int, os.popen('stty size', 'r').read().split()))
    old_term = termios.tcgetattr(STDIN_FILENO)
    set_terminal_mode("non-canonical")
    print("running in interactive mode.  Type help for help, quit to quit")
    move_cursor(0, 1)

    while True:
        command = get_command(1)
        if command == "quit":
            break
        if len(command) <= 0:
            continue
        try:
            run_command(command)
        except Exception as e:
            pass

    set_terminal_mode("canonical")


