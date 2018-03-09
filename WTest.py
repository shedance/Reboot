import os
from time import sleep
from tkinter import *

class Dirlist (object):
    def __init__(self, initedir=None):
        self.top = Tk()
        self.label = Label(self.top, text = "Directory lister v1.2")
        self.label.pack()

        self.cwd = StringVar(self.top)
        self.cwd_lablel = Label(self.top, fg='red', font=('Helvetica', 12, 'bold'))
        self.cwd_lablel.pack()

        self.dirs_frame = Frame(self.top)

        self.sbar = Scrollbar(self.dirs_frame)
        self.sbar.pack(side=RIGHT,fill=Y)

        self.dirs_listbox = Listbox(self.dirs_frame,height=15, width=50,yscrollcommand=self.sbar.set)
        self.dirs_listbox.bind('<double-1>', self.setdirandgo)
        self.dirs_listbox.pack(side=LEFT, fill=BOTH)

        self.dirs_frame.pack()

        self.dirs_frame.pack()

        self.dirn = Entry(self.top, width = 50, textvariable=self.cwd)
        self.dirn.bind('<return>', self.doLS)
        self.dirn.pack()




def main():
    d=Dirlist(os.curdir)
    mainloop()
if __name__ == "__main__":
    main()