from tkinter import *

class LineNumber(Canvas):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, width=40, background='lightgrey', **kwargs)
        self.text_widget = text_widget

        # Hook events
        self.text_widget.bind("<KeyRelease>", self.redraw)
        self.text_widget.bind("<MouseWheel>", self.redraw)
        self.text_widget.bind("<ButtonRelease>", self.redraw)
        self.text_widget.bind("<Configure>", self.redraw)

        # Override Text's yscrollcommand
        self.text_widget.config(yscrollcommand=self.on_textscroll)

        self.redraw()

    def on_textscroll(self, *args):
        # Set the scrollbar linked with text widget
        if hasattr(self.text_widget.master.master, 'scrollbar'):
            self.text_widget.master.master.scrollbar.set(*args)
        # Redraw line numbers on every scroll
        self.redraw()

    def redraw(self, event=None):
        self.delete("all")
        index = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(index)
            if dline is None:
                break
            y = dline[1]
            linenum = str(index).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, font=self.text_widget['font'])
            index = self.text_widget.index(f"{index}+1line")
