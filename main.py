
# The main file that runs everything.

# Don't write __pycache__ ------
import sys

sys.dont_write_bytecode = True
# ------------------------------

from hints.control.hint_notebook import HintNotebook

if __name__ == '__main__':
    instance = HintNotebook()
