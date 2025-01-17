import tkinter as tk
from tkinter.messagebox import *
from tkinter import filedialog as fd
from tkinter.colorchooser import askcolor


# https://baijiahao.baidu.com/s?id=1816470520806985445

def show_error():
    showerror(title='错误', message='这是一个错误信息窗口')
def show_info():
    showinfo(title='提示', message='这是一个提示信息窗口')
def show_warning():
    showwarning(title='警告', message='这是一个警告信息窗口')
# def confirm_destroy():
#     answer = askyesno(title='Yes/No', message='你确定要退出？')
#     if answer:
#         root.destroy()
def confirm_delete():
    answer = askokcancel(title='Ok/Cancel', message='删除所有数据？')
    if answer:
        showinfo(title='提示', message='所有数据删除成功')
def confirm_retry():
    answer = askretrycancel(title='Retry/Cancel', message='数据发送不成功，尝试重新发送？')
    if answer:
        showinfo(title='提示', message='尝试再次发送数据')
def select_file():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='打开文件', initialdir='/', filetypes=filetypes)
    showinfo(
        title='选择文件', message=filename)
# def change_color():
#     colors = askcolor(title="选择颜色")
#     root.configure(bg=colors[1])