import tkinter as tk

# https://baijiahao.baidu.com/s?id=1812301955119941804

def makeEntry(root):
    text = tk.StringVar()
    entry = tk.Entry(
        root,
        textvariable=text,
    )
    entry.pack(padx=10, pady=10, expand=True)