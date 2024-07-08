
# Don't write __pycache__
import sys
sys.dont_write_bytecode = True

from TestPage import create_tab
from tkinter import Tk

root = Tk()

create_tab(root)

root.mainloop()