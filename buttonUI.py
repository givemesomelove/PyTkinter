import tkinter as tk

def makeButton(root):
    button = tk.Button(
    root, 
    text="Click Me", 
    # command=None,
    activebackground="blue", # 按钮按下时的颜色
    activeforeground="white", # 按钮按下时文字颜色
    bd=1, # 按钮边框宽度
    bg="lightgray", # 按钮背景色
    cursor="hand2", # 鼠标指针样式
    fg="black", # 文字颜色
    font=("Arial", 12), # 文字字体字号
    height=2, # 按钮高度
    justify="center", # 对齐方式
    padx=10, # 文字左右边距
    pady=5, # 文字上下边距
    width=15, # 按钮宽度
    wraplength=100 # 文本换行
    ) 
    button.pack(ipadx=5, ipady=5, expand=True)