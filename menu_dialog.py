from tkinter import *
from tkinter.filedialog import *


class MainWindow(object):
    def __init__(self):
        self.func_types = {
            'open_file': self._open_file,
            'new_file': self._new_file,
            'save_file': self._save_as
        }
        self.label_func = {
            '新建 ctrl+shift+n': self._new_file,
            '打开 ctrl+shift+o': self._open_file,
            '保存 ctrl+shit+s': self._save_as,
        }
        self.window = Tk(className='文件的使用')
        self.window.bind('<Control-O>', self._global_bind_open_file())
        self.window.bind(
            '<Control-N>', self._global_bind_open_file('new_file'))
        self.window.bind(
            '<Control-S>', self._global_bind_open_file('save_file'))
        self._menu()
        self.file_name = ""
        self.text = None

    def _menu(self):
        """生成默认的菜单, 使用弹出式菜单，直接使用menu.post(x, y)即可"""
        menubar = Menu(self.window)
        file_menu = Menu(menubar)
        for key, val in self.label_func.items():
            file_menu.add_command(label=key, command=val)
        menubar.add_cascade(label='文件', menu=file_menu)
        self.window['menu'] = menubar

    def _global_bind_open_file(self, ftype="open_file"):
        """全局快捷键绑定"""
        def bind(event):
            self.func_types[ftype]()
        return bind

    def _open_file(self):
        """打开文件"""
        self._new_file()
        self.file_name = askopenfilename(filetypes=[('all files', '.go')])
        fp = open(self.file_name, 'r')
        for line in fp.readlines():
            self.text.insert(END, line)
        fp.close()

    def _save_as(self):
        """存储文件"""
        data = self.text.get(0.0, END)
        if self.file_name != "":
            with open(self.file_name, 'w') as fp:
                fp.write(data)
        else:
            save_file = asksaveasfile()
            save_file.write(data)
        self.text.destroy()

    def _new_file(self):
        """新建文件"""
        if self.text is not None:
            self.text.destroy()
        self.text = Text(self.window)
        self.text.grid(row=0, sticky='E')

    def loop(self):
        self.window.mainloop()


if __name__ == '__main__':
    w = MainWindow()
    w.loop()
