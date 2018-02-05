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
prompt_len = len(PROMPT)

old_term = None 
height = 0
width = 0

def move_cursor(x, y):
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.flush()

def clear_screen():
    global height; global width
    move_cursor(0, 0)
    for _ in range(height):
        for _ in range(width):
            sys.stdout.write(" ")
            sys.stdin.flush()

def clear_line(lineno):
    global width
    move_cursor(0, lineno)
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

def write_command_and_prompt(lineno, command):
    move_cursor(0, lineno)
    sys.stdout.write(PROMPT)
    move_cursor(prompt_len + 2, lineno)
    sys.stdout.write(command)
    sys.stdout.flush()

def get_command(lineno):
    """ Function that grabs input until a newline or escape code is received
    """
    get_char = lambda: sys.stdin.read(1)
    command = ""
    while True:
        clear_line(lineno)
        write_command_and_prompt(lineno, command)
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
            print("regular char")
            command += char


        sys.stdout.write(command) 
        sys.stdin.flush()

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
    move_cursor(0, 0)
    print("running in interactive mode.  Type help for help, quit to quit")
    move_cursor(0, 1)
    
    lineno = 3
    while True:
        command = get_command(lineno)
        lineno += 1
        move_cursor(0, lineno)
        if command == "quit":
            break
        if len(command) <= 0:
            continue
        try:
            run_command(command)
        except:
            print("hit exception running command")
        lineno += 1

    set_terminal_mode("canonical")


