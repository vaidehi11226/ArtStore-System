from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
import random2
import temp
import os




con = mysql.connector.connect(
		    	host="localhost",
				user="root",
				password="",
				database="mainartstore"
				)
cur=con.cursor()





#topFrame=Frame(window,bg="thistle3")
#topFrame.place(x=15,y=50,width=1500,height=700)

class Main:
	def __init__(self,window):
		self.window=window
		self.window.title("ArtsyWorld")
		self.window.config(bg="thistle3")
		self.window.geometry("2000x2000")

		p3=PhotoImage(file="palletes.png")
		self.window.iconphoto(False,p3)

		brandLabel=Label(window,text="Welcome to ArtsyWorld Artstore",font=("System 30",30,"bold"),bg="darkorange",fg="black")
		brandLabel.place(x=470,y=10)


		frame1=Frame(window,bg='black')
		frame1.place(x=20,y=60,width=590,height=720)

		frame2=Frame(window,bg='black')
		frame2.place(x=640,y=60,width=880,height=300)

		label1=Label(frame2,text='Menu',font=("System 30",20,"bold"),bg="SkyBlue1",fg="black")
		label1.place(x=370,y=20)

		idlable=Label(frame2,text='ProId:',font=('times new roman',15,"bold"),bg="wheat1",fg="black")
		namelable=Label(frame2,text='ProName:',font=('times new roman',15,"bold"),bg="wheat1",fg="black")
		setnolable=Label(frame2,text='Setofno:',font=('times new roman',15,"bold"),bg="wheat1",fg="black")
		brandlable=Label(frame2,text='Brand:',font=('times new roman',15,"bold"),bg="wheat1",fg="black")
		quanlable=Label(frame2,text='Quantity:',font=('times new roman',15,"bold"),bg="wheat1",fg="black")
		pricelable=Label(frame2,text='Price:',font=('times new roman',15,"bold"),bg="wheat1",fg="black")

		#place lbl
		idlable.place(x=10,y=80)
		namelable.place(x=280,y=80)
		setnolable.place(x=600,y=80)
		brandlable.place(x=10,y=140)
		quanlable.place(x=280,y=140)
		pricelable.place(x=600,y=140)

		global prodid
		prodid=StringVar()
		global prodname
		prodname=StringVar()
		global prodbrand
		prodbrand=StringVar()
		global prodset
		prodset=StringVar()
		global prodprice
		prodprice=StringVar()
		global prodqty
		prodqty=StringVar()

		global list1
		list1=[]

		self.identry=Entry(frame2,font=('time new roman',15,"bold"),width=10,bg='lightgray',textvariable=prodid)
		self.nameentry=ttk.Combobox(frame2,font=('times new roman',15,"bold"),width=14,state="readonly",textvariable=prodname)
		self.nameentry["values"]=("ACRYLIC COLOR","GOUACHE COLOR","WATER COLOR","OIL COLOR","PENCIL COLOR","PAINTING KNIVES",'CANVAS BOARD BIG',"CANVAS BOARD SMALL","SOFT PASTEL","EASEL SMALL","EASEL BIG","ACRYLIC BRUSHES","WATERCOLOR BRUSHES","OIL COLOR BRUSHES","OIL PASTEL","300GSM A5SIZE WHITE PAPER","300GSM A4 SIZE WHITE PAPER","300GSM A3 SIZE WHITE PAPER","300GSM A5 SIZE BLACK PAPER","MATTE VARNISH","GLOSS VARNISH")
		self.nameentry.current(0)
		self.setentry=Entry(frame2,font=('time new roman',15,"bold"),width=10,bg='lightgray',textvariable=prodset)
		self.combobrand=ttk.Combobox(frame2,font=('times new roman',15,"bold"),width=14,state="readonly",textvariable=prodbrand)
		self.combobrand["values"]=("CAMEL","MONT MARTE","WINSON & NEWTON","BRUSTRO","PRISMA")
		self.combobrand.current(0)
		self.quanentry=Entry(frame2,font=('time new roman',15,"bold"),width=10,bg='lightgray',textvariable=prodqty)
		self.priceen=Entry(frame2,font=('time new roman',15,"bold"),width=14,bg='lightgray',textvariable=prodprice)

		#entry place
		self.identry.place(x=90,y=80)
		self.nameentry.place(x=400,y=80)
		self.setentry.place(x=700,y=80)
		self.combobrand.place(x=90,y=140)
		self.quanentry.place(x=400,y=140)
		self.priceen.place(x=700,y=140)

		

		#for bill
		global text
		text=Text(window,width=10,height=10,font=("System 30",15,"bold"),bg="DarkOliveGreen3",fg="black")
		text.place(x=640,y=365,width=880,height=420)


		billno=StringVar()
		x=random2.randint(1000,9999)
		billno.set(str(x))

		text.delete(1.0,END)
		text.insert(END,"\t\t\tWelcome to ArtsyWorld Shopping System")
		text.insert(END,f'\n\n\tBill Number :\t\t{billno.get()}')
		text.insert(END,f"\n ========================================================================")
		text.insert(END,f"\n   Proid\t\tName\t\t\tBrand\t\tSet\tQuantity\t   Price")
		text.insert(END,f"\n ========================================================================")
		#text.insert(END)		

		#table
		self.trv= ttk.Treeview(frame1,columns=(1,2,3,4,5,6),show="headings",height='50')
		self.trv.pack(expand=True, fill=tk.BOTH)

		self.trv.column("# 1",anchor=CENTER, stretch=NO, width=80)
		self.trv.heading("#1", text="ProId")
		self.trv.column("# 2",anchor=CENTER, stretch=NO, width=180)
		self.trv.heading("#2", text="Proname")
		self.trv.column("# 3",anchor=CENTER, stretch=NO, width=130)
		self.trv.heading("#3", text="Brand")
		self.trv.column("#4",anchor=CENTER, stretch=NO, width=50)
		self.trv.heading("#4", text="Setofno")
		self.trv.column("#5",anchor=CENTER, stretch=NO, width=50)
		self.trv.heading("#5", text="Prize")
		self.trv.column("#6",anchor=CENTER, stretch=NO, width=100)
		self.trv.heading("#6", text="Stock")
		

		butnadd=Button(frame2,text='Get Product',command=self.addproduct,font=('times new roman',20,"bold"),bg='SkyBlue1')
		butndel=Button(frame2,text='Clear',command=self.clear,font=('times new roman',20,"bold"),bg='SkyBlue1')
		butnbill=Button(frame2,text='Generate Bill',command=self.generatebill,font=('times new roman',20,'bold'),bg='SkyBlue1')
		butnlogout=Button(frame2,text='Logout',command=self.logout,font=('times new roman',10,'bold'),bg='red')
		butnprint=Button(frame2,text='Print',command=self.print,font=('times new roman',20,'bold'),bg='SkyBlue1')
		butnlogout.place(x=20,y=20)

		#place
		butnadd.place(x=120,y=200)
		butndel.place(x=390,y=200)
		butnbill.place(x=570,y=200)
		#butnprint.place(x=740,y=200)
		self.update()

		


	def update(self):
		cur.execute("Select * from artinfo")
		rows=cur.fetchall()
		for i in rows:
			self.trv.insert('','end',values=i)

	def clear(self):
		self.identry.delete(0,END)	
		self.nameentry.current(0)
		self.combobrand.current(0)
		self.setentry.delete(0,END)
		self.quanentry.delete(0,END)
		self.priceen.delete(0,END)


	def addproduct(self):
		if self.identry.get()=="" or self.nameentry.get()=="" or self.setentry.get()=="" or self.combobrand.get()=="" or self.quanentry.get()=="" or self.priceen.get()=="":
				messagebox.showerror('Error',"ALl Fields are required",parent=self.window)
		else:
			try:
				cur.execute('select * from artinfo where proid=%s and proname=%s and brand=%s and setofno=%s ',(self.identry.get(),self.nameentry.get(),self.combobrand.get(),self.setentry.get()))
				row=cur.fetchone()
				print(row)
				if row==None:
					messagebox.showerror("Error","We don't have this product,U can get some another supplies pls check the table",parent=self.window)
				else:
					cur.execute('insert into billgenerate (proid,proname,brand,setofno,price,quantity)values(%s,%s,%s,%s,%s,%s)',
									(self.identry.get(),
									 self.nameentry.get(),
									 self.combobrand.get(),
									 self.setentry.get(),
									 self.priceen.get(),
									 self.quanentry.get()
									))
					con.commit()
					#con.close()
					messagebox.showinfo("Success","Product added successfully to the bill",parent=self.window)
					#n=prodprice.get()
					m=int(prodqty.get())*int(prodprice.get())
					list1.append(m)
					text.insert(END,f'  {prodid.get()}\t\t{prodname.get()}\t\t\t{prodbrand.get()}\t\t{prodset.get()}\t{prodqty.get()}\t  {m}')
					
			except Exception as e:
				messagebox.showerror('Error',f'Error Due to: {str(e)}',parent=self.window)
	def deleteproduct(self):
		if self.identry.get()=="" or self.nameentry.get()=="" or self.setentry.get()=="" or self.combobrand.get()=="" or self.quanentry.get()=="" or self.priceen.get()=="":
				messagebox.showerror('Error',"ALl Fields are required",parent=self.window)
		else:
			try:
				cur.execute('Delete from billgenerate where proid=%s and proname=%s and brand=%s and setofno=%s and price=%s and quantity=%s',(self.identry.get(),self.nameentry.get(),self.combobrand.get(),self.setentry.get(),self.priceen.get(),self.quanentry.get()))
				con.commit()
				#con.close()
				messagebox.showinfo("Success","Product deleted successfully!!",parent=self.window)
				self.clear()
			except Exception as e:
				messagebox.showerror('Error',f'Error Due to: {str(e)}',parent=self.window)
	def logout(self):
		self.window.destroy()
		import login1

	def generatebill(self):
		if self.identry.get()=="" or self.nameentry.get()=="" or self.setentry.get()=="" or self.combobrand.get()=="" or self.quanentry.get()=="" or self.priceen.get()=="":
			messagebox.showerror('Error',"ALl Fields are required",parent=self.window)
		else:
			tex=text.get(10.0,(10.0+float(len(list1))))
			text.insert(END,tex)
			text.insert(END,f"\n ========================================================================")
			text.insert(END,f"\t\t\t\t\tTotal Payment:\t\t{sum(list1)}")
			text.insert(END,f"\n ========================================================================")
	def print(self):
		q=text.get('1.0','end-lc')
		filename=temp.mktemp('.txt')
		open(filename,'w').write(q)
		os.startfile(filename,'Print')

window=Tk()
obj=Main(window)
window.mainloop()