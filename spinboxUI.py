import tkinter as tk

# https://baijiahao.baidu.com/s?id=1815112635917214562

def makeSpinbox(root):
    current_value = tk.StringVar(value=0)
    spinbox = tk.Spinbox(
        root,
        from_=0,
        to=10,
        textvariable=current_value,
        wrap=True
    )
    spinbox.pack()