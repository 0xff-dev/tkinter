from tkinter import *
from tkinter.dialog import *
from tkinter.filedialog import *

def open_dialog():
    d = Dialog(None, title='测试dialog', text='6666',
            bitmap=DIALOG_ICON, default=0, strings=('5', '6', '7'))
    # index
    print(d)

t = Button(None, text='打开dialog', command=open_dialog)
t.pack()
t.mainloop()
