import tkinter as tk

# https://baijiahao.baidu.com/s?id=1818228093088495748

def makePanedWindow(root):
    pw=tk.PanedWindow(root,orient=tk.VERTICAL,sashrelief='sunken') # 创建纵向窗格
    pw.pack(fill=tk.BOTH,expand=True) 
    top_frame = tk.Frame(pw)
    tk.Label(top_frame, text='顶部Frame').pack() 
    
    pw1=tk.PanedWindow(pw,orient=tk.HORIZONTAL,sashrelief='sunken') # 创建横向窗格
    label = tk.Label(pw1,text='左侧标签',width=15)
    right_frame = tk.Frame(pw1)
    text = tk.Text(right_frame,wrap="none") # 右侧多行文本框
    
    scrollbar_h = tk.Scrollbar(right_frame,orient=tk.HORIZONTAL,command=text.xview) # 创建滚动条
    scrollbar_v = tk.Scrollbar(right_frame,command=text.yview)
    scrollbar_h.pack(side=tk.BOTTOM,fill=tk.X)
    scrollbar_v.pack(side=tk.RIGHT,fill=tk.Y)

    text.pack(side=tk.LEFT,fill=tk.BOTH,expand=True) 
    text.config(xscrollcommand=scrollbar_h.set,yscrollcommand=scrollbar_v.set)
    pw1.add(label)
    pw1.add(right_frame)
    pw.add(top_frame,minsize=80)
    pw.add(pw1) 
