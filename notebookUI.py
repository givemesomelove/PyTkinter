import tkinter as tk
from tkinter import ttk

def makeNotebook(root):
    def tab_selected(event):
        tab_id = notebook.select()
        tab_text = notebook.tab(tab_id, 'text')
        label2['text'] = tab_text
    
    frame = ttk.Frame(root)
    label1 = ttk.Label(frame, text = "当前选项卡：")
    label1.pack(side=tk.LEFT,)
    label2 = ttk.Label(frame, text = "")
    label2.pack()
    frame.pack()

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)

    label3 = ttk.Label(frame1, text = "第一个选项卡区域")
    label3.pack(expand=True)
    label4 = ttk.Label(frame2, text = "第二个选项卡区域")
    label4.pack(expand=True)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    notebook.add(frame1, text='选项卡1')
    notebook.add(frame2, text='选项卡2')
    notebook.bind("<<NotebookTabChanged>>", tab_selected)
    # 默认选择第二个选项卡
    notebook.select(1)