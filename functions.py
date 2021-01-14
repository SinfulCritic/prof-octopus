from tkinter import filedialog
from tkinter import *

def gui_file():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    return filename