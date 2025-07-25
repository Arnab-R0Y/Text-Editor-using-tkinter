from tkinter import *
import tkinter.font as tkfont


from menubar import MenuBar
from panel import SlideMenu
from line_number import LineNumber

root = Tk()
root.title("Shashank's Text Editor")
root.geometry("700x800")

shared_font = tkfont.Font(family="Arial", size=12)

#Toolbar Frame at top (for SlideMenu button)
toolbar_frame = Frame(root, bg="darkgrey", height=30)
toolbar_frame.pack(side=TOP, fill=X)

# Main Frame for Line Numbers, Text, and Scrollbar
text_frame = Frame(root)
text_frame.pack(fill=BOTH, expand=True)

# Text Widget (pack first)
text = Text(text_frame, wrap=WORD, font=shared_font, undo=True)

# Line Number Sidebar (Canvas-based)
line_numbers = LineNumber(text_frame, text, bg="lightgrey")

# Pack in correct order
line_numbers.pack(side=LEFT, fill=Y)
text.pack(side=LEFT, fill=BOTH, expand=True)

menu = MenuBar(root,text)
menu.Files()
menu.Edit()
menu.View()

# Scrollbar on RIGHT
scrollbar = Scrollbar(text_frame, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scrollbar.set)

#Initialize SlideMenu with toolbar_frame and text
slide_menu = SlideMenu(root, text, shared_font)
slide_menu.toolbar.destroy()  # Remove default toolbar created in SlideMenu
slide_menu.toolbar = toolbar_frame  # Assign our own toolbar frame
slide_menu.menu_button = Button(toolbar_frame, text=" ☰ ", command=slide_menu.toggle_menu)
slide_menu.menu_button.pack(side=LEFT, padx=2, pady=2)

root.mainloop()