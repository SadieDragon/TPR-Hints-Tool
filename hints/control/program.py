
# Avoids the risk of circular imports. Somehow.

class Program:
    # The global variable of the notepad to add to
    notebook = None

    # The global variable of the data tabs.
    data_tabs = {}

    # Functions that are required elsewhere. --
    def close_all_tabs(self) -> None:
        '''Close all of the tabs.'''
        pass

    def create_notepad_tab(self) -> None:
        '''Recreate the primary tab.'''
        pass

    def reset_tracker(self) -> None:
        '''Completely reset the tracker.'''
        pass
    # -----------------------------------------
