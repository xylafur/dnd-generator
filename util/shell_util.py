import tty
import termios
import sys

from util.parser_util import parsers

class DNDShellException(Exception):pass

"""**************************Globals**************************"""
STDIN_FILENO = 0

FUNCTIONS = list(parsers.keys())
ARGS = {key: val for key, val in \
        zip(FUNCTIONS, \
            [val['args'] for val in parsers.values()])}

PROMPT = "dnd> "
prompt_len = len(PROMPT)

old_term = None 
height = 0
width = 0

"""**************************Util Function**************************"""

def move_cursor(x, y):
    """ 
        moves the cursor to the designated coordinates

        Arguments:
            x (:class:`int`): the x coordinate 
            y (:class:`int`): the y coordinate
    """
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.flush()

def clear_screen():
    """ 
        clears the terminal screen via a special escape code
    """
    print("\033[2J")

def clear_line(lineno):
    """ 
        Clears the specified line via a special escape code

        Arguments:
            lineno (:class:`int`): the line number of the line to clean
    """
    move_cursor(0, lineno)
    print("\033[K")

def set_terminal_mode(mode, old_term):
    """ 
        changes the terminal to the specified mode

        Arguments:
            mode (:class:`str`): what mode to change the terminal into
            old_term (:class:`termios terminal`): the old terminal, must be 
                                                  created outside this function

        Raises:
            DNDShellException if an invalid terminal mode is supplied
    """
    if mode == "canonical":
        termios.tcsetattr(STDIN_FILENO, termios.TCSANOW, old_term)
    elif mode == "non-canonical":
        tty.setraw(STDIN_FILENO)
    else:
        raise DNDShellException("Invalid Terminal Mode")
    clear_screen()
    move_cursor(0, 0)

def write_command_and_prompt(lineno, command):
    """ 
        writes the command prompt and the characters the the user has entered
        at the specified lineno

        Arguments:
            lineno (:class:`int`): the linenumber of the line to print the 
                                   prompt command

            command (:class:`str`): The current characters that the user has 
                                    enterd
    """
    move_cursor(0, lineno)
    sys.stdout.write(PROMPT)
    move_cursor(prompt_len + 2, lineno)
    sys.stdout.write(command)
    sys.stdout.flush()

def list_commands(lineno):
    """ 
        lists all of the valid commands in the shell

        Arguments:
            lineno (:class:`int`): the line to start printing the commands at
    """
    print("listing all functions, for more info ask help")
    for function in FUNCTIONS:
        print(function)
        lineno += 1
        move_cursor(0, lineno)
    
def help(lineno, command=None):
    """ 
        print help either for the shell or for the supplied command

        Arguments:
            lineno (:class:`int`): the lineno to start printing the help on

            command (:class:`string`): the command to get help for, optional
    """
    if not command:
        print("This is the dnd interactive cli shell.\n"
              "You can run commands in the same way you would directly from bash\n"
              "If you want help for a specific command, type help <command name>\n")
    else:
        pass
def tabout(command):
    """ 
        tabout ro finish the partial command that the user has entered    

        Arguments:
            command (:class:`str`): partial command to finish
    """
    match = False
    match_str = ""

    #possible arg parsing for future implemetation
    """
    for comm in FUNCTIONS:
        if comm in command and '-' in command:
            if '--' in command:
                start = command.find('--')
                for arg in ARGS[comm]:
                    if command[start:] in arg:
                        pass 
            else:
                return ""
    """
    for comm in FUNCTIONS:
        if command in comm:
            if not match:
                match = True
                match_str = comm
            else:
                return ""
    return match_str[len(command):]
