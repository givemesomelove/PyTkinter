import tkinter as tk


# https://baijiahao.baidu.com/s?id=1817286171297205470
# mac端的工具栏显示在顶部

def makeMenuUI(root):
    
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=False)
    file_menu.add_command(label='新建')
    file_menu.add_command(label='打开...')
    sub_menu = tk.Menu(file_menu, tearoff=0)
    sub_menu.add_command(label='关闭当前文件')
    sub_menu.add_command(label='关闭所有文件')
    file_menu.add_cascade(label="关闭文件", menu=sub_menu)
    file_menu.add_separator()
    file_menu.add_command(label='退出', command=root.destroy)
    menubar.add_cascade(label="文件", menu=file_menu)
    menubar.add_cascade(label="编辑")