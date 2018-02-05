import termios
import os
import sys

from util.parser_util import parser_util, get_parser
from util.shell_util import *

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
            command += tabout(command)
        #this should be ctrl l but I can't get it to work
        elif char == '\00c':
            pass
        #regular character
        else:
            command += char

        sys.stdout.write(command) 
        sys.stdin.flush()

def check_command(command, commands=FUNCTIONS):
    return command in commands

def display_result(result, lineno):
    alter = 0
    for line in result:
        move_cursor(0, lineno + alter)
        print(line)
        alter += 1
    return alter

def run_command(command, lineno):
    if isinstance(command, str):
        command = command.split()
    parser = get_parser(program=command[0])
    args = parser.parse_args(command)

    result = parser_util('shell', args.which, args)

    alter = display_result(result, lineno)

    return lineno + alter

def handle_command(command, lineno):
        if command == "quit":
            return -1
        if len(command) <= 0:
            return lineno
        if not check_command(command.split()[0]):
            print("INVALID COMMAND")
            return lineno
        else:
            try:
                if command in custom_commands.keys():
                    custom_commands[command]()
                    return get_new_lineno(lineno, command)
                else:
                    return run_command(command, lineno)
            except:
                return lineno

def run_interactive():
    global old_term; global height; global width
    height, width = list(map(int, os.popen('stty size', 'r').read().split()))
    old_term = termios.tcgetattr(STDIN_FILENO)

    set_terminal_mode("non-canonical", old_term)
    clear_screen()
    move_cursor(0, 0)
    print("running in interactive mode.  Type help for help, quit to quit")
    move_cursor(0, 1)
    
    lineno = 3
    while True:
        command = get_command(lineno)
        lineno += 1
        move_cursor(0, lineno)
        
        result = handle_command(command, lineno)
        if result == -1:
            break
        lineno = result

    set_terminal_mode("canonical", old_term)
