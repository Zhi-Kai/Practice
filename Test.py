#<<<<<<< HEAD
# from tkinter import *

# form = Tk()

# form.title("Tkinter.TK Demo")
# form.geometry("300x200+10+10")

# form.minsize(300, 200)
# form.maxsize(600, 400)

# form.attributes("-topmost", 1) 

# form.configure(background='black')

# form.mainloop()

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)




listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()

root.mainloop()                 # 进入消息循环

#=======
import tkinter as tk
win=tk.Tk()
win.mainloop()
#>>>>>>> b9a7513f440c964dae4d8b9c73721516f5204517
