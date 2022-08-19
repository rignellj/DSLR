import sys
from time import sleep
import pandas as pd

def handle_open(file: str):
    try:
        return pd.read_csv(file, index_col=False)
    except FileNotFoundError:
        print('Second argument should be file')
        sleep(2)
        exit(1)
    except PermissionError:
        print('You don\'t have succifient permissions')
        sleep(2)
        exit(1)
    except IsADirectoryError:
        print('Your second argument is directory. Argument should be file')
        sleep(2)
        exit(1)

def check_args():
    if len(sys.argv) != 2:
        print('There should be two arguments')
        sleep(2)
        exit(1)
    return sys.argv[1]