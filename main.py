from backend import *
from functions import *
from tkinter import *

root = Tk()

e = Entry(root)
e.grid(row=4, column=0 )
e.focus_set()


file_pick = Button(root, text="Browse", command=gui_file())
init_count = Button(root, text="Start", command=txt_count('test.txt'))
file_pick.grid(row=1, column=0)
init_count.grid(row=2, column=0)

root.mainloop()