import tkinter as tk
from tkinter.messagebox import showinfo

# https://baijiahao.baidu.com/s?id=1813571156579774860


def makeCheckbox(root):

    def agr_changed():
        pass
        # showinfo(title='是否同意', message=agr.get())

    agr = tk.StringVar()

    box = tk.Checkbutton(
        root,
        text='是否同意',
        command=agr_changed,
        variable=agr,
        onvalue='同意',
        offvalue='不同意',
        indicatoron=0
    )
    box.pack()
