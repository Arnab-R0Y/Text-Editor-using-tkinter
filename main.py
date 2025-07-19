from tkinter import *
from tkinter import scrolledtext

from menubar import MenuBar

root = Tk()
root.title("Shashank's Text Editor")
root.geometry("700x800")

menu=MenuBar(root)
menu.Files()
menu.Edit()
menu.View()

# Frame to hold Text + Scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

text = Text(frame, wrap=WORD)
text.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame, command=text.yview)
text.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)

def autohide_scrollbar(event=None):
    if text.yview() == (0.0, 1.0):  # Content fits
        scrollbar.pack_forget()
    else:
        scrollbar.pack(side=RIGHT, fill=Y)

text.bind("<Configure>", autohide_scrollbar)
text.bind("<KeyRelease>", autohide_scrollbar)

root.mainloop()
