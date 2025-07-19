from tkinter import filedialog, messagebox, simpledialog
from tkinter import simpledialog
from tkinter import *

class MenuCommands:

    def __init__(self, master, text_widget):
        self.master = master
        self.text = text_widget
        self.file_path = None

    def new_file(self):
        self.text.delete(1.0, "end")
        self.file_path = None
        self.master.title("Untitled - Text Editor")

    def open_file(self):
        file = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text.delete(1.0, "end")
                self.text.insert("end", content)
                self.file_path = file
                self.master.title(f"{file} - Text Editor")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file:\n{e}")

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w", encoding="utf-8") as f:
                    f.write(self.text.get(1.0, "end-1c"))
                self.master.title(f"{self.file_path} - Text Editor")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")
        else:
            self.save_as()

    def save_as(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file:
            try:
                with open(file, "w", encoding="utf-8") as f:
                    f.write(self.text.get(1.0, "end-1c"))
                self.file_path = file
                self.master.title(f"{file} - Text Editor")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")

    def exit_app(self):
        self.master.destroy()

    def undo(self):
        try:
            self.text.event_generate("<<Undo>>")
        except:
            pass  # In case undo stack is empty

    def redo(self):
        try:
            self.text.event_generate("<<Redo>>")
        except:
            pass

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def go_to_line(self):
        try:
            line = simpledialog.askinteger("Go To Line", "Enter line number:")
            if line is not None and line > 0:
                total_lines = int(self.text.index('end-1c').split('.')[0])
                if line <= total_lines:
                    self.text.mark_set("insert", f"{line}.0")
                    self.text.see(f"{line}.0")
                else:
                    messagebox.showerror("Error", "Line number exceeds total lines.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input:\n{e}")

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end-1c")

    def find_text(self):
        search_term = simpledialog.askstring("Find", "Enter text to find:")
        if search_term:
            self.text.tag_remove("find_match", "1.0", END)
            idx = "1.0"
            found = False
            while True:
                idx = self.text.search(search_term, idx, nocase=1, stopindex=END)
                if not idx:
                    break
                lastidx = f"{idx}+{len(search_term)}c"
                self.text.tag_add("find_match", idx, lastidx)
                idx = lastidx
                found = True
            if not found:
                messagebox.showinfo("Result", f"'{search_term}' not found.")
            else:
                self.text.tag_config("find_match", background="yellow", foreground="black")

    def replace_text(self):
        find_word = simpledialog.askstring("Replace", "Find what:")
        replace_word = simpledialog.askstring("Replace", "Replace with:")
        if find_word and replace_word is not None:
            content = self.text.get("1.0", END)
            if find_word not in content:
                messagebox.showinfo("Result", f"'{find_word}' not found.")
            else:
                new_content = content.replace(find_word, replace_word)
                self.text.delete("1.0", END)
                self.text.insert("1.0", new_content)
                messagebox.showinfo("Result", f"All occurrences of '{find_word}' replaced.")

    def word_count(self):
        word = simpledialog.askstring("Word Count", "Enter the word to count:")
        if word:
            content = self.text.get("1.0", "end-1c")
            count = content.count(word)
            if count > 0:
                messagebox.showinfo("Word Count", f"The word '{word}' appears {count} times.")
            else:
                messagebox.showinfo("Word Count", f"The word '{word}' was not found.")

    def character_count(self):
        char = simpledialog.askstring("Character Count", "Enter the character to count:")
        if char:
            if len(char) != 1:
                messagebox.showwarning("Invalid Input", "Please enter a single character.")
                return
            content = self.text.get("1.0", "end-1c")
            count = content.count(char)
            if count > 0:
                messagebox.showinfo("Character Count", f"The character '{char}' appears {count} times.")
            else:
                messagebox.showinfo("Character Count", f"The character '{char}' was not found.")


    

