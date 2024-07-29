
from customtkinter import CTk
from hints.utils.title import return_title


def create_window() -> CTk:
    '''Create the main window'''
    # Create the window
    root = CTk()

    # Manage the window size --
    root.geometry('500x500')
    root.minsize(300, 300)
    # -------------------------

    # Set the title to default title
    root.title(return_title())

    # Return the new window
    return root
