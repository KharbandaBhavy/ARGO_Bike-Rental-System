# Argo Create New Ride Interface
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
class Admin_Create:
    # Defining the constructor
    def __init__(self, root):
        self.root = root
        self.root.title("ARGO : Create your Ride")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="#b93c30")  # Background default color

        # For background image and its placement
        self.bg = ImageTk.PhotoImage(file="Assets\\create_bg.png")
        bg = Label(self.root, image=self.bg)
        bg.place(x=250, y=0, relwidth=1, relheight=1)

        # For left side image and its placement
        self.bg2 = ImageTk.PhotoImage(file="Assets\\create_fg.png")
        bg2 = Label(self.root, image=self.bg2)
        bg2.place(x=80, y=100, width=400, height=500)

        # Registration form frame
        create_frame = Frame(self.root, bg="white")
        create_frame.place(x=480, y=100, width=700, height=500)

        # For register heading
        title1 = Label(create_frame, text="CREATE YOUR RIDE HERE", font=("Rockwell Extra Bold", 20, "bold"), bg="white")
        title1.place(x=150, y=20)

        # ================================================ For Row 1
        # For creating the form: Name
        aname = Label(create_frame, text="Name", font=("times new roman", 15), bg="white", fg="black")
        aname.place(x=50, y=100)

        self.txt_aname = Entry(create_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_aname.place(x=50, y=130, width=250, height = 25)

        # For creating the form: Contact
        acontact = Label(create_frame, text="Contact", font=("times new roman", 15), bg="white", fg="black")
        acontact.place(x=370, y=100)

        self.txt_acontact = Entry(create_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_acontact.place(x=370, y=130, width=250, height = 25)


        # ================================================= For Row 2
        # For creating the form: Email Id
        aemail = Label(create_frame, text="Email Id", font=("times new roman", 15), bg="white", fg="black")
        aemail.place(x=50, y=170)

        self.txt_aemail = Entry(create_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_aemail.place(x=50, y=200, width=250, height = 25)

        # For creating the form: Address
        alocation = Label(create_frame, text="Address", font=("times new roman", 15), bg="white", fg="black")
        alocation.place(x=370, y=170)

        self.txt_alocation = Entry(create_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_alocation.place(x=370, y=200, width=250, height = 25)

        # ================================================= For Row 3
        # For creating the form: Vechile Type
        vec_type_ques = Label(create_frame, text="Vehicle Type", font=("times new roman",15), bg="white", fg="black")
        vec_type_ques.place(x=50, y=240)

        self.vec_type = ttk.Combobox(create_frame, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.vec_type['values'] = ("Select", "Honda Active", "TVS Jupiter", "TVS Ntorq", "Suzuki Access", "Royal Enfield","Splendor", "CB Shine", "Pulsar", "Platina", "Apache")
        self.vec_type.place(x=50, y=270, width=250, height = 25)
        self.vec_type.current(0)


        # For creating the form: Kms Driven
        akm = Label(create_frame, text="Distance Travelled (Km)", font=("times new roman", 15), bg="white", fg="black")
        akm.place(x=370, y=240)

        self.txt_akm = Entry(create_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_akm.place(x=370, y=270, width=250, height = 25)


        # ================================================ For Row 4
        # For creating the form: Drop Locations
        drop_loc_ques = Label(create_frame, text="Drop Locations", font=("times new roman",15), bg="white", fg="black")
        drop_loc_ques.place(x=50, y=310)

        self.drop_loc = ttk.Combobox(create_frame, font=("times new roman", 13), state="readonly", justify=CENTER)
        self.drop_loc['values'] = ("Select", "UPES Bidholi Campus", "UPES Kandoli Campus", "Nanda ki Chowki", "Sudhowala Chowk", "Forest Research Institute (FRI)", "Indian Military Academy", "Premnagar", "Paltan Bazaar", "Ghanta Ghar", "Pacific Mall")
        self.drop_loc.place(x=50, y=340, width=250, height = 25)
        self.drop_loc.current(0)


        # For creating the form: Vehicle Number
        vec_num = Label(create_frame, text="Vehicle Number", font=("times new roman", 15), bg="white", fg="black")
        vec_num.place(x=370, y=310)

        self.txt_vec_num = Entry(create_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_vec_num.place(x=370, y=340, width=250, height = 25)


        # For creating the form: Vehicle Number
        vec_date = Label(create_frame, text="Available Date (YYYY/MM/DD)", font=("times new roman", 13), bg="white", fg="black")
        vec_date.place(x=50, y=380)

        self.txt_vec_date = Entry(create_frame, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_vec_date.place(x=50, y=410, width=250, height = 25)

    

        # ======================== For Row 5
        # For creating a check point for terms and conditions
        self.var_chk = IntVar()
        self.chk = Checkbutton(create_frame, text="I Agree to the Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", fg="blue", font=("times new roman", 12))
        self.chk.place(x=365, y=420)

        # ======================== For Row 6
        # For creating a submit button
        btn_register = Button(create_frame, text="Create Ride", command = self.reg_data, font=("Vani", 14, "bold"), bg="#b93c30", fg="white", bd=5, cursor="hand2")
        btn_register.place(x=370, y=450, width=250, height=40)


    def reg_data(self):
        if  self.txt_aname.get() == "" or  self.txt_acontact.get()=="" or self.txt_aemail=="" or self.txt_alocation=="" or self.vec_type=="Select" or self.drop_loc=="Select"  or self.txt_akm=="" or self.txt_vec_num=="" or self.txt_vec_date.get=="":
            messagebox.showerror("Error", "All fields are rquired !!!!!!", parent = self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Accept the Terms and Conditions to Register", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password = "", database="argo_main" )
                cur = con.cursor()
                cur.execute("Select * from inventory_details where aemail = %s", self.txt_aemail.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showinfo("Welcome Back", "We hope you liked it the last time, Thanks for creating another one.", parent=self.root)
                else:
                    cur.execute("insert into inventory_details (aname, acontact, aemail, alocation, vec_type, akm, drop_location, vec_num, vec_date) values (%s,%s,%s,%s,%s,%s,%s,%s, %s)", 
                                    (
                                        self.txt_aname.get(),
                                        self.txt_acontact.get(),
                                        self.txt_aemail.get(),
                                        self.txt_alocation.get(),
                                        self.vec_type.get(),
                                        self.txt_akm.get(),
                                        self.drop_loc.get(),
                                        self.txt_vec_num.get(),
                                        self.txt_vec_date.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ride created Successfully, Thanks for using our service.", parent = self.root)
                    self.clear()
                    self.root.destroy()                    
                    import Argo_Thanks
                    
            except Exception as exc2:
                messagebox.showerror("Error", f"Error due to: {str(exc2)}", parent = self.root)

    def clear(self):
        self.txt_aname.delete(0, END),
        self.txt_acontact.delete(0, END),
        self.txt_aemail.delete(0, END),
        self.txt_alocation.delete(0, END),
        self.vec_type.current(0),
        self.txt_akm.delete(0, END),
        self.drop_loc.current(0),
        self.txt_vec_num.delete(0, END),
        self.var_chk.set(0)
        self.txt_vec_date.delete(0, END)


    # Function to call the Login Page
    def login_window(self):
        self.root.destroy()
        import Argo_Thanks


root = Tk()
obj = Admin_Create(root)
root.iconbitmap("Assets\\argo_icon.ico")
root.mainloop()  # Closing mainloop
