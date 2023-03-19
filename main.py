import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")

        self.textarea = tk.Text(master, font=('Arial', 14))
        self.textarea.pack(fill=tk.BOTH, expand=True)

        # create menu bar
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        # create file menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

    def new_file(self):
        self.textarea.delete('1.0', tk.END)

    def open_file(self):
        file = filedialog.askopenfile(parent=self.master, mode='rb', title="Select a file")
        if file is not None:
            content = file.read()
            self.textarea.insert('1.0', content)

    def save_file(self):
        file = filedialog.asksaveasfile(mode='w')
        if file is not None:
            # slice off the last character from get, as an extra return is added
            data = self.textarea.get('1.0', tk.END+'-1c')
            file.write(data)
            file.close()

root = tk.Tk()
notepad = Notepad(root)
root.mainloop()
