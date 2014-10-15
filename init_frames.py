__author__ = 'Kyle Vitautas Lopin'

import Tkinter as tk
import ICA_actions as actions

def make_frames_ICA(self, master):
    column_numbers = 6
    row_numbers = 30
    self.grid()
    for x in range(column_numbers):
        tk.Grid.columnconfigure(master, x, weight=1)
    for y in range(row_numbers):
        tk.Grid.rowconfigure(master, y, weight=1)

    picture1_frame = tk.Frame(bd=1, relief="ridge")
    picture2_frame = tk.Frame(bd=1, relief="ridge")
    self.picture_stack_scroll_frame = tk.Frame()

    tk.Label(picture1_frame, text='Click to load picture').pack()
    tk.Label(picture2_frame, text='Click to load picture').pack()
    #picture1_frame.pack(side='left', fill='both', expand=True)
    #picture2_frame.pack(side='left',fill='both', expand=True)

    #information_frame = tk.Frame()
    #tk.Label(information_frame, text='hello').pack()
    #information_frame.pack(side="bottom", fill='x')

    #self.pictures_frame.pack(fill='both', expand=True)

    """
    list of things to put into the grid manager
    picture1_frame
    picture2_frame
    self.picture_stack_scroll_frame
    """
    pad = 10
    picture1_frame.grid(row=0, column=0, columnspan=3, rowspan=20,
                        sticky='wnes', padx=pad, pady=pad)
    picture2_frame.grid(row=0, column=3, columnspan=3, rowspan=20,
                        sticky='wnes', padx=pad, pady=pad)
    self.picture_stack_scroll_frame.grid(row=22, column=0, columnspan=6,
                                         sticky='we', padx=pad/2)

    """
    add actions to the frames
    """
    picture1_frame.bind("<Button-1>",
                        lambda event, arg=picture1_frame:
                        actions.clickedOn(self, event, picture1_frame, 1))
    picture2_frame.bind("<Button-1>",
                        lambda event, arg=picture2_frame:
                        actions.clickedOn(self, event, picture2_frame, 2))

def make_picture_frame(self):
    output_frame = tk.Frame
