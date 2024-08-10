
from hints.gui_management.notebook_frame import NotebookFrame
from .create_save_dir import CreateSaveDir
from .collect_notebook_data import CollectNotebookData


class SaveNotes:
    '''A class that hosts the utilities for saving your notes.'''

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        '''Store the notebook instance,
           and initialize saving functions.'''

        # Grab the data to write to saving
        collected_data = CollectNotebookData(notebook_frame).notebook_data

        # Write the save folder
        dir_writing_instance = CreateSaveDir(collected_data)
