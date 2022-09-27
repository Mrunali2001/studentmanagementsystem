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


class deleted:
    def  __init__(self):
         self.root5=Tk()
         self.root5.title("student management system")
         self.root5.geometry("1380x800+8+8")
         self.root5.configure(bg="#D49A89")
         self.root5.state('zoomed')

         label1=Label(self.root5,text="WELCOME TO STUDENT MANAGEMENT SYSTEM",bg="#30475E",fg="black",font=("oswald",20,"bold"),width=50)
         label1.place(x=0,y=0,relwidth=1)
         l1=Label(self.root5,text="RollNo:",bg="#164A58",fg="white",font=("oswald",18,"bold"))
         l1.place(x=200,y=160)
         #e1=Entry(self.root3,width=50,bg="white")
         #e1.place(x=290,y=160)
         self.rollno=StringVar()

         self.e11=Entry(self.root5,textvariable=self.rollno,width=20)
         self.e11.config(font=("oswald",20,"bold"))
         self.e11.place(x=300,y=160)
         self.b1=Button(self.root5,bg="#164A58",width=15,fg="white",text="Search",command=self.editrecord)
         self.b1.config(font=("oswald",15,"bold"))
         self.b1.place(x=650,y=160)

         #b1=Button(self.root3,text="Click To View",width=30,bg="purple",fg="white",font="arial")
         #b1.place(x=200,y=300)
         #b2=Button(self.root3,text="Exit",width=25,bg="purple",fg="white",font="arial",command=self.root3.destory)
         #b2.place(x=400,y=300)
         self.root5.mainloop()
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
        mydb.commit()
        mydb.close()    
        l2=Label(self.root5,text="Roll No:",bg="red",fg="black")
        l2.config(font=("oswald",12,"bold"))
        l2.place(x=200,y=250)
        l3=Label(self.root5,text="Name:",bg="red",fg="black")
        l3.config(font=("oswald",12,"bold"))
        l3.place(x=200,y=280)
        l4=Label(self.root5,text="Standard:",bg="red",fg="black")
        l4.config(font=("oswald",12,"bold"))
        l4.place(x=200,y=310)
        l5=Label(self.root5,text="Section",bg="red",fg="black")
        l5.config(font=("oswald",12,"bold"))
        l5.place(x=200,y=340)
        l6=Label(self.root5,text="Gender",bg="red",fg="black")
        l6.config(font=("oswald",12,"bold"))
        l6.place(x=200,y=370)
        l7=Label(self.root5,text="Address",bg="red",fg="black")
        l7.config(font=("oswald",12,"bold"))
        l7.place(x=200,y=400)
        self.rollno=StringVar()
        self.name=StringVar()
        self.std=StringVar()
        self.sec=StringVar()
        self.gen=StringVar()
        self.add=StringVar()
        self.e1=Entry(self.root5,width=32,textvariable=self.rollno,bg="white",font=("oswald",12,"bold"))
        self.e1.insert(0,self.a)
        self.e1.place(x=300,y=250)
        self.e2=Entry(self.root5,width=32,textvariable=self.name,bg="white",font=("oswald",12,"bold"))
        self.e2.insert(0,self.b)
        self.e2.place(x=300,y=280)
        self.e3=Entry(self.root5,width=32,textvariable=self.std,bg="white",font=("oswald",12,"bold"))
        self.e3.insert(0,self.c)
        self.e3.place(x=300,y=310)
        self.e4=Entry(self.root5,width=32,bg="white",textvariable=self.sec,font=("oswald",12,"bold"))
        self.e4.insert(0,self.d)
        self.e4.place(x=300,y=340)
        self.e5=Entry(self.root5,width=32,bg="white",textvariable=self.gen,font=("oswald",12,"bold"))
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
        self.e6=Entry(self.root5,width=32,bg="white",textvariable=self.add,font=("oswald",12,"bold"))
        self.e6.insert(0,self.f)
        self.e6.place(x=300,y=400)
        self.b1=Button(self.root5,text="Exit",command=self.root5.destroy,width=15,bg="#F57328",fg="white")
        self.b1.config(font=("oswald",15,"bold"))
        self.b1.place(x=200,y=470)
        self.b2=Button(self.root5,text="Delete",command=self.finaldelete,width=15,bg="#F57328",fg="white")
        self.b2.config(font=("oswald",15,"bold"))
        self.b2.place(x=400,y=470)


        #b2.place(x=400,y=410)
        self.root5.mainloop()
    def finaldelete(self):
        mydb=con()
        cursor=mydb.cursor()
        sql="delete from studented where rollno=%s"
        val=(self.e1.get(),)
        cursor.execute(sql,val)
        messagebox.showinfo("success","record deleted successfully")
        mydb.commit()
        mydb.close()