from tkinter import filedialog
from tkinter import messagebox

def output(data, data_filename):
    #saving the directory of file
    folder_dir = filedialog.askdirectory()

    if not folder_dir:
        messagebox.showwarning("Warning", "No directory selected")
        return
    
    with open(f'{folder_dir}/{data_filename}', 'w') as f:
        f.write(data)
        