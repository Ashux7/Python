import os
from tkinter import *
from PIL import Image,ImageTk
root = Tk()
cwd = os.getcwd()

root.geometry("734x434")
root.title(cwd)

heading = Label(text="Welcome to Achuu's GUI!!!",bg="Blue",padx="10",pady="10",fg="red",relief=RIDGE,font='ALGERIAN 20 bold',borderwidth=30)
heading.pack()


image = PhotoImage(file="itachi.png")
image_label = Label(image=image)
image_label.pack()

root.mainloop()