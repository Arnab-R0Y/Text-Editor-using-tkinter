from tkinter import *
from tkinter import colorchooser

class SlideMenu:
    def __init__(self, master, text_widget, shared_font):
        self.master = master
        self.shared_font = shared_font
        self.text_widget = text_widget
        self.menu_visible = False

        # Toolbar
        self.toolbar = Frame(master, bg="lightgrey", height=30)
        self.toolbar.pack(fill=X)


        self.menu_button = Button(self.toolbar, text=" ☰ ", command=self.toggle_menu)
        self.menu_button.pack(side=LEFT, padx=2, pady=2)

        # Side Menu Frame
        self.menu_frame = Frame(master, bg="white", width=200, height=800, relief=RAISED, borderwidth=2)
        self.menu_frame.place(x=-200, y=30)

        # Buttons inside menu_frame
        self.theme_btn = Button(self.menu_frame, text="Theme", padx=14, pady=4, relief=GROOVE, command=self.toggle_theme_sub)
        self.theme_btn.pack(fill=X, pady=2)

        self.font_btn = Button(self.menu_frame, text="Font", padx=14, pady=4, relief=GROOVE, command=self.toggle_font_sub)
        self.font_btn.pack(fill=X, pady=2)

        self.color_btn = Button(self.menu_frame, text="Color", padx=14, pady=4, relief=GROOVE, command=self.change_text_color)
        self.color_btn.pack(fill=X, pady=2)

        self.size_btn = Button(self.menu_frame, text="Text Size", padx=14, pady=4, relief=GROOVE, command=self.toggle_size_sub)
        self.size_btn.pack(fill=X, pady=2)

        self.themes = {
        "Light": {
            "text_bg": "white",
            "text_fg": "black",
            "insert_bg": "black",
            "toolbar_bg": "lightgrey",
            "menu_bg": "white"
            },
        "Dark": {
            "text_bg": "#2e2e2e",
            "text_fg": "#f5f5f5",
            "insert_bg": "#f5f5f5",
            "toolbar_bg": "#3a3a3a",
            "menu_bg": "#3a3a3a"
            },
        "Solarized Dark": {
            "text_bg": "#002b36",
            "text_fg": "#839496",
            "insert_bg": "#93a1a1",
            "toolbar_bg": "#073642",
            "menu_bg": "#073642"
            },
        "Monokai": {
            "text_bg": "#272822",
            "text_fg": "#f8f8f2",
            "insert_bg": "#f8f8f0",
            "toolbar_bg": "#383830",
            "menu_bg": "#383830"
            }
        }


        # Submenus (initially hidden)
        self.theme_sub = Frame(master, bg="lightgrey", relief=RAISED, borderwidth=2)
        for theme_name in self.themes.keys():
            Button(self.theme_sub, text=theme_name, command=lambda t=theme_name: self.apply_theme(t)).pack(fill=X)


        self.font_sub = Frame(master, bg="lightgrey", relief=RAISED, borderwidth=2)
        Button(self.font_sub, text="Default (System)", command=self.set_default_font).pack(fill=X)
        for f in ["Arial", "Courier", "Times", "Helvetica"]:
            Button(self.font_sub, text=f, command=lambda ff=f: self.set_font(ff)).pack(fill=X)

        self.size_sub = Frame(master, bg="lightgrey", relief=RAISED, borderwidth=2)
        self.size_slider = Scale(self.size_sub, from_=8, to=40, orient=HORIZONTAL)
        self.size_slider.pack(fill=X)

        Button(self.size_sub, text="✔ Set", command=self.apply_text_size).pack(pady=2)


    def hide_all_subs(self):
        self.theme_sub.place_forget()
        self.font_sub.place_forget()
        self.size_sub.place_forget()

    def toggle_theme_sub(self):
        self.hide_all_subs()
        if not self.theme_sub.winfo_ismapped():
            bx = self.menu_frame.winfo_x() + self.menu_frame.winfo_width()
            by = self.theme_btn.winfo_rooty() - self.master.winfo_rooty()
            self.theme_sub.place(x=bx, y=by)

    def toggle_font_sub(self):
        self.hide_all_subs()
        if not self.font_sub.winfo_ismapped():
            bx = self.menu_frame.winfo_x() + self.menu_frame.winfo_width()
            by = self.font_btn.winfo_rooty() - self.master.winfo_rooty()
            self.font_sub.place(x=bx, y=by)

    def toggle_size_sub(self):
        self.hide_all_subs()
        if not self.size_sub.winfo_ismapped():
            bx = self.menu_frame.winfo_x() + self.menu_frame.winfo_width()
            by = self.size_btn.winfo_rooty() - self.master.winfo_rooty()
            self.size_sub.place(x=bx, y=by)

    def apply_theme(self, theme_name):
        theme = self.themes.get(theme_name)
        if theme:
            self.text_widget.config(bg=theme["text_bg"], fg=theme["text_fg"], insertbackground=theme["insert_bg"])
            self.toolbar.config(bg=theme["toolbar_bg"])
            self.menu_frame.config(bg=theme["menu_bg"])
        self.hide_all_subs()

    def set_default_font(self):
        self.text_widget.config(font=("TkDefaultFont", 12))
        self.hide_all_subs()

    def set_font(self, font_name):
        self.text_widget.config(font=(font_name, 12))
        self.hide_all_subs()

    def set_text_size(self, size):
        current_font = self.text_widget.cget("font").split()[0]
        self.shared_font.configure(size=int(size))


    def apply_text_size(self):
        size = self.size_slider.get()
        self.shared_font.configure(size=int(size))
        self.hide_all_subs()


    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_widget.config(fg=color)
        self.hide_all_subs()

    def toggle_menu(self):
        if self.menu_visible:
            self.hide_menu()
        else:
            self.show_menu()

    def show_menu(self):
        def slide_in():
            x = self.menu_frame.winfo_x()
            if x < 0:
                self.menu_frame.place(x=x+20, y=30)
                self.master.after(10, slide_in)
            else:
                self.menu_visible = True
        slide_in()

    def hide_menu(self):
        def slide_out():
            x = self.menu_frame.winfo_x()
            if x > -200:
                self.menu_frame.place(x=x-20, y=30)
                self.master.after(10, slide_out)
            else:
                self.menu_visible = False
                self.hide_all_subs()
        slide_out()

if __name__ == "__main__":
    from tkinter import font

    root = Tk()
    root.geometry("700x800")

    # Toolbar frame at the top
    toolbar_frame = Frame(root)
    toolbar_frame.pack(side=TOP, fill=X)

    # Text Frame below the toolbar
    text_frame = Frame(root)
    text_frame.pack(fill=BOTH, expand=True)

    shared_font = font.Font(family="Arial", size=12)

    text = Text(text_frame, wrap=WORD, font=shared_font)
    text.pack(side=LEFT, fill=BOTH, expand=True)

    slide = SlideMenu(root, text, shared_font)  # Pass shared_font here

    slide.toolbar.destroy()
    slide.toolbar = toolbar_frame
    slide.menu_button = Button(slide.toolbar, text=" ☰ ", command=slide.toggle_menu)
    slide.menu_button.pack(side=LEFT, padx=2, pady=2)

    root.mainloop()




