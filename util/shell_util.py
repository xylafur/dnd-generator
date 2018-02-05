import tty
import termios
import sys

from util.parser_util import parsers

class DNDShellException(Exception):pass

"""**************************Globals**************************"""
STDIN_FILENO = 0

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

def clear():
    clear_screen()
    move_cursor(0, 0)

def get_new_lineno(lineno, function):
    if function == 'clear':
        return 0
    return lineno

custom_commands = {
    'list': list_commands,
    'help': help,
    'clear': clear
}

FUNCTIONS = list(parsers.keys()) + list(custom_commands.keys())
ARGS = {key: val for key, val in \
        zip(FUNCTIONS, \
            [val['args'] for val in parsers.values()])}

PROMPT = "dnd> "
prompt_len = len(PROMPT)

old_term = None 
height = 0
width = 0

def move_cursor(x, y):
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.flush()

def clear_screen():
    print("\033[2J")

def clear_line(lineno):
    move_cursor(0, lineno)
    print("\033[K")

def set_terminal_mode(mode, old_term):
    if mode == "canonical":
        print(old_term)
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

def tabout(command):
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






        
