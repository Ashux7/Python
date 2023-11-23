# imports
import mysql.connector
from tkinter import *
from playsound import playsound

# mysql
cnntn = mysql.connector.connect(host='localhost',user='root',password='8318534234')
print(cnntn)
crsr = cnntn.cursor()
crsr.execute("show databases")
db=[]
for i in crsr:
    db.append(i)
print(db)
if ('tkinterdatastorage',) not in db:
    crsr.execute('create database tkinterdatastorage')
    crsr.execute("use tkinterdatastorage")
    crsr.execute('create table TkinterForm(USERNAME varchar(50),PASSWORD varchar(50))')
    cnntn.commit()
else:
    crsr.execute("use tkinterdatastorage")
    cnntn.commit()

# window
win = Tk()
win.geometry("400x500")
win.title("Paise Lelo Friends")

# saste functions/commands
def rickroll():
    playsound("D:\\ASHU\\codes\\PYTHON\\GUI\\RickRoll.mp3")
def music():
    playsound("D:\\ASHU\\codes\\PYTHON\\GUI\\Make Me Move.mp3")
    

# buttons
btn1 = Button(win,text="CLICK FOR Rs 500000/- !!!",borderwidth=10,relief=GROOVE,font=('Algerian 10 italic'),command=rickroll)
btn1.pack()
btn2 = Button(win, text="Gaana sunega??",command=music,borderwidth=10,relief=GROOVE,font=('Algerian 10 italic'))
btn2.pack()

# image
img = PhotoImage(file="itachi.png")
img1 = Label(image=img)
img1.pack(fill=X)

# form
username = Label(win,text="Username").place(x=30,y=300)
password = Label(win,text="Password").place(x=30,y=320)
Label(win,text='** Can\'t use [] \' ; {} to create Username or Password. **').place(x=30,y=340)
user_name = StringVar()  #variable to store data entered.
user_pass = StringVar()
user_entry = Entry(win , width=30,textvariable=user_name).place(x=100,y=300)
pass_entry = Entry(win , width=30,textvariable=user_pass,show='*').place(x=100,y=320)

def data_sender():
    name=user_name.get()
    passw=user_pass.get()
    crsr.execute(f"insert into TkinterForm(Username , Password) VALUES('{name}','{passw}')")
    crsr.execute('select * from TkinterForm')
    for i in crsr:
        print(i)
    cnntn.commit()
submit = Button(win,text="SUBMIT",command=data_sender).place(x=150,y=360)


import matplotlib.pyplot as coord

x=[1,2,3]
y=[1,2,3]

coord.plot(x,y)

coord.xlabel('x-axis')
coord.ylabel('y-axis')

coord.title('graph')

coord.show()


win.mainloop()