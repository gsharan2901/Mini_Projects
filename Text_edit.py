import tkinter as tk
from tkinter import filedialog as fd
w = tk.Tk()
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
w.mainloop()