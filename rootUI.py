
import tkinter as tk
import tkinter.messagebox as msgbox

# https://baijiahao.baidu.com/s?id=1810983572402992515


def makeRoot():
    def on_closing():
        if msgbox.askokcancel("提示", "你确定要关闭窗口吗？"):
            root.destroy()
    
    root = tk.Tk()
    root.title("tkinter 教程")
    root.geometry('500x500+0+0')
    # root.resizable(False, False)
    # root.overrideredirect(True)
    root.attributes('-topmost', 1) #一直置顶
    # root.attributes('-fullscreen', 1) #全屏

    # WM_DELETE_ WINDOW 关闭窗口
    # WM_TAKE_FOCUS 获取焦点触发
    # WM_SAVE_YOURSELF 保存状态
    # WM_LOSE_FOCUS 失去焦点
    # root.protocol("WM_DELETE_WINDOW", on_closing)
    return root
