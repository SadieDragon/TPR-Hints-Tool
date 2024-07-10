
from tkinter import Frame, Tk


def read_root(root: Tk) -> None:
    '''Simply reading the root window.'''
    notebook = root.winfo_children()[0]
    # => [<tkinter.ttk.Notebook object .!notebook>]

    tabs = notebook.winfo_children()
    # => [<tkinter.Frame object .!notebook.!frame>,
    #     <tkinter.Frame object .!notebook.!frame2>,
    #     <tkinter.Frame object .!notebook.!frame3>,
    #     <tkinter.Frame object .!notebook.!frame4>]
    # (Main, Notes, Agitha, Jovani)

    for index, tab in [*enumerate(tabs)]:
        if index == 1:
            tab_frame = tab.winfo_children()[0]
            test_reset(tab_frame)

    # print(notebook.winfo_children())


def test_reset(frame: Frame) -> None:
    '''Destroy the frame, as a test.'''
    frame.destroy()