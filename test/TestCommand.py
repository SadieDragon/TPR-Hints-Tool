
from tkinter import END, Tk

def read_tab(root: Tk) -> None:
    '''Figure out how to get the info from nothing but root'''
    notebook = root.winfo_children()[0]
    # => {'!frame': <tkinter.Frame object .!notebook.!frame>}

    frame = [*notebook.children.values()][0]
    # => .!notebook.!frame

    frame_contents = frame.children
    # => {'!button': <tkinter.Button object .!notebook.!frame.!button>,
    #     '!frame': <tkinter.Frame object .!notebook.!frame.!frame>}
    # interesting.

    sub_frame_contents = [*frame_contents.values()][1].children
    # => {'!scrollbar': <tkinter.Scrollbar object .!notebook.!frame.!frame.!scrollbar>, '!scrolledtext': <tkinter.scrolledtext.ScrolledText object .!notebook.!frame.!frame.!scrolledtext>}

    # text = textbox.get("1.0", END)

    print(sub_frame_contents)
    # print(text)