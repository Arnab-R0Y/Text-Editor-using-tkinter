from tkinter import *

class LineNumber(Text):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=2, padx=4, pady=2, takefocus=0, border=0, background='lightgrey',
                         state='disabled', **kwargs)
        self.text_widget = None

    def attach_text_widget(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.bind("<KeyRelease>", self.update_line_numbers)
        self.text_widget.bind("<ButtonRelease>", self.update_line_numbers)

    def update_line_numbers(self, event=None):
        if not self.text_widget:
            return
        line_count = int(self.text_widget.index('end-1c').split('.')[0])
        lines = "\n".join(str(i) for i in range(1, line_count + 1)) or "1"
        self.config(state='normal')
        self.delete(1.0, 'end')
        self.insert(1.0, lines)
        self.config(state='disabled')



if __name__ == '__main__':

    root = Tk()
    root.geometry("500x400")

    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)

    line_numbers = LineNumber(frame)
    line_numbers.pack(side=LEFT, fill=Y)

    text = Text(frame, wrap="word", undo=True)
    text.pack(side=LEFT, fill=BOTH, expand=True)

    line_numbers.attach_text_widget(text)

    root.mainloop()


