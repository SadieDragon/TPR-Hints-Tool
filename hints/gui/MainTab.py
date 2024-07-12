from hints.gui.Program import Program
from hints.gui.pick_spoiler import spoiler_pop_up
from os import abort
from tkinter import Button, Frame, messagebox


class MainTab:
    program = None

    def __init__(self, program: Program, main_page: Frame):
        '''Creates the buttons responsible for the different pop ups.'''
        self.program = program

        # Where I want things placed
        button_placement = {
            'Pick Spoiler Log': [0, 0],
            'Reset Tracker': [0, 1],
            'Race Mode': [1, 0],
        }

        for text, (row, column) in button_placement.items():
            # Create then place the new button
            new_button = Button(main_page, text=text)
            new_button.grid(padx=5, pady=5, row=row, column=column)

            # Configure the button commands
            if text == 'Pick Spoiler Log':
                new_button.config(command=lambda: spoiler_pop_up(program))
            elif text == 'Race Mode':
                new_button.config(command=lambda: self.verify_reset(True))
            elif text == 'Reset Tracker':
                new_button.config(command=lambda: self.verify_reset())
            else:
                print(f'There is no command for {text}, dev.')
                abort()

    def verify_reset(self, race_mode=False) -> None:
        '''Have the user verify they want to reset.'''
        # A warning of "are you sure, mate?" PEP8 compliance
        if not self.program.has_unsaved_data():
            self.program.reset(race_mode)
            return

        warning = 'Are you sure? This will wipe everything.'
        if messagebox.askokcancel('Verify Reset', warning):
            self.program.reset(race_mode)
