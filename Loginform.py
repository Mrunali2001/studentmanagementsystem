from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import sys
import mysql.connector
from mysql.connector import Error
from project1 import stdmgt
from PIL import ImageTk

def loginvalidate():
   try:
      student=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="",database="student2527")
      cursor=student.cursor()
      sql="select * from mydb where name=%s and email=%s"
      val=[uid.get(),pass1.get()]
      cursor.execute(sql,val)
      results=cursor.fetchall()
      i=0
      for row in results:
         if uid.get()==row[0] and pass1.get()==row[2]:
            i=1
            obj=stdmgt()
         if i==0:
            messagebox.showinfo("Error","Try again!!!username and password are not matched")
   except Error as e:
         print("Error while connecting to database",e)
if __name__=="__main__":
	root=Tk()
	root.title("Student Management System")
	root.geometry("1380x800")
	root.configure(bg="white")
	root.state('zoomed')
	root.topheading=Label(root,text="STUDENT MANAGEMENT SYSTEM",font=("oswald",20,"bold"),bg="#164A58",fg="white",pady=17,justify=CENTER)
	root.topheading.place(x=0,y=0,relwidth=1)
	root.resizable(False,False)
	backgroundImage=ImageTk.PhotoImage(file='sd.jpg')
	bglabel=Label(root,image=backgroundImage)
	bglabel.place(x=0,y=60 ,width=1380,height=800)
	'''framehome=Frame(root,bg="red")
	framehome.pack(fill=BOTH,expand=True)
	image=PhotoImage(file="img.jpg")
	label=ttk.Label(framehome,image=imagehome)
	label.pack(fill=BOTH,expand=True)'''
	#l1.place(x=150,y=100)
	#root.leftFrame=Frame(root,bg="#226D88")
	#root.leftFrame.place(x=0,y=56, width=400,height=745)
	#canv = Canvas(root, width=80, height=80, bg='white')
	#canv.grid(row=2, column=3)
 	#img= ImageTk.PhotoImage(Image.open('C:\\Users\\OCT\\Desktop\\python project intenship\\python project(internship)\\Python1\\i.jpg'))  # PIL solution
	#canv.create_image(20, 20, anchor=NW, image=img)

	#root.leftheaderframetitle=Label(root,text="Login Form",fg="white",font=("oswald",15,"bold"),bg="#226D88")
	#root.leftframeheadertitle.place(x=8,y=40,relwidth=1)
	label1=Label(root,text="Student ID",font=("oswald",20,"bold"),fg="black")
	label1.place(x=460,y=230)
	uid=StringVar()
	pass1=StringVar()
	e1=Entry(root,textvariable=uid,width=35)
	e1.place(x=660,y=235)
	label2=Label(root,text="Password:",font=("oswald",20,"bold"),fg="black")
	label2.place(x=462,y=290)
	e2=Entry(root,textvariable=pass1,width=33)
	e2.place(x=665,y=300)
	b1=Button(root,text="Login",command=loginvalidate,width=18,font=("oswald",16,"bold"),bg="red",fg="black",justify=CENTER,activebackground="#ff853a")
	b1.place(x=500,y=380)
	root.mainloop()


