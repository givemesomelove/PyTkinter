import tkinter as tk
import tkinter as ttk

# https://baijiahao.baidu.com/s?id=1817492597408150295

def makePack(root):
    var1 =tk.IntVar()
    var2 =tk.BooleanVar()
    left_frame = tk.Frame(root,  width=160,  height=400,  bg='grey')
    left_frame.pack(side='left',  fill='both',  padx=10,  pady=5,  expand=True)

    right_frame  =  tk.Frame(root,  width=400,  height=400,  bg='grey')
    right_frame.pack(side='right',  fill='both',  padx=10,  pady=5,  expand=True)

    tk.Label(left_frame,  text="标签").pack(side='top', padx=5, pady=5, ipadx=20)

    photo = tk.PhotoImage()
    tk.Label(left_frame,  image=photo).pack(fill='both',  padx=5,  pady=5)

    tool_bar1  =  tk.Frame(left_frame,  width=70,  height=100,  bg='lightgrey')
    tool_bar1.pack(side='left',  fill='both',  padx=5,  pady=5,  expand=True)
    tk.Button(tool_bar1,  text="按钮", width=10).pack(padx=5,  pady=5)
    tk.Button(tool_bar1,  text="按钮", width=10).pack(padx=5,  pady=5)
    tk.Button(tool_bar1,  text="按钮", width=10).pack(padx=5,  pady=5)
    tk.Button(tool_bar1,  text="按钮", width=10).pack(padx=5,  pady=5)
    tool_bar2 = tk.Frame(left_frame,  width=70,  height=100,  bg='lightgrey')
    tool_bar2.pack(side='right',  fill='both',  padx=5,  pady=5,  expand=True)

    labelframe1 = tk.LabelFrame(tool_bar2, text='复选框', padx=10, pady=5, bg='lightgrey')
    labelframe1.pack()
    tk.Checkbutton(labelframe1, text='选项1', variable=var1,  bg='lightgrey').pack()
    tk.Checkbutton(labelframe1, text='选项2', variable=var2,  bg='lightgrey').pack(anchor=tk.W)

    labelframe2 = tk.LabelFrame(tool_bar2, text='单选框', padx=10, pady=5, bg='lightgrey')
    labelframe2.pack()
    tk.Radiobutton(labelframe2, text='选项1', variable=var2, value=1, bg='lightgrey').pack()
    tk.Radiobutton(labelframe2, text='选项2', variable=var2,  value=2, bg='lightgrey').pack(anchor=tk.W)

    photo2 = tk.PhotoImage()
    label = tk.Label(right_frame,  image=photo2)
    label.pack(fill='both',  padx=5,  pady=5)
    message ='''
    Python 提供了多个图形开发界面的库，几个常用 Python GUI 库如下：

    Tkinter：Tkinter 模块(Tk 接口)是Python 的标准 Tk GUI 工具包的接口.Tk 和 Tkinter 可以在大多数的 Unix平台下使用,同样可以应用在 Windows 和 Macintosh 系统里。Tk8.0 的后续版本可以实现本地窗口风格,并良好地运行在绝大多数平台中。

    wxPython：wxPython 是一款开源软件，是 Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能健全的 GUI 用户界面。

    Jython：Jython 程序可以和 Java 无缝集成。除了一些标准模块，Jython 使用 Java 的模块。Jython 几乎拥有标准的Python 中不依赖于 C 语言的全部模块。比如，Jython 的用户界面将使用 Swing，AWT或者 SWT。Jython 可以被动态或静态地编译成 Java 字节码。
    '''
    text_box = tk.Text(right_frame, height=30, width=45)
    text_box.pack(pady=5)
    text_box.insert('end', message)
    text_box.config(state='disabled')