__author__ = 'Kyle Vitautas Lopin'

"""
User Interface to perform ICA/ICQ analysis on cells
"""
import Tkinter as tk
import init_frames as fi

class ICQ_ICA_GUI(tk.Frame, object):
    """
    Class to make a tkinter frame that allows a user to:
    import 2 pictures
    measure the ICA / ICQ of the two pictures
    create graphs of the data
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #fi.make_picture_frame(self)
        self.initUI(master)

    def initUI(self, master):
        fi.make_frames_ICA(self, master)


def main():
    """
    call custom class ICA ICQ GUI
    :return:
    """
    root=tk.Tk()
    root.title("ICA ICQ analyzer")
    root.geometry("600x400")
    ICQ_ICA_GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()