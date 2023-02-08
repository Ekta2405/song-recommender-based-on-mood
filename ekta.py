from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
root =Tk()
root.geometry("500x300")
def getvals():
    if angryvalue.get()==1:
        messagebox.showinfo("THE RECOMMENDED SONGS ARE:","You don't own me")
    elif sadvalue.get()==1:
        messagebox.showinfo("THE RECOMMENDED SONGS ARE:","No distance left to run")
    elif calmvalue.get()==1:
        messagebox.showinfo("THE RECOMMENDED SONGS ARE:", "Mellomaniac")
    elif happyvalue.get()==1:
        messagebox.showinfo("THE RECOMMENDED SONGS ARE:","Someone like you")
    else:
        messagebox.showinfo("THE RECOMMENDED SONGS ARE:", "Let's go crazy")

    print("excepted")

Label(root,text="SONG RECOMMENDER\n WHAT'S YOUR MOOD",font="arial 10 bold").grid(row=0,column=3)
angry=Label(root,text="1.ANGRY",font="arial 10 bold")
sad=Label(root,text="2.SAD",font="arial 10 bold")
calm=Label(root,text="3.CALM",font="arial 10 bold")
happy=Label(root,text="4.HAPPY",font="arial 10 bold")
excited=Label(root,text="5.EXCITED",font="arial 10 bold")

angry.grid(row=1,column=2)
sad.grid(row=2,column=2)
calm.grid(row=3,column=2)
happy.grid(row=4,column=2)
excited.grid(row=5,column=2)

angryvalue=IntVar()
sadvalue=IntVar()
calmvalue=IntVar()
happyvalue=IntVar()
excitedvalue=IntVar()

angryentry=Checkbutton(root,text="\U0001F620",onvalue=1,offvalue=0,font="arial 20 bold",variable =angryvalue)
sadentry=Checkbutton(root,text="\U0001F614",onvalue=1,offvalue=0,font="arial 20 bold",variable =sadvalue)
calmentry=Checkbutton(root,text="\U0001F607",onvalue=1,offvalue=0,font="arial 20 bold",variable =calmvalue)
happyentry=Checkbutton(root,text="\U0001F606",onvalue=1,offvalue=0,font="arial 20 bold",variable =happyvalue)
excitedentry=Checkbutton(root,text="\U0001F973",onvalue=1,offvalue=0,font="arial 20 bold",variable =excitedvalue)

angryentry.grid(row=1,column=3)
sadentry.grid(row=2,column=3)
calmentry.grid(row=3,column=3)
happyentry.grid(row=4,column=3)
excitedentry.grid(row=5,column=3)

Button(text="submit",command=getvals).grid(row=6,column=3)

root.mainloop()