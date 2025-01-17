import tkinter as tk

# https://baijiahao.baidu.com/s?id=1815565427284804231

def makeCanvasUI(root):
    canvas = tk.Canvas(
        root, 
        width=550, 
        height= 350, 
        bg='white', 
        relief='sunken',
        bd=4
        )
    canvas.create_oval(10, 100, 90, 180, outline='black', fill='red', width = 2)
    canvas.pack(anchor=tk.CENTER, expand=True)
