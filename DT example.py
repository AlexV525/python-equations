import random
import math
from tkinter import*
class Application(Frame):
 globalnumber=1

def square():
    number1=int(e1.get())
    if number1==0:
        lab4=Label(root,text="Please enter a nuw number")
        lab4.grid()
    else:
        number3=number1*number1
        Label(root,text=number3).grid()
        Label(root,text="Did you get the same answer?").grid()
        Button(root,text="Yes",command=commend).grid()
        Button(root,text="No",command=encourage).grid()

def commend():
    word=int(random.randint(0,2))
    worldlist=["Well done!","Congratulations!","Marvelous!"]
    Label(root,text=worldlist[word]).grid()

def encourage():
    word1=int(random.randint(0,2))
    word1list=["Practise make perfect.","Try again.","Sometimes wrong in your calculation?"]
    Label(root,text=word1list[word1]).grid()

root=Tk()
root.title("Calculator")
Label(root,text="Input a number1").grid(row=0)
e1=Entry(root)
e1.grid(row=0,column=1)
b1=Button(root,text="Quit",bg="White",command=root.destroy).grid(row=0,column=4)
b2=Button(root,text="Square",bg="White",command=square).grid(row=3,column=0)
root.mainloop()
