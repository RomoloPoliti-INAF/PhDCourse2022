from functools import wraps
from time import sleep

from rich import print
from rich.console import Console
from rich.status import Status

from commons import MSG

##########################################
# Commands
##############################


def message(text: str):
    def decorate(f):
        @wraps(f)
        def inner(*args, **kwargs):
            print(f"{MSG.INFO}TM(1,7)")
            with Status(text, spinner='aesthetic', console=args[0].console):
                ret = f(*args, **kwargs)
                if args[0].verbose:
                    
                    print(f"{MSG.INFO} {f.__name__} executed")
            return ret
        return inner
    return decorate


class MECommands:
    def __init__(self, verbose: bool = False, console: Console = None):
        self.verbose = verbose
        self.console = console

    @message(text='Booting...')
    def NSS00001(self):
        """Boot Command"""
        print(f'{MSG.INFO}[magenta]TM(5,1)[/magenta] - Boot Report')
        sleep(5)

    @message(text='Shuting down...')
    def NSS00002(self):
        """Shuting Down Command"""
        sleep(5)


class PECommands:
    def __init__(self, verbose: bool = False, console: Console = None):
        self.verbose = verbose
        self.console = console

    @message(text="PE...ON ")
    def NSS00003(self):
        """PE ON Command"""
        sleep(1)
