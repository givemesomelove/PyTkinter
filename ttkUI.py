import tkinter as tk
from tkinter import ttk

# https://baijiahao.baidu.com/s?id=1818669209035040918

def makeTtk(root):
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 16))
    style.map('TButton', foreground=[('pressed', 'blue'), ('active', 'red')])

    button = ttk.Button(root, text='按钮')
    button.pack(pady=20)
    button = ttk.Button(root, text='按钮')
    button.pack(pady=20)