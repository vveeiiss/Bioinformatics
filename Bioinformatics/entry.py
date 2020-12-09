import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class InputDialog(object):
    # root is a parent widget same as root = Tk()
    def __init__(self, root):
        # The toplevel windows have the title bars, borders, and other window decorations
        top = self.top = tk.Toplevel(root)

        self.input_entry = tk.Text(root=top)
        self.input_entry.pack()

        self.browse_btn = tk.Button(
            root=top, text='Upload File', command=self.ask_Upload_file_dialog)
        self.browse_btn.pack()

        self.submit_btn = tk.Button(
            root=top, text='submit', command=self.submit)
        self.submit_btn.pack()

        self.data_file = None
        self.data = None

    def submit(self):
        if self.data_file is not None:
            self.data = self.data_file.read()
        else:
            self.data = self.input_entry.get(1.0, tk.END)

        top.destroy()

    def ask_Upload_file_dialog(self):
        filename = filedialog.askopenfilename(parent=top)
        try:
            self.data_file = open(filename, 'r')
        except FileNotFoundError:
            messagebox.showwarning(
                title='Bad file', message='No files selected')

    def show(self):
        #Displays the window
        top.deiconify()
        #it waits until the given window is destroyed
        top.wait_window()
        return self.data
