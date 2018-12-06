import tkinter as tk
from tkinter import filedialog as fd
w = tk.Tk()
def new_file():
    global txt
    txt.delete('1.0', tk.END)
def open_file():
    global txt
    openlocation1 = fd.askopenfilename(filetypes = (("text files", "*.txt"), ("All files", ".*")))
    f1 = open(openlocation1, 'r')
    content = f1.read()
    txt.insert(tk.END, content)
menu = tk.Menu(w)
w.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'New', command = new_file)
file_menu.add_command(label = 'Open', command = open_file)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command = exit)
help_menu = tk.Menu(menu)
menu.add_cascade(label = 'Help', menu = help_menu)
help_menu.add_command(label = 'Documentation')
help_menu.add_command(label = 'Check for Updates')
help_menu.add_separator()
help_menu.add_command(label = 'About me')
w.title("Text Editor")
txt = tk.Text(w)
txt.pack()
def saveas():
    global txt
    content = txt.get("1.0", "end-1c")
    savelocation = fd.asksaveasfilename()
    file = open(savelocation, "w+")
    file.write(content)
    file.close()
b = tk.Button(w, text = 'Save As...', command = saveas)
b.pack()
q = tk.Button(w, text = 'QUIT!', activeforeground = 'red', command = quit)
q.pack()
w.mainloop()