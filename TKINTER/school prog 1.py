from tkinter import *
import os
win = Tk()
win.geometry('200x200')
win.title(os.getcwd())

    

txt1 = Label(win,text='Enter Text').pack()
ans_txt1 = StringVar()
entry_txt1 = Entry(win,width=30,textvariable=ans_txt1).pack()

def output():
    ans = ans_txt1.get()
    Label(win,text=ans).pack()

btn1 = Button(win,text="SUBMIT",command=output).pack()



win.mainloop()