from util.parser_util import parser_util
FUNCTIONS = [
    "chargen", 
    "namer", 
    "diceroll",
    "avg",
    "stats"
]

PROMPT = ">>> "

class Shell:
    def __init__(self):
        self.history = []
        last_command = None

        while last_command not in ["quit", "q"]:
            last_command, args = self.get_command()

    def get_command(self):
        command = input(PROMPT)
        command = command.lower()

        return (command[0], command[1:])

    def run_command(self, command, params):
        pass


def run_interactive():
    print("running in interactive mode.  Type help for help, quit to quit")
    Shell()

