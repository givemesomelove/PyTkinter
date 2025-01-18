import tkinter as tk

# https://baijiahao.baidu.com/s?id=1817918758260754377

def makePlace(root):
    button1 = tk.Button(root, text="x=100, y=100", width=20, height=5, bg='red')
    button1.place(x=100, y=100)

    button2 = tk.Button(root, text="x=100, y=100", width=20, height=5, bg='green')
    button2.place(x=100, y=100, anchor=tk.CENTER)

    button3 = tk.Button(root, text="relx=0.5, rely=0.5", width=20, bg='red')
    button3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button4 = tk.Button(root, text="relx=0.5, rely=0.5", width=20, bg='green')
    button4.place(relx=0.5, rely=0.5)