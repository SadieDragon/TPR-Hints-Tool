
# Hosts the main window creation, running,
# and also some basic utitlies acting upon it.

from customtkinter import CTk
from hints.gui_management.window_manager import create_window
from hints.gui_management.notebook_frame import NotebookFrame
from hints.gui_management.tab_creator import TabCreator


class HintNotebook:
    '''The main window.'''
    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Create the window
        root = create_window()

        # Create the main notebook
        notebook = NotebookFrame(root)

        # Create the tabs
        TabCreator(notebook, root)

        # Run the window
        root.mainloop()
