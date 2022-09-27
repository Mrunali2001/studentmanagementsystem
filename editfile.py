import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import sys
def con():
    try:
        mydb=mysql.connector.connect(host="localhost",port=3306,user="root",database="mydb011",passwd="")
    except Error as e:
        print("error occured in database",e)
    return mydb        
class edited:
    def  __init__(self):
        self.root6=Tk()
        self.root6.title("student managment system")
        self.root6.geometry("1380x900+8+8")
        self.root6.configure(bg="#FFE9A0")
        self.root6.state('zoomed')

        label1=Label(self.root6,text=" WELCOME TO STUDENT MANAGMENT SYSTEM",font=("oswald",20,"bold"),bg="brown",fg="black",width=50)
        label1.place(x=200,y=100)
        l1=Label(self.root6,text="Enter the RollNo:",font=("oswald",18,"bold"),bg="#367E18",fg="black")
        l1.place(x=150,y=198)
        #e1=Entry(self.root6,bg="white",width=30,font=("arial",18,"bold"),fg="black")
        #e1.place(x=380,y=200)
        self.rollno=StringVar()
        self.e11=Entry(self.root6,textvariable=self.rollno,width=20)
        self.e11.config(font=("oswald",15,"bold"))
        self.e11.place(x=358,y=200)
        self.b1=Button(self.root6,bg="#367E18",width=15,fg="white",text="Retrive",command=self.editrecord)
        self.b1.config(font=("oswald",15,"bold"))
        self.b1.place(x=620,y=200)
        #b2=Button(self.root6,bg="purple",width=19,font="arial",fg="white",text="exit",command=self.root6.destroy)
        #b2.place(x=400,y=410)
        self.root6.mainloop()
    def editrecord(self):
        self.a=StringVar()
        self.b=StringVar()
        self.c=StringVar()
        self.c=StringVar()
        self.d=StringVar()
        self.e=StringVar()
        self.f=StringVar()
        mydb=con()
        cursor=mydb.cursor()
        sql="select * from studented where rollno=%s"
        val=[self.e11.get(),]
        cursor.execute(sql,val)
        result=cursor.fetchall()
        for row in result:
            self.a=row[0]
            self.b=row[1]
            self.c=row[2]
            self.d=row[3]
            self.e=row[4]
            self.f=row[5]
        l2=Label(self.root6,text="Roll No:",bg="red",fg="black")
        l2.config(font=("oswald",12,"bold"))
        l2.place(x=200,y=250)
        l3=Label(self.root6,text="Name:",bg="red",fg="black")
        l3.config(font=("oswald",12,"bold"))
        l3.place(x=200,y=280)
        l4=Label(self.root6,text="Standard:",bg="red",fg="black")
        l4.config(font=("oswald",12,"bold"))
        l4.place(x=200,y=310)
        l5=Label(self.root6,text="Section",bg="red",fg="black")
        l5.config(font=("oswald",12,"bold"))
        l5.place(x=200,y=340)
        l6=Label(self.root6,text="Gender",bg="red",fg="black")
        l6.config(font=("oswald",12,"bold"))
        l6.place(x=200,y=370)
        l7=Label(self.root6,text="Address",bg="red",fg="black")
        l7.config(font=("oswald",12,"bold"))
        l7.place(x=200,y=400)
        self.rollno=StringVar()
        self.name=StringVar()
        self.std=StringVar()
        self.sec=StringVar()
        self.gen=StringVar()
        self.add=StringVar()
        self.e1=Entry(self.root6,width=32,textvariable=self.rollno,bg="white",font=("oswald",12,"bold"))
        self.e1.insert(0,self.a)
        self.e1.place(x=300,y=250)
        self.e2=Entry(self.root6,width=32,textvariable=self.name,bg="white",font=("oswald",12,"bold"))
        self.e2.insert(0,self.b)
        self.e2.place(x=300,y=280)
        self.e3=Entry(self.root6,width=32,textvariable=self.std,bg="white",font=("oswald",12,"bold"))
        self.e3.insert(0,self.c)
        self.e3.place(x=300,y=310)
        self.e4=Entry(self.root6,width=32,bg="white",textvariable=self.sec,font=("oswald",12,"bold"))
        self.e4.insert(0,self.d)
        self.e4.place(x=300,y=340)
        self.e5=Entry(self.root6,width=32,bg="white",textvariable=self.gen,font=("oswald",12,"bold"))
        self.e5.insert(0,self.e)
        self.e5.place(x=300,y=370)

		#self.e1=Entry(self.root2,width=40,textvariable=self.sec
		#self.e1.place(x=300,y=200)
		#a1=['A','B','C','D','E']
		#self.cb=ttk.Combobox(self.root2,state="readonly",values=a1,textvariable=self.sec,width=37)
		#self.cb.place(x=300,y=290)
		#a2=["male","female"]
		#self.cb1=ttk.Combobox(self.root2,state="readonly",values=a2,textvariable=self.gen,width=32)
		#self.cb1.place(x=300,y=320)
        self.e6=Entry(self.root6,width=35,bg="white",textvariable=self.add,font=("oswald",12,"bold"))
        self.e6.insert(0,self.f)
        self.e6.place(x=300,y=400)
        self.b1=Button(self.root6,text="Exit",command=self.root6.destroy,width=15,bg="#F57328",fg="white")
        self.b1.config(font=("oswald",12,"bold"))
        self.b1.place(x=200,y=440)
        self.b2=Button(self.root6,text="Update",width=15,bg="#F57328",fg="white",command=self.finalupdate)
        self.b2.config(font=("oswald",12,"bold"))
        self.b2.place(x=400,y=440)
    def finalupdate(self):
        mydb=con()
        cursor=mydb.cursor()
        sql="update studented set rollno=%s,name=%s,standard=%s,section=%s,gender=%s,address=%s where rollno=%s"
        val=(self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get(),self.e5.get(),self.e6.get(),self.e1.get())
        cursor.execute(sql,val)
        messagebox.showinfo("success","succusefully record update")
        mydb.commit()
        mydb.close()
        #b1=Button(self.root6,bg="purple",width=19,font="arial",fg="white",text="Edit")
        #b1.place(x=200,y=350)
        #b2=Button(self.root6,bg="purple",width=19,font="arial",fg="white",text="Exit",command=self.root6.destroy)
        #b2.place(x=400,y=350)
        #self.root6.mainloop()