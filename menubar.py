from tkinter import *

from tkinter import *

class MenuBar:
    def __init__(self, master):
        self.menubar = Menu(master)
        master.config(menu=self.menubar)

    def Files(self):
        file_menu = Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="New File")
        file_menu.add_command(label="Open File")
        file_menu.add_separator()
        file_menu.add_command(label="Save File")
        file_menu.add_command(label="Save As")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        self.menubar.add_cascade(label="File", menu=file_menu)

    def Edit(self):
        edit_menu = Menu(self.menubar, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        edit_menu.add_separator()
        edit_menu.add_command(label="Go to")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All")
        self.menubar.add_cascade(label="Edit", menu=edit_menu)

    def View(self):
        view_menu = Menu(self.menubar, tearoff=0)
        view_menu.add_command(label="Find")
        view_menu.add_command(label="Replace")
        view_menu.add_separator()
        view_menu.add_command(label="Word Count")
        view_menu.add_command(label="Character Count")
        self.menubar.add_cascade(label="View", menu=view_menu)



if __name__ == '__main__':

    root=Tk()
    root.title("Menubar")
    root.geometry("600x300")

    app = MenuBar(root)
    app.Files()
    app.Edit()
    app.View()
    
    root.mainloop()
