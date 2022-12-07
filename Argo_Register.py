# Argo New User Registration Interface
# Minor Project: 3rd Year AIML CSE Batch: B5 Non-Hons. 
# Project Made By: Bhavy Kharbanda (500082531), Anuj Singh (500082307), Dhruv Gupta (500083965)

# importing libraries
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import pymysql

# Class definition for New user registration
class User_Register:
    # Defining the constructor
    def __init__(self, root):
        self.root = root
        self.root.title("ARGO : Registration Window")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="#f15138")  # Background default color

        # For background image and its placement
        self.bg = ImageTk.PhotoImage(file="Assets\\register_bg.jpg")
        bg = Label(self.root, image=self.bg)
        bg.place(x=250, y=0, relwidth=1, relheight=1)

        # For left side image and its placement
        self.bg2 = ImageTk.PhotoImage(file="Assets\\register_fg.png")
        bg2 = Label(self.root, image=self.bg2)
        bg2.place(x=80, y=100, width=400, height=500)

        # Registration form frame
        register_frame = Frame(self.root, bg="white")
        register_frame.place(x=480, y=100, width=700, height=500)

        # For register heading
        title1 = Label(register_frame, text="REGISTER HERE", font=("Rockwell Extra Bold", 20, "bold"), bg="white")
        title1.place(x=200, y=20)

        # ======================== For Row 1
        # For creating the form: first name
        fname = Label(register_frame, text="First Name", font=("times new roman", 15), bg="white", fg="black")
        fname.place(x=50, y=100)

        self.txt_fname = Entry(register_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_fname.place(x=50, y=130, width=250, height = 25)

        # For creating the form: Last name
        lname = Label(register_frame, text="Last Name", font=("times new roman", 15), bg="white", fg="black")
        lname.place(x=370, y=100)

        self.txt_lname = Entry(register_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_lname.place(x=370, y=130, width=250, height = 25)

        # ======================== For Row 2
        # For creating the form: contact
        contact = Label(register_frame, text="Contact", font=("times new roman", 15), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = Entry(register_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_contact.place(x=50, y=200, width=250, height = 25)

        # For creating the form: Email
        email = Label(register_frame, text="Email Id", font=("times new roman", 15), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = Entry(register_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_email.place(x=370, y=200, width=250, height = 25)

        # ======================== For Row 3
        # For creating the form: Security question
        question = Label(register_frame, text="Security Question", font=("times new roman",15), bg="white", fg="black")
        question.place(x=50, y=240)

        self.Sec_quest = ttk.Combobox(register_frame, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.Sec_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Vehicle Number")
        self.Sec_quest.place(x=50, y=270, width=250, height = 25)
        self.Sec_quest.current(0)

        # For creating the form: answer field
        answer = Label(register_frame, text="Answer", font=("times new roman", 15), bg="white", fg="black")
        answer.place(x=370, y=240)

        self.txt_answer = Entry(register_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_answer.place(x=370, y=270, width=250, height = 25)

        # ======================== For Row 4
        # For creating the form: password
        password = Label(register_frame, text="Password", font=("times new roman", 15), bg="white", fg="black")
        password.place(x=50, y=310)

        self.txt_password = Entry(register_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1, show='*')
        self.txt_password.place(x=50, y=340, width=250, height = 25)


        # For creating the form: confirm password
        cnf_password = Label(register_frame, text="Confirm Password", font=("times new roman", 15), bg="white", fg="black")
        cnf_password.place(x=370, y=310)

        self.txt_cnf_password = Entry(register_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1, show='*')
        self.txt_cnf_password.place(x=370, y=340, width=250, height = 25)

        check_pass=IntVar(value=0)
        # Function to hide the password
        def pass_show():
            if(check_pass.get()==1):
                self.txt_password.config(show='')
                self.txt_cnf_password.config(show='')
            else:
                self.txt_password.config(show='*')
                self.txt_cnf_password.config(show='*')


        pass_check1 = Checkbutton(register_frame,text="Show Password",variable=check_pass, onvalue=1, offvalue=0, bg="white", font=("times new roman", 11),command=pass_show)
        pass_check1.place(x=500, y=370)

        # ======================== For Row 5
        # For creating a check point for terms and conditions
        self.var_chk = IntVar()
        self.chk = Checkbutton(register_frame, text="I Agree to the Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", fg="blue", font=("times new roman", 12))
        self.chk.place(x=50, y=390)

        # ======================== For Row 6
        # For creating a submit button
        btn_register = Button(register_frame, text="REGISTER", command = self.reg_data, font=("Vani", 14, "bold"), bg="#f05037", bd=5, cursor="hand2")
        btn_register.place(x=50, y=430, width=250, height=40)

        # for creating login button
        btn_login = Button(self.root, text="SIGN IN", command = self.login_window, font=("Vani", 16, "bold"), bg="#f05037", bd=3, cursor="hand2")
        btn_login.place(x=230, y=530, width=100, height=40)


    def reg_data(self):
        if  self.txt_fname.get() == "" or  self.txt_lname.get()=="" or self.Sec_quest=="Select" or self.txt_contact=="" or self.txt_email=="" or self.txt_answer=="" or self.txt_password=="" or self.txt_cnf_password=="":
            messagebox.showerror("Error", "All fields are rquired !!!!!!", parent = self.root)
        elif self.txt_password.get() != self.txt_cnf_password.get():
            messagebox.showerror("Error", "Confirm password should be same as Password", parent = self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Accept the Terms and Conditions to Register", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password = "", database="argo_main" )
                cur = con.cursor()
                cur.execute("Select * from registration_details where email_id = %s", self.txt_email.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "User Already exists, Try with another email id", parent=self.root)
                else:
                    cur.execute("insert into registration_details (fname, lname, contact, email_id, question, answer, password) values (%s,%s,%s,%s,%s,%s,%s)", 
                                    (
                                        self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.Sec_quest.get(),
                                        self.txt_answer.get(),
                                        self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful, Welcome to ARGO", parent = self.root)
                    self.clear()
                    self.root.destroy()                    
                    import Argo_Login
                    
            except Exception as exc2:
                messagebox.showerror("Error", f"Error due to: {str(exc2)}", parent = self.root)

            

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.Sec_quest.current(0)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cnf_password.delete(0, END)
        self.var_chk.set(0)



    # Function to call the Login Page
    def login_window(self):
        self.root.destroy()
        import Argo_Login



root = Tk()
obj = User_Register(root)
root.iconbitmap("Assets\\argo_icon.ico")
root.mainloop()  # Closing mainloop
