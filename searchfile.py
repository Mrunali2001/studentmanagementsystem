import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#import sys
import mysql.connector
from mysql.connector import Error
import sys
def con():
    try:
        mydb=mysql.connector.connect(host="localhost",port=3306,user="root",database="mydb011",passwd="")
    except Error as e:
        print("error occured in database",e)
    return mydb        


class searched:
    def  __init__(self):
        self.root4=Tk()
        self.root4.title("student managment system")
        self.root4.geometry("1380x800+8+8")
        self.root4.configure(bg="orange")
        self.root4.state('zoomed')

        label1=Label(self.root4,text=" WELCOME TO STUDENT MANAGMENT SYSTEM",font=("oswald",20,"bold"),bg="brown",fg="black",width=50)
        label1.place(x=200,y=100)
        l1=Label(self.root4,text="Enter the name:",font=("oswald",20,"bold"),bg="purple",fg="white")
        l1.place(x=150,y=198)
        self.name=StringVar()
        self.e11=Entry(self.root4,textvariable=self.name,width=20)
        self.e11.config(font=("oswald",20,"bold"))
        self.e11.place(x=400, y=200)
        b1 = Button(self.root4, text="Search", width=15, bg="purple", fg="white", font=("arial",15,"bold"),command=self.editrecord,activebackground="red")
        b1.place(x=750, y=198)
        #b2 = Button(self.root4, text="Exit", width=15, bg="purple", fg="white", font="arial", command=self.root4.destory)
        #b2.place(x=400, 
        self.root4.mainloop()
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
        sql="select * from studented where name=%s"
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
        l2=Label(self.root4,text="Roll No:",bg="red",fg="black")
        l2.config(font=("oswald",12,"bold"))
        l2.place(x=200,y=250)
        l3=Label(self.root4,text="Name:",bg="red",fg="black")
        l3.config(font=("oswald",12,"bold"))
        l3.place(x=200,y=280)
        l4=Label(self.root4,text="Standard:",bg="red",fg="black")
        l4.config(font=("oswald",12,"bold"))
        l4.place(x=200,y=310)
        l5=Label(self.root4,text="Section",bg="red",fg="black")
        l5.config(font=("oswald",12,"bold"))
        l5.place(x=200,y=340)
        l6=Label(self.root4,text="Gender",bg="red",fg="black")
        l6.config(font=("oswald",12,"bold"))
        l6.place(x=200,y=370)
        l7=Label(self.root4,text="Address",bg="red",fg="black")
        l7.config(font=("oswald",12,"bold"))
        l7.place(x=200,y=400)
        self.rollno=StringVar()
        self.name=StringVar()
        self.std=StringVar()
        self.sec=StringVar()
        self.gen=StringVar()
        self.add=StringVar()
        self.e1=Entry(self.root4,width=32,textvariable=self.rollno,bg="white",font=("oswald",12,"bold"))
        self.e1.insert(0,self.a)
        self.e1.place(x=300,y=250)
        self.e2=Entry(self.root4,width=32,textvariable=self.name,bg="white",font=("oswald",12,"bold"))
        self.e2.insert(0,self.b)
        self.e2.place(x=300,y=280)
        self.e3=Entry(self.root4,width=32,textvariable=self.std,bg="white",font=("oswald",12,"bold"))
        self.e3.insert(0,self.c)
        self.e3.place(x=300,y=310)
        self.e4=Entry(self.root4,width=32,bg="white",textvariable=self.sec,font=("oswald",12,"bold"))
        self.e4.insert(0,self.d)
        self.e4.place(x=300,y=340)
        self.e5=Entry(self.root4,width=32,bg="white",textvariable=self.gen,font=("oswald",12,"bold"))
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
        self.e6=Entry(self.root4,width=35,bg="white",textvariable=self.add,font=("oswald",12,"bold"))
        self.e6.insert(0,self.f)
        self.e6.place(x=300,y=400)
        self.b1=Button(self.root4,text="Exit",command=self.root4.destroy,width=15,bg="purple",fg="white",activebackground="white")
        self.b1.config(font=("Oswald",12,"bold"))
        self.b1.place(x=300,y=445)



