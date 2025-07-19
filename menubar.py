from tkinter import *

from menu_commands import MenuCommands


class MenuBar:
    def __init__(self, master, text_widget):
        self.menubar = Menu(master)
        master.config(menu=self.menubar)
        self.commands = MenuCommands(master, text_widget)

    def Files(self):
        file_menu = Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="New File", command=self.commands.new_file)
        file_menu.add_command(label="Open File", command=self.commands.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save File", command=self.commands.save_file)
        file_menu.add_command(label="Save As", command=self.commands.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.commands.exit_app)
        self.menubar.add_cascade(label="File", menu=file_menu)

    def Edit(self):
        edit_menu = Menu(self.menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.commands.undo)
        edit_menu.add_command(label="Redo", command=self.commands.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.commands.cut)
        edit_menu.add_command(label="Copy", command=self.commands.copy)
        edit_menu.add_command(label="Paste", command=self.commands.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Go to", command=self.commands.go_to_line)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.commands.select_all)
        self.menubar.add_cascade(label="Edit", menu=edit_menu)

    def View(self):
        view_menu = Menu(self.menubar, tearoff=0)
        view_menu.add_command(label="Find", command=self.commands.find_text)
        view_menu.add_command(label="Replace", command=self.commands.replace_text)

        view_menu.add_separator()
        view_menu.add_command(label="Word Count", command=self.commands.word_count)
        view_menu.add_command(label="Character Count", command=self.commands.character_count)
        self.menubar.add_cascade(label="View", menu=view_menu)



if __name__ == '__main__':
    root = Tk()
    root.title("Menubar")
    root.geometry("600x300")

    text = Text(root)
    text.pack()

    app = MenuBar(root, text)
    app.Files()
    app.Edit()
    app.View()

    root.mainloop()

