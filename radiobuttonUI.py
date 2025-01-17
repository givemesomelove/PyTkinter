import tkinter as tk
from tkinter.messagebox import showinfo

# https://baijiahao.baidu.com/s?id=1813935665361134887

def makeRadiobutton(root):
    frame = tk.Frame(root)
    frame.pack()

    selected = tk.StringVar()

    def show_selected():
        showinfo(title='结果',message=selected.get())

    r1 = tk.Radiobutton(frame, text='Option 1', value='Value 1', variable=selected)
    r1.pack(anchor="w")
    r2 = tk.Radiobutton(frame, text='Option 2', value='Value 2', variable=selected)
    r2.pack(anchor="w")
    r3 = tk.Radiobutton(frame, text='Option 3', value='Value 3', variable=selected)
    r3.pack(anchor="w")

    button = tk.Button(root, text="获取成绩", command=show_selected)
    button.pack(padx=5, pady=5)

