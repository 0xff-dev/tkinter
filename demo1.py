from tkinter import *

root = Tk()

def new_label(event):
    global root
    label = Label(root, text="new lable")
    label.pack()

root.wm_title("Gui Demo")
# btn = Button(root, text="Bnt", command=new_label)
btn = Button(root, text="Btn")
btn.width = 20
btn.bind("<Button-1>", new_label)
btn.pack()
root.mainloop()