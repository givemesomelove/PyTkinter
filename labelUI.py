import tkinter as tk

# https://baijiahao.baidu.com/s?id=1811129652634555427

def makeLabl(root):
    lab = tk.Label(
        root, 
        text='这是一个标签',
        foreground='red',
        bg='black'
        )
    lab.pack(ipadx=100, ipady=100)