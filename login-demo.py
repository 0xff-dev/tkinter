from tkinter import *

def login_btn(e1: Entry, e2: Entry, tips: Label):
    def login(event):
        account = e1.get()
        pwd = e2.get()
        if account == "111" and pwd == "123":
            tips['text'] = "登录成功"
        else:
            tips['text'] = "登陆失败"
    return login

root = Tk()
Label(root, text="账号").grid(row=0, sticky=W)
e1 = Entry(root)
e1.grid(row=0, column=1, sticky=E)

Label(root, text="密码").grid(row=1, sticky=W)
e2 = Entry(root, show='*')
e2.grid(row=1, column=1, sticky=E)

tips = Label(root, text="")
tips.grid(row=2, sticky=W)

btn = Button(root, text="登陆")
btn.bind("<Button-1>", login_btn(e1, e2, tips))
btn.grid(row=2, column=1, sticky=E)
root.mainloop()
