import tkinter as tk
from tkinter import ttk

def makeProgressbar(root):
        root.grid_anchor('center')
        def startall():
            pb1.start(5)
            pb2.start(10)
            pb3.start(5)
            pb4.start(10)
            
        def stepall():
            pb1.step(10)
            pb2.step(8)
            pb3.step(25)
            pb4.step(15)

        def stopall():
            pb1.stop()
            pb2.stop()
            pb3.stop()
            pb4.stop()
        pb1 = ttk.Progressbar(root, orient='horizontal', length=280)
        pb1.grid(row=0,column=0,pady=10,padx=10)
        pb2 = ttk.Progressbar(root, orient='horizontal',  mode='indeterminate', length=280)
        pb2.grid(row=1,column=0,pady=10,padx=10)
        pb3 = ttk.Progressbar(root, orient='vertical', length=280)
        pb3.grid(row=0,column=1,pady=10,padx=10,rowspan=2)
        pb4 = ttk.Progressbar(root, orient='vertical',  mode='indeterminate', length=280)
        pb4.grid(row=0,column=2,pady=10,padx=10,rowspan=2)
        start_button = ttk.Button(root, text='开始', command=startall)
        start_button.grid(row=2,column=0,pady=10,padx=10)
        start_button = ttk.Button(root, text='步进', command=stepall)
        start_button.grid(row=2,column=1,pady=10,padx=10)
        start_button = ttk.Button(root, text='停止', command=stopall)
        start_button.grid(row=2,column=2,pady=10,padx=10)