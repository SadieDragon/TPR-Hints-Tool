
from customtkinter import CTk
from hints.utils.title import return_title


def create_window() -> CTk:
    '''Create the main window'''
    # Create the window
    root = CTk()

    # Manage the window size --------------
    root.geometry('500x500')
    root.minsize(300, 300)
    # -------------------------------------

    # Set the title to default title
    root.title(return_title())

    # Return the new window
    return root


def change_title(root: CTk, seed_name: str = '') -> None:
    '''Change the title of the window.'''
    # The default without the seed name
    title = 'TPR Hint Notebook'
    # If there was a seed name, append it
    if seed_name:
        title = f'{title} ({seed_name})'

    # Update the title of the window
    root.title(title)
