from tkinter import *
import sys
from studentrec import rec
from viewfile import viewdata 
from searchfile import searched
from  editfile import edited
from deleteform import deleted
from PIL import ImageTk

def exit():
      sys.exit()
def insert():
       obj=rec()
def view():
       obj=viewdata()
def  search():
       obj=searched()
def edit():
       obj=edited()
def delete():
        obj=deleted()

class stdmgt:
   def __init__(self):
       self.root1=Tk()
       self.root1.title("Student Management System")
       self.root1.geometry("1380x800")
       self.root1.configure(bg="#F96666")
       self.root1.state('zoomed')

       l1=Label(self.root1,text="STUDENT MANAGEMENT SYSTEM",bg="#632626",fg="red",font=("oswald",20,"bold"),width=50)
       l1.place(x=0,y=0,relwidth=1)
       #backgroundImage=ImageTk.PhotoImage(file='i.jpg')
	#bglabel=Label(self.root1,image=backgroundImage)
	#bglabel.place(x=300,y=60)
       b1=Button(self.root1,text="Add Record",width=38,bg="black",fg="white",font=("oswald",12,"bold"),command=insert,activebackground="blue")
       b1.place(x=400,y=200)
       b2=Button(self.root1,text="View all Records",width=38,bg="black",fg="white",font=("oswald",12,"bold"),command=view,activebackground="blue")
       b2.place(x=400,y=250)
       b3=Button(self.root1, text="Edit Record", width=38, bg="black", fg="white", font=("oswald",12,"bold"),command=edit,activebackground="blue")
       b3.place(x=400, y=300)
       b4=Button(self.root1,text="Delete Record",width=38,bg="black",fg="white",font=("oswald",12,"bold"),command=delete,activebackground="blue")
       b4.place(x=400,y=350)
       b5=Button(self.root1,text="Search Record",width=38,bg="black",fg="white",font=("oswald",12,"bold"),command=search,activebackground="blue")
       b5.place(x=400,y=400)
       b6=Button(self.root1,text="Exit",width=38,bg="black",fg="white",font=("oswald",12,"bold"),command=exit,activebackground="orange")
       b6.place(x=400,y=450)
       self.root1.mainloop()