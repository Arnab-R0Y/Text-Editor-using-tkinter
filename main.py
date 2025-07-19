from tkinter import *
from menubar import MenuBar
from panel import SlideMenu

root = Tk()
root.title("Shashank's Text Editor")
root.geometry("700x800")

menu = MenuBar(root)
menu.Files()
menu.Edit()
menu.View()

#Toolbar Frame at top (for SlideMenu button)
toolbar_frame = Frame(root, bg="lightgrey", height=30)
toolbar_frame.pack(side=TOP, fill=X)

#Main Frame for Text and Scrollbar below toolbar
text_frame = Frame(root)
text_frame.pack(fill=BOTH, expand=True)

text = Text(text_frame, wrap=WORD, font=("Arial", 12))
text.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(text_frame, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scrollbar.set)

#Initialize SlideMenu with toolbar_frame and text
slide_menu = SlideMenu(root, text)
slide_menu.toolbar.destroy()  # Remove default toolbar created in SlideMenu
slide_menu.toolbar = toolbar_frame  # Assign our own toolbar frame
slide_menu.menu_button = Button(toolbar_frame, text=" ☰ ", command=slide_menu.toggle_menu)
slide_menu.menu_button.pack(side=LEFT, padx=2, pady=2)

root.mainloop()
