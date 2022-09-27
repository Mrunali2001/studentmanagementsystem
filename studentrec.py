from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

import sys
def connection():
	try:
		mydb=mysql.connector.connect(host="localhost",port=3306,database="mydb011",user="root",passwd="")
	except Error as e:
		print("error in database",e)
	return mydb

class rec:
    def __init__(self):
        self.root2=Tk()
        self.root2.title("student management system")
        self.root2.geometry("1380x900")
        self.root2.configure(bg="#F6D860")
        self.root2.state('zoomed')

        label1=Label(self.root2,text="STUDENT MANAGEMENT SYSTEM",bg="#95CD41",fg="white",font=("oswald",20,"bold"),width=50)
        label1.place(x=0,y=0,relwidth=1)
        l1=Label(self.root2,text="Roll No:",bg="#FF7F3F",fg="black",font=("oswald",15,"bold"))
        l1.place(x=200,y=148)
        #e1=Entry(self.root2,width=35,bg="white")
        #e1.place(x=310,y=148)
        l2= Label(self.root2, text="Name:", bg="#FF7F3F", fg="black", font=("oswald",15,"bold"))
        l2.place(x=200, y=188)
        #e2=Entry(self.root2, width=35, bg="white")
        #e2.place(x=310, y=188)
        l3= Label(self.root2, text="Standard:", bg="#FF7F3F", fg="black", font=("oswald",15,"bold"))
        l3.place(x=200, y=232)
        #e3 = Entry(self.root2, width=35, bg="white")
        #e3.place(x=310, y=232)
        l4= Label(self.root2, text="Section:", bg="#FF7F3F", fg="black", font=("oswald",15,"bold"))
        l4.place(x=200, y=265)
        #a1=["A","B","C","D","E","F"]
        #cb=ttk.Combobox(self.root2,width=32,values=a1,state="readonly")
        #cb.place(x=310,y=265)
        l5= Label(self.root2, text="gender", bg="#FF7F3F", fg="black", font=("oswald",15,"bold"))
        l5.place(x=200, y=300)
        #var=IntVar()
        #r1=Radiobutton(self.root2,text="male",bg="#FF7F3F",fg="black",font=("oswald",15,"bold"),value=1,variable=var)
        #r1.place(x=300,y=300)
        #r2=Radiobutton(self.root2,text="female",bg="#FF7F3F",fg="black",font=("oswald",15,"bold"),value=2,variable=var)
        #r2.place(x=380,y=300)
        l6= Label(self.root2, text="Address:", bg="#FF7F3F", fg="black", font=("oswald",15,"bold"))
        l6.place(x=200, y=340)
        #e4= Entry(self.root2, width=35, bg="white")
        #e4.place(x=310, y=340)
        #b1=Button(self.root2,text="exit",command=self.root2.destroy,width=15,bg="purple",fg="white",font=("oswald",12,"bold"),activebackground="red")
        #b1.place(x=200,y=420)
        #b2=Button(self.root2,text="Add Record",command=self.insertrec,width=35,bg="purple",fg="white",font=("oswald",12,"bold"),activebackground="red")
        #b2.place(x=400,y=420)
        self.rollno=StringVar()
        self.name=StringVar()
        self.std=StringVar()
        self.sec=StringVar()
        self.gen=StringVar()
        self.add=StringVar()
        self.e1=Entry(self.root2,width=40,textvariable=self.rollno)
        self.e1.place(x=310,y=148)
        self.e2=Entry(self.root2,width=40,textvariable=self.name,bg="white")
        self.e2.place(x=310,y=188)
        self.e3=Entry(self.root2,width=40,textvariable=self.std,bg="white")
        self.e3.place(x=310,y=232)
        #self.e4=Entry(self.root2,width=40,textvariable=self.sec,bg="white")
        #self.e4.place(x=310,y=265)
        a1=['A','B','C','D','E']
        self.cb=ttk.Combobox(self.root2,state="readonly",values=a1,textvariable=self.sec,width=37)
        self.cb.place(x=310,y=273)
        a2=["male","female"]
        self.cb1=ttk.Combobox(self.root2,state="readonly",values=a2,textvariable=self.gen,width=37)
        self.cb1.place(x=310,y=308)
        self.e4=Entry(self.root2,width=40,bg="white",textvariable=self.add)
        self.e4.place(x=310,y=343)
        self.b1=Button(self.root2,text="Exit",command=self.root2.destroy,width=15,bg="purple",fg="white")
        self.b1.config(font=("Oswald",12,"bold"))
        self.b1.place(x=200,y=410)
        self.b2=Button(self.root2,text="Add Record",command=self.insertrec,width=15,bg="purple",fg="white")
        self.b2.config(font=("Oswald",12,"bold"))
        self.b2.place(x=400,y=410)
        self.root2.mainloop()
    def insertrec(self):
        mydb=connection()
        cursor=mydb.cursor()
        sql="insert into studented(rollno,name,standard,section,gender,address)values(%s,%s,%s,%s,%s,%s)"
        val=(self.e1.get(),self.e2.get(),self.e3.get(),self.cb.get(),self.cb1.get(),self.e4.get())
        cursor.execute(sql,val)
        messagebox.showinfo("success","record inserted the successfully")
        mydb.commit()       

