import termios
import os
import sys

from util.parser_util import parser_util, get_parser
from util.shell_util import *

shell_commands = {"help": help,
                  "list": list_commands
                }


def get_command(lineno):
    """ Function that grabs input until a newline or escape code is received

        Arguments:
            lineno (:class:`int`): the current line number.  Used for things
                                   like clearing the line and prompt

        Returns:
            the command intered once the user has pressed inter
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
        #regular character
        else:
            command += char

        sys.stdout.write(command) 
        sys.stdin.flush()

def run_command(lineno, command):
    """
        Runs the command provided and calls the utility

        Arguments:
            command (:class:`string`): the command to run as a string in the
                                       format it would be called from cli

        Note:
            The parser util command will handle printing to the screen in the
            non cannonical format.  
    """
    if isinstance(command, str):
        command = command.split()

    if command[0] in shell_commands.keys():
        lineno = shell_commands[command[0]](lineno, *command[1:])
        return lineno

    parser = get_parser(program=command[0])
    args = parser.parse_args(command)
    parser_util(args.which, args)

    return lineno


def run_interactive():
    """
        The main loop the shell mode

        First the old state of the teminal is saved and then the changed to
        a noncannonical terminal so we can handle anything the user enters into
        the program

        Then we get the command, decide what to do.  Also keeps track of the
        line number so the screen can be presented in a orderly format
    """ 
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
        if command == "quit":
            break
        if len(command) <= 0:
            continue
        try:
            lineno = run_command(lineno, command)
        except Exception as e:
            #currently no exception handling other than passing
            print("hit exception: {}".format(e))
        lineno += 1

    set_terminal_mode("canonical", old_term)
