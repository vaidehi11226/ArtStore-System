from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class Register:
	def __init__(self,window):
		self.window=window
		self.window.title('Registration form')
		self.window.geometry('2000x1500+0+0')
		#self.window.resizable(False,False)
		self.window.configure(bg='black')
		Frame_login1=Frame(self.window,bg='gray82')
		Frame_login1.place(x=400,y=150,height=560,width=800)

		label1=Label(Frame_login1,text="REGISTER HERE",font=('impact',25,'bold'),fg='black',bg='darkorange')
		label1.place(x=270,y=30)


		label2=Label(Frame_login1,text="Name : ",font=("Goudy old style",20,"bold"),fg='black',bg='MediumPurple1')
		label2.place(x=30,y=95)
		self.enname=Entry(Frame_login1,font=('time new roman',15,"bold"),bg='lightgray')
		self.enname.place(x=30,y=145,width=270,height=35)

		label3=Label(Frame_login1,text="Mobile.no: ",font=("Goudy old style",20,"bold"),fg='black',bg='MediumPurple1')
		label3.place(x=30,y=195)
		self.enmobile=Entry(Frame_login1,font=('time new roman',15,"bold"),bg='lightgray')
		self.enmobile.place(x=30,y=245,width=270,height=35)

		label7=Label(Frame_login1,text="State: ",font=("Goudy old style",20,"bold"),fg='black',bg='MediumPurple1')
		label7.place(x=30,y=295)
		self.combostate=ttk.Combobox(Frame_login1,font=("Goudy old style",20,"bold"),state="readonly")
		self.combostate["values"]=("Maharashtra","Gujarat","Rajasthan","Madhya pradesh","Delhi","Goa","kerela","sikkim")
		self.combostate.place(x=30,y=345,width=270,height=35)
		self.combostate.current(0)

		#self.enstate=Entry(Frame_login1,font=('time new roman',15,"bold"),bg='lightgray')
		#self.enstate.place(x=30,y=245,width=270,height=35)


		label4=Label(Frame_login1,text="Email-Id : ",font=("Goudy old style",20,"bold"),fg='black',bg='MediumPurple1')
		label4.place(x=330,y=95)
		self.enmail=Entry(Frame_login1,font=('time new roman',15,"bold"),bg='lightgray')
		self.enmail.place(x=330,y=145,width=270,height=35)

		label5=Label(Frame_login1,text="Address : ",font=("Goudy old style",20,"bold"),fg='black',bg='MediumPurple1')
		label5.place(x=330,y=195)
		self.enaddress=Entry(Frame_login1,font=('time new roman',15,"bold"),bg='lightgray')
		self.enaddress.place(x=330,y=245,width=270,height=35)

		label6=Label(Frame_login1,text="Password :",font=("Goudy old style",20,"bold"),fg='black',bg='MediumPurple1')
		label6.place(x=330,y=295)
		self.enpass=Entry(Frame_login1,show="*",font=('time new roman',15,"bold"),bg='lightgray')
		self.enpass.place(x=330,y=345,width=270,height=35)

		#state checkbox

		

		btnre=Button(Frame_login1,command=self.register,text='Register',cursor='hand2',font=('calibri',15),fg='black',bg='darkorange',bd=0,width=25,height=1)
		btnre.place(x=90,y=450)

		btnlo=Button(Frame_login1,text='ALready Registered?Login',command=self.login_window,cursor='hand2',font=('calibri',15),fg='black',bg='darkorange',bd=0,width=25,height=1)
		btnlo.place(x=360,y=450)

	def login_window(self):
		self.window.destroy()
		import login1

	def clear(self):
		self.enname.delete(0,END)	
		self.enmobile.delete(0,END)
		self.enmail.delete(0,END)
		self.enaddress.delete(0,END)
		self.enpass.delete(0,END)
		self.combostate.current(0)

	def register(self):
		if self.enname.get()=="" or self.enmobile=="" or self.enmail=="" or self.combostate=="" or self.enaddress=="" or self.enpass=="":
			messagebox.showerror("Error","All fields are required",parent=self.window)
		else:
			try:
				con=mysql.connector.connect(
		    	host="localhost",
				user="root",
				password="",
				database="mainartstore"
				)
				cur=con.cursor()
				
				cur.execute('insert into register(Name,Mobile_no,emailid,state,address,password)values(%s,%s,%s,%s,%s,%s)',(self.enname.get(),self.enmobile.get(),self.enmail.get(),self.combostate.get(),self.enaddress.get(),self.enpass.get()))
				con.commit()
				#con.close()
				messagebox.showinfo("Success","Register Successfull!!",parent=self.window)
				self.clear()
				self.window.destroy()
				import login1
				#self.window.destroy()
				#import artstore
			except Exception as es:
				messagebox.showerror("Error",f'Error Due to: {str(es)}',parent=self.window)
			
window=Tk()
obj=Register(window)
window.mainloop()