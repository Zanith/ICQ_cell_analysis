__author__ = 'Kyle Vitautas Lopin'

import Tkinter as tk
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk
import tifffile as tiff

def clickedOn(self, event, _frame, frame_number):
    """
    One of the picture frames was clicked on for the first time
    :param event: the click
    :param _frame: which frame was clicked on, to put the image in
    :param frame_number: where to save the image too
    :return:
    """
    filename = askopenfilename()
    if filename:
        loadPicture(self, _frame, frame_number, filename)


def loadPicture(self, _frame, frame_number, filename):

    im = Image.open(filename)
    im2 = tiff.imread(filename)
    # save to self so that the program has access to the image after this function closes
    if hasattr(self, 'photoim'+str(frame_number)):
        # this will not be the first time the program is run
        pack_picture = False
    else:
        # this is the first time the program has been run
        pack_picture = True
    if len(im2.shape) > 2: # a stack of images was loaded
        setattr(self, 'number_stacks'+str(frame_number), im2.shape[0])
    else: # a single image was loaded
        setattr(self, 'number_stacks'+str(frame_number), 1)

    setattr(self, 'photo_data_type'+str(frame_number), im2.dtype)

    setattr(self, 'photoim'+str(frame_number), ImageTk.PhotoImage(im))
    setattr(self, 'photo_name'+str(frame_number), filename)
    # display the picture and the filename for reference
    if pack_picture:
        # this is the first time an image is loaded so it also has to be displayed
        setattr(self, 'picture_in_frame'+str(frame_number),
                tk.Label(_frame, image=eval('self.photoim'
                                            +str(frame_number))))
        eval('self.picture_in_frame'+str(frame_number)).pack()

        setattr(self, 'filename_in_pic_frame'+str(frame_number),
                tk.Label(_frame, text=filename))
        eval('self.filename_in_pic_frame'+str(frame_number)).pack()

        tk.Button(_frame, text="Change picture",
                  command=lambda: clickedOn(self, 1, _frame, frame_number)).pack()
    else:
        # change the image displayed
        eval('self.picture_in_frame'+str(frame_number)).\
            config(image=eval('self.photoim'+str(frame_number)))

        eval('self.filename_in_pic_frame'+str(frame_number)).config(text=filename)

    # if the images displayed are a stack then display a scroll bar that can be used
    # to scroll through the stacks
    config_scrollbar(self, frame_number)

def config_scrollbar(self, frame_number):

    if eval('self.number_stacks'+str(frame_number)) == 1:
        # a single image was loaded
        self.scrollbar_label = tk.Label(self.picture_stack_scroll_frame)
        self.scrollbar_label.config(text="Single image loaded")
        self.scrollbar_label.pack()
# def UpdatePicture(self, _frame, frame_num):
