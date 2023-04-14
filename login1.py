from tkinter import*
from tkinter import messagebox
import mysql.connector

#import smtplib

class Login:
	def __init__(self,window):
		self.window=window
		self.window.title('Login Form')
		self.window.geometry('2000x1500+0+0')
		#self.window.resizable(False,False)
		self.window.configure(bg='black')
		#___LoginFrame___
		frame1=Frame(self.window,bg='gray82')
		frame1.place(x=420,y=150,width=700,height=500)

		title=Label(frame1,text="LOGIN HERE",font=('times new roman',25,"bold"),bg='darkorange',fg="black").place(x=220,y=30)

		f_user=Label(frame1,text="Username : ",font=('times new roman',20,"bold"),bg='MediumPurple1',fg="black").place(x=150,y=180)
		self.txt_user=Entry(frame1,font=("times new roman",20),bg='lightgray')
		self.txt_user.place(x=320,y=180,width=250)

		f_pass=Label(frame1,text="Password : ",font=('times new roman',20,"bold"),bg='MediumPurple1',fg="black").place(x=150,y=280)
		self.txt_pass=Entry(frame1,show="*",font=("times new roman",20),bg='lightgray')
		self.txt_pass.place(x=320,y=280,width=250)


		btnfpass=Button(frame1,text="forgot password?",command=self.forgotpassword,cursor='hand2',font=("calibri",10),bg="white",fg="black",bd=0)
		btnfpass.place(x=150,y=340)

		btnflogin=Button(frame1,text="Login",command=self.login,cursor='hand2',font=("new times roman",15),bg="darkorange",fg="black",bd=0,width=15,height=1)
		btnflogin.place(x=150,y=380)

		btnfregister=Button(frame1,text="Not registered?Register",command=self.register_window ,cursor='hand2',font=("calibri",15),bg="darkorange",fg="black",bd=0,width=30,height=1)
		btnfregister.place(x=340,y=380)

	def register_window(self):
		self.window.destroy()
		import register


	def login(self):
		if self.txt_user.get()=="" or self.txt_pass.get()=="":
			messagebox.showerror('Error',"ALl Fields are required",parent=self.window)
		else:
			try:
				con = mysql.connector.connect(
		    	host="localhost",
				user="root",
				password="",
				database="mainartstore"
				)
				cur=con.cursor()
				#cur.execute('select loginform from artstore')
				cur.execute('select * from loginform where username=%s and password=%s',(self.txt_user.get(),self.txt_pass.get()))
				row=cur.fetchone()
				print(row)
				if row==None:
					messagebox.showerror("Error","Invalid Username And Password",parent=self.window)
				else:
					messagebox.showinfo("Success","Login succesfull!!",parent=self.window)
					self.window.destroy()
					import artstore
			except Exception as e:
				messagebox.showerror('Error',f'Error Due to: {str(e)}',parent=self.window)


	def forgotpassword(self):
		#forgotpassword
		frame2=Frame(self.window,bg="gray82")
		frame2.place(x=420,y=150,width=700,height=550)

		title=Label(frame2,text="RESET PASSWORD",font=('times new roman',25,"bold"),bg='darkorange',fg="black").place(x=220,y=30)

		user=Label(frame2,text="Username : ",font=('times new roman',20,"bold"),bg='MediumPurple1',fg="black").place(x=95,y=180)
		self.en_user=Entry(frame2,font=("times new roman",20),bg='lightgray')
		self.en_user.place(x=350,y=180,width=250)

		newpass=Label(frame2,text="New Password : ",font=('times new roman',20,"bold"),bg='MediumPurple1',fg="black").place(x=95,y=280)
		self.newpassen=Entry(frame2,show="*",font=("times new roman",20),bg='lightgray')
		self.newpassen.place(x=350,y=280)

		confirmpass=Label(frame2,text="Confirm Password : ",font=('times new roman',20,"bold"),bg='MediumPurple1',fg="black").place(x=95,y=380)
		self.conpassen=Entry(frame2,show="*",font=("times new roman",20),bg='lightgray')
		self.conpassen.place(x=350,y=380)

		btnnewpass=Button(frame2,text="Confirm",command=self.checkpass,cursor='hand2',font=("new times roman",15),bg="darkorange",fg="black",bd=0,width=15,height=1)
		btnnewpass.place(x=260,y=480)
		#btnback=Button(frame2,text="Back",command=self.login,cursor='hand2',font=("new times roman",15),bg="darkorange",fg="black",bd=1,width=30,height=1)
		#btnback.place(x=500,y=580)

		#btnfback=Button(frame2,text="Cancel",cursor='hand2',font=("new times roman",15),bg="darkorange",fg="black",bd=0,width=15,height=1)
		#btnfback.place(x=340,y=380)

	def checkpass(self):
		if self.en_user.get()=="" or self.newpassen.get()=="" or self.conpassen.get()=="":
			messagebox.showerror("Error","All fields are required")
		elif self.newpassen.get()!=self.conpassen.get():
			messagebox.showerror("Error","newpassword and confirm password must be same")
		else:
			try:
				con = mysql.connector.connect(
		    	host="localhost",
				user="root",
				password="",
				database="artstore"
				)
				cur=con.cursor()
				cur.execute("select * from loginform where username=%s",(self.en_user.get()))
				row=cur.fetchone()
				#print(row)
				if row==None:
					messagebox.showerror("Error","Enter valid username",parent=self.window)
				else:
					cur.execute("update loginform set password=%s where username=%s",(self.conpassen.get(),self.en_user.get()))
					row2=cur.fetchone()
					con.commit()
					con.close()
					messagebox.showinfo("Success","Your password has been reset successfully,Please login with new password",parent=self.window)

			except Exception as e:
				messagebox.showerror('Error',f'Error Due to: {str(e)}',parent=self.window)	


window=Tk()
obj=Login(window)
window.mainloop()