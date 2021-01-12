from count import *
from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.focus_set()

init_count = Button(root, text="Start", command=txt_count('test.txt'))
init_count.pack()

root.mainloop()