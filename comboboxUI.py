from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import ttk
from calendar import month_name
from datetime import datetime

# https://baijiahao.baidu.com/s?id=1818826045260408568

def makeCombobox(root):
    label = tk.Label(text="请选择省份：")
    label.pack(fill=tk.X, padx=5, pady=5)
    combobox1 = ttk.Combobox(root)
    combobox1['values'] = ["山东省", "江苏省", "吉林省"]
    combobox1['state'] = 'readonly'
    combobox1.pack(padx=5, pady=5)

    label = tk.Label(text="请选择城市：")
    label.pack(fill=tk.X, padx=5, pady=5)
    combobox2 = ttk.Combobox(root)
    combobox2['state'] = 'readonly'
    combobox2.pack(padx=5, pady=5)

    # 联动响应
    region = {
    '山东省': ["济南", "青岛", "淄博"],
    '江苏省': ["南京", "苏州" ],
    '吉林省': ["长春", "吉林"]
    }
    def handle(event):
        selected = combobox1.get()
        combobox2['values'] = region[selected]

    combobox1.bind('<<ComboboxSelected>>', handle) 