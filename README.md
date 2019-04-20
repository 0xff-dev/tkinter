# tkinter
python GUI  ✌🏻

## 按钮与事件的绑定
1. 通过`command`绑定
```python
def new_label():
    global root
    label = Label(root, text="lable")
    label.pack()

root = Tk()
btn = Button(paretn, command=func)
bnt.pack()
root.mainloop()
```

2. `bind`完成事件的绑定
> `bind(event_type, event_func)`
> 事件介绍 <Button-1>鼠标左键，<Button-3>鼠标右键, <KeyPress-A>按下A, B 等按键. <Control-C/V> <F1-12>F按键
> `bind`函数可以做全程序级别的绑定`bind_all`, 全局绑定快捷键. `bind_class` 绑定类别。`w.bind_class("Entry", "<Control-V", func)` 所有的输入框具有粘贴功能.
> 解除绑定`unbind`
```python
def new_label(event):
    global root
    label = Label(root, text="lable")
    label.pack()

root = Tk()
btn = Button(root, text="Button1")
btn.bind("<Button-1>", new_lable)
bnt.pack()
root.mainloop()
```