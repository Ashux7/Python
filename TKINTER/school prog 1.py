import pandas as pd
from tkinter import *

win = Tk()
win.geometry('500x500')

s1={'name':'Ashu','class':'XII','sec':'A','gen':'M'}
s2={'name':'Tasmay','class':'XII','sec':'B','gen':'M'}
s3={'name':'Lavish','class':'XII','sec':'B','gen':'M'}
s4={'name':'Hemal','class':'XII','sec':'C','gen':'M'}
s5={'name':'Manish','class':'XII','sec':'C','gen':'M'}

df = pd.DataFrame([s1,s2,s3,s4,s5],index=['Student 1','Student 2','Student 3','Student 4','Student 5'])

for i in df:
    print(df)
    

win.mainloop()
