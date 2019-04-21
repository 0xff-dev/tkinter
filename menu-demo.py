from tkinter import *


def pop(menu: Menu):
    def pop_func(event):
        menu.post(event.x_root, event.y_root)
    return pop_func

root = Tk(className='File Window')

pop_menu = Menu(root)
for item in ['python', 'go', 'c', 'dart']:
    pop_menu.add_command(label=item)
root.bind("<Button-3>", pop(pop_menu))

menu = Menu(root)
f_menu = Menu(menu)
f_cas_menu = Menu(f_menu)
for item in ['新建', '打开']:
    f_cas_menu.add_command(label=item)
f_menu.add_separator()
for item in ['6', '7']:
    f_cas_menu.add_checkbutton(label=item)
f_cas_menu.add_radiobutton(label='8')
f_menu.add_cascade(label='文件', menu=f_cas_menu)

e_menu = Menu(menu)
for item in ['复制', '粘贴', '剪切']:
    e_menu.add_command(label=item)

menu.add_cascade(label='文件', menu=f_menu)
menu.add_cascade(label='编辑', menu=e_menu)
root['menu'] = menu

root.mainloop()