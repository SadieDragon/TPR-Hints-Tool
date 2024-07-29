
# Holds all of the deletion utilities for the tracker

from hints.gui_management.notebook_frame import NotebookFrame


class DeletionUtils:
    '''A class for all of the deletion utilities.'''
    # The notebook instance
    notebook_frame = NotebookFrame

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        '''Update the instances.'''
        self.notebook_frame = notebook_frame

    def close_tab(self, tab_name: str) -> None:
        '''Close a tab in the notebook.'''
        try:
            # Close the tab
            self.notebook_frame.notebook.delete(tab_name)

            # Remove the key, it no longer exists
            del self.notebook_frame.data_tabs[tab_name]
        except ValueError:
            pass
