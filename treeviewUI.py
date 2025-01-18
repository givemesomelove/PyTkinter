import tkinter as tk
from tkinter import ttk

def makeTreeview(root):
    tree = ttk.Treeview(root)
    tree.heading('#0', text='行政区划', anchor=tk.W)

    tree.insert('', tk.END, text='山东省', iid=0, open=False)
    tree.insert('', tk.END, text='江苏省', iid=1, open=False)
    tree.insert('', tk.END, text='吉林省', iid=2, open=False)
    tree.insert('', tk.END, text='北京市', iid=3, open=False)
    tree.insert('', tk.END, text='上海市', iid=4, open=False)

    tree.insert('', tk.END, text='济南', iid=5, open=False)
    tree.insert('', tk.END, text='青岛', iid=6, open=False)
    tree.insert('', tk.END, text='淄博', iid=7, open=False)
    tree.move(5, 0, 0)
    tree.move(6, 0, 1)
    tree.move(7, 0, 2)
    tree.insert('', tk.END, text='长春', iid=8, open=False)
    tree.insert('', tk.END, text='吉林', iid=9, open=False)
    tree.move(8, 2, 0)
    tree.move(9, 2, 1)
    tree.grid(row=0, column=0, sticky=tk.NSEW)