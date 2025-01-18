import tkinter as tk

# https://baijiahao.baidu.com/s?id=1817739866675474284

def makeGrid(root):
    frame = tk.Frame(root)
    frame.grid(column=0, row=0)

    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=0, row=0, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=1, row=0, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=2, row=0, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=0, row=1, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='red')
    button.grid(column=1, row=1, columnspan=2, sticky=tk.EW, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='red')
    button.grid(column=0, row=2, rowspan=2, sticky=tk.NS, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=1, row=2, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=2, row=2, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=1, row=3, ipadx=15, ipady=15)
    button = tk.Button(frame, text="按钮", bg='green')
    button.grid(column=2, row=3, ipadx=15, ipady=15)