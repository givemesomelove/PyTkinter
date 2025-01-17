import tkinter as tk

# https://baijiahao.baidu.com/s?id=1814929986936396532

def makeListbox(root):
    langs = ['Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift']

    listbox = tk.Listbox(
        root,
        height=6,
        width=20,
        selectmode=tk.EXTENDED
    )
    listbox.pack(expand=True)
    for item in langs:
        listbox.insert(tk.END, item)
        