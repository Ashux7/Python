# imports
from tkinter import *
import mysql.connector

# mysql
conn = mysql.connector.connect(host="localhost",username="root",password="8318534234")
print(conn)
cr = conn.cursor()

# tkinter
win = Tk()
win.geometry('500x500')

def use_db():
	selected_db = db.get()
	selected_db = selected_db[2:-3]
	cr.execute(f'use {selected_db}')
	conn.commit()
	print('using db successful!')


dbases=[]
cr.execute('show databases')
for i in cr:
	dbases.append(i)
conn.commit()
print('Databases Available are: ',dbases,sep='\n')

db = StringVar()
db.set("Select a Database")
selectdb = OptionMenu(win,db,*dbases).place(x=190,y=10)
nxt1 = Button(win,text='-->',command=use_db).place(x=327,y=12)

tables = []
cr.execute('show tables')
for i in cr:
	tables.append(i)
conn.commit()
table = StringVar()
table.set('Select a Table')
settable = OptionMenu(win , table , *tables).place(x=190,y=20)
nxt2 = Button(win,text='-->').place(x=190,y=22)

win.mainloop()