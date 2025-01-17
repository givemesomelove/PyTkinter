import tkinter as tk
import tkinter as ttk

# https://baijiahao.baidu.com/s?id=1817492597408150295

def makePack(root):
    button1 = ttk.Button(root, text='1', bg='red', fg='white', width=20)
    button2 = ttk.Button(root, text='2', bg='green', fg='white', width=20)
    button3 = ttk.Button(root, text='3', bg='blue', fg='white', width=20)

    button1.pack()
    button2.pack()
    button3.pack()