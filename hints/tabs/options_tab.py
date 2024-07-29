
# A class hosting all of the basic options,
# for more flexible and future-proof code

from customtkinter import CTk, CTkButton, CTkFrame
from hints.gui_management.managers import ResetUtils
from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants import tab_names


class OptionsTab(ResetUtils):
    '''Hosts all of the Option Tab setup.'''
    def __init__(self, notebook_frame: NotebookFrame, root: CTk) -> None:
        '''Create the tab with the options, flexibly.'''
        # Initialize the resetter
        super().__init__(notebook_frame, root)

        # Create the tab itself
        options_tab = self.add_tab(tab_names.options_tab_name)

        # And a sub frame for the buttons
        buttons_frame = CTkFrame(master=options_tab)
        buttons_frame.pack(padx=5, pady=5)

        # Race Mode ---------------------------------------
        race_button = CTkButton(command=self.race_mode,
                                master=buttons_frame,
                                text='Race Mode')
        race_button.grid(column=0, padx=5, pady=5, row=0)
        # -------------------------------------------------

        # Reset Tracker ------------------------------------
        reset_button = CTkButton(command=self.reset,
                                  master=buttons_frame,
                                  text='Reset Tracker')
        reset_button.grid(column=1, padx=5, pady=5, row=0)
        # --------------------------------------------------

    def race_mode(self) -> None:
        '''The command for race mode.'''
        # Get permission to reset the tracker
        if not self.show_warning():
            return

        # Go through the data tabs
        for index, tab_name in [*enumerate(tab_names.data_tab_names)]:
            # Reset the notes tab
            if index == 0:
                self.reset_tab(tab_name)
                continue

            # Close everything else
            self.close_tab(tab_name)

        self.notebook_frame.set_to_notes_tab()

    def reset(self) -> None:
        '''A wrapper for the tracker reset.'''
        # Get permission to reset the tracker
        if not self.show_warning():
            return

        # Reset the tracker
        self.reset_tracker()
