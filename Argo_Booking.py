# Argo Booking interface
# Minor Project: 3rd Year AIML CSE Batch: B5 Non-Hons. 
# Project Made By: Bhavy Kharbanda (500082531), Anuj Singh (500082307), Dhruv Gupta (500083965)

# importing libraries
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

# Class definition for Booking of the APP
class User_Booking:

    # Defining the constructor
    def __init__(self, root):
        self.root = root
        self.root.title("ARGO : Booking")
        self.root.geometry("1520x750+0+0")
        self.root.config(bg="white")  # Background default color

        #=================================== For banner Image
        banner = Image.open("Assets\\booking_banner.jpg")
        banner = banner.resize((1520, 140))
        self.banner_img = ImageTk.PhotoImage(banner)

        #=================================== For Logo Image
        label1 = Label(self.root, image = self.banner_img, bd=2, relief=RIDGE)
        label1.place(x=0, y=0, width=1520, height=140)

        banner2 = Image.open("Assets\\Logo2.png")
        banner2 = banner2.resize((510, 230))
        self.banner2_img = ImageTk.PhotoImage(banner2)
        label2 = Label(self.root, image = self.banner2_img, bd=2, relief=RIDGE)
        label2.place(x=1000, y=180, width=510, height=230)



        #=================================== Declaring variables
        self.var_contact = StringVar()
        self.var_address = StringVar()
        self.var_bookdate = StringVar()
        self.var_pickuploc = StringVar()
        self.var_booktime = StringVar()
        self.var_bookdays = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_vectype = StringVar()
        self.var_vecnum = StringVar()
        

        #=================================== For Title of app

        label2 = Label(self.root, text="ARGO : Affordable Rides on Go", font =("times new roman", 24, "bold"), bg="black", fg="white",bd=2, relief=RIDGE)
        label2.place(x=0, y=140, width=1520, height=40)

        #=================================== For working on the main frame
        # Details Frame
        main_frame = LabelFrame(self.root, bg="white", bd=2, relief = RIDGE, text="Consumer Details", font=("times new roman", 12, "bold"), padx=2, pady=2)
        main_frame.place(x=0, y=180, width=500, height=270)

        #=================================== Consumer Details Frame
        # Contact of the user
        book_contact = Label(main_frame, text="Contact", font=("times new roman", 13), bg="white",padx=3, pady=6)
        book_contact.grid(row=1, column=0, sticky=W)

        self.txt_b_contact = ttk.Entry(main_frame, textvariable=self.var_contact, font=("times new roman", 12), width=29)
        self.txt_b_contact.grid(row=1, column=1, sticky=W)

        # ======================== For creating button
        # For creating a Fetch button
        btn_fetch = Button(main_frame, text="Fetch Data", font=("Vani", 10, "bold"), command = self.Fetch_details, bg="black", fg="white", bd=5, cursor="hand2")
        btn_fetch.place(x=370, y=4, height=25, width=100)
        
        # =======================Address of the User======================
        book_Address = Label(main_frame, text="Address", font=("times new roman", 13), bg="white", padx=3, pady=6)
        book_Address.grid(row=2, column=0, sticky = W)

        self.txt_b_address = ttk.Entry(main_frame, textvariable = self.var_address, font=("times new roman", 12), width=29)
        self.txt_b_address.grid(row=2, column=1)

        # ==========================Date for Booking==========================
        book_date = Label(main_frame, text="Booking Date", font=("times new roman", 13), bg="white", padx=3, pady=6)
        book_date.grid(row=3, column=0, sticky = W)

        self.txt_b_date = ttk.Entry(main_frame, textvariable=self.var_bookdate, font=("times new roman", 12), width=29)
        self.txt_b_date.grid(row=3, column=1)

        # ========================Date for Booking==========================
        book_date = Label(main_frame, text="(YYYY/MM/DD)", font=("times new roman", 10), bg="white")
        book_date.grid(row=4, column=0, sticky = W)



        # ====================================Identity Proof========================
        book_proof = Label(main_frame, text="Identity Proof", font=("times new roman", 13), bg="white", padx=3, pady=6)
        book_proof.grid(row=5, column=0, sticky = W)

        self.b_book_proof = ttk.Combobox(main_frame, textvariable=self.var_idproof, font=("times new roman", 13), state="readonly", justify=CENTER, width = 24)
        self.b_book_proof['values'] = ("Select", "Driving License", "Adhaar Card", "Pan Card", "Voter Id Card")
        self.b_book_proof.grid(row=5, column=1)
        self.b_book_proof.current(0)

        # ===================================Identity Number========================
        book_id_num = Label(main_frame, text="ID Number", font=("times new roman", 13), bg="white", padx=3, pady=6)
        book_id_num.grid(row=6, column=0, sticky = W)

        self.b_id_num = ttk.Entry(main_frame, textvariable=self.var_idnumber, font=("times new roman", 12), width=29)
        self.b_id_num.grid(row=6, column=1)


        # ======================== For creating button========================================================
        # For creating a submit button
        btn_check = Button(main_frame, text="Check Availability", command = self.check_availability, font=("Vani", 14, "bold"), bg="black", fg="white", bd=5, cursor="hand2")
        btn_check.place(x=50, y=200, width=380, height=30)


        #=================================== For working on the main frame
        # Vehicle Details Frame
        form_frame = LabelFrame(self.root, bg="white", bd=2, relief = RIDGE, text="Vehicle Details", font=("times new roman", 12, "bold"), padx=2, pady=2)
        form_frame.place(x=0, y=450, width=500, height=290)

        # For creating the form: Ref Id
        self.var_refid = StringVar()
        vec_ref = Label(form_frame, text="Reference ID", font=("times new roman",13), bg="white", fg="black", padx=3, pady=6)
        vec_ref.grid(row=1, column=0, sticky=W)

        self.txt_refid = ttk.Entry(form_frame, textvariable=self.var_refid, font=("times new roman", 12), width=29, state="readonly")
        self.txt_refid.grid(row=1, column=1)


        # Pickup Locations
        pick_loc = Label(form_frame, text="Pickup Location", font=("times new roman", 13), bg="white", padx=3, pady=6)
        pick_loc.grid(row=2, column=0, sticky = W)

        self.b_pick_loc = ttk.Combobox(form_frame, textvariable = self.var_pickuploc,font=("times new roman", 13), state="readonly", justify=CENTER, width = 24)
        self.b_pick_loc['values'] = ("Select", "UPES Bidholi Campus", "UPES Kandoli Campus", "Nanda ki Chowki", "Sudhowala Chowk", "Forest Research Institute (FRI)", "Indian Military Academy", "Premnagar", "Paltan Bazaar", "Ghanta Ghar", "Pacific Mall")
        self.b_pick_loc.grid(row=2, column=1)
        self.b_pick_loc.current(0)
        
        #============================= For checking Vehicle===================================================
        # For creating the form: Vechile Type
        vec_type = Label(form_frame, text="Select Vehicle Type", font=("times new roman",13), bg="white", fg="black", padx=3, pady=6)
        vec_type.grid(row=3, column=0, sticky=W)

        self.b_vec_type = ttk.Combobox(form_frame, textvariable=self.var_vectype, font=("times new roman", 12), state="readonly", justify=CENTER, width=27)
        self.b_vec_type['values'] = ("Choose", "Honda Activa", "TVS Jupiter", "TVS Ntorq", "Suzuki Access", "Royal Enfield","Splendor", "CB Shine", "Pulsar", "Platina", "Apache")
        self.b_vec_type.grid(row=3, column=1)
        self.b_vec_type.current(0)


        # For creating the form: Vechile Type
        vec_num = Label(form_frame, text="Enter Vehicle No", font=("times new roman",13), bg="white", fg="black", padx=3, pady=6)
        vec_num.grid(row=4, column=0, sticky=W)

        self.b_vec_num = ttk.Entry(form_frame, textvariable=self.var_vecnum, font=("times new roman", 12), width=29)
        self.b_vec_num.grid(row=4, column=1)

                # Number of Hours
        book_hours = Label(form_frame, text="Booking Time", font=("times new roman", 13), bg="white", padx=3, pady=6)
        book_hours.grid(row=5, column=0, sticky = W)

        self.b_book_hours = ttk.Combobox(form_frame, textvariable = self.var_booktime, font=("times new roman", 13), state="readonly", justify=CENTER, width = 24)
        self.b_book_hours['values'] = ("Select", "1 Hour", "2 Hours", "4 Hours", "6 Hours", "8 Hours", "10 Hours", "12 Hours", "More than 12 Hours")
        self.b_book_hours.grid(row=5, column=1)
        self.b_book_hours.current(0)


        # Number of Days
        book_days = Label(form_frame, text="Booking Days", font=("times new roman", 13), bg="white", padx=3, pady=6)
        book_days.grid(row=6, column=0, sticky = W)

        self.b_book_days = ttk.Combobox(form_frame, textvariable=self.var_bookdays, font=("times new roman", 13), state="readonly", justify=CENTER, width = 24)
        self.b_book_days['values'] = ("Select", "1 Day", "2 Days", "3 Days", "4 days", "5 Days", "6 Days", "7 Days")
        self.b_book_days.grid(row=6, column=1)
        self.b_book_days.current(0)


        # For creating a check point for terms and conditions
        self.var_chk = IntVar()
        self.chk = Checkbutton(form_frame, text="I Agree to the Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", fg="blue", font=("times new roman", 12), padx=2, pady=4)
        self.chk.grid(row=7, column=0)


        # ======================== For creating button==========================================================
        # For creating a Bill button
        btn_check = Button(form_frame, text="Generate Bill", command = self.enter_data, font=("Vani", 14, "bold"), bg="black", fg="white", bd=5, cursor="hand2")
        btn_check.place(x=240, y=220, width=240, height=30)


        # For fetching details and printing them
        #=================================== For working on the Details Fetch Frame===============================
        # Details Frame
        details_frame = LabelFrame(self.root, bg="white", bd=2, relief = RIDGE, text="Previous Details", font=("times new roman", 12, "bold"), padx=2, pady=2)
        details_frame.place(x=500, y=180, width=500, height=230)


        #=================================== For working on the Vehicle availability frame=======================
        # Vehicle Availability Frame
        vec_frame = LabelFrame(self.root, bg="white", bd=2, relief = RIDGE, text="Available Vehicles", font=("times new roman", 12, "bold"), padx=2, pady=2)
        vec_frame.place(x=500, y=410, width=1010, height=330)

        # Search label
        search_label = Label(vec_frame, bg="black", fg="white", bd=2, relief = RIDGE, text="Search Vehicle By", font=("times new roman", 12, "bold"))
        search_label.grid(row = 0, column = 0, sticky = W, padx=1)

        # Search options combo box
        self.search_var = StringVar()
        self.search_vec = ttk.Combobox(vec_frame, textvariable = self.search_var, font=("times new roman", 12), state="readonly", justify=CENTER)
        self.search_vec["values"] = ("Choose", "drop_location", "vec_type", "vec_date")
        self.search_vec.grid(row = 0, column = 1, sticky = W, padx=1)
        self.search_vec.current(0)

        # Take Entry
        self.text_search = StringVar()
        self.txt_search = Entry(vec_frame, textvariable=self.text_search, font=("times new roman", 12), width=29, bg="lightgrey")
        self.txt_search.grid(row = 0, column = 2, sticky = W, padx=1)

        # ======================== For creating button==================================================
        # For creating a Search button
        btn_search = Button(vec_frame, text="SEARCH", command = self.search_func, font=("Vani", 10, "bold"), bg="black", fg="white", bd=3, cursor="hand2", width=16)
        btn_search.grid(row=0, column=3, sticky = W, padx=1)


        # For creating a Search button
        btn_showall = Button(vec_frame, text="SHOW ALL", command = self.show_details, font=("Vani", 10, "bold"), bg="black", fg="white", bd=3, cursor="hand2", width=16)
        btn_showall.grid(row=0, column=4, sticky = W, padx=1)



        #==============================Showing Data of Available vehicles============================================#

        details_table = Frame(vec_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=30, width=1000, height=270)


        # For setting up a scroll bar
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.vec_details_table = ttk.Treeview(details_table, column=("a_id","aname", "acontact", "aemail", "alocation", "vec_type", "akm", "drop_location", "vec_num","vec_date"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command = self.vec_details_table.xview)
        scroll_y.config(command = self.vec_details_table.yview)

        #==================== For showing headings of table=========================   
        self.vec_details_table.heading("a_id", text="Ref Id")     
        self.vec_details_table.heading("aname", text="Owner Name")
        self.vec_details_table.heading("acontact", text="Contact No.")
        self.vec_details_table.heading("aemail", text="Owner Email")
        self.vec_details_table.heading("alocation", text="Address")
        self.vec_details_table.heading("vec_type", text="Vehicle Type")
        self.vec_details_table.heading("akm", text="Distance Travelled (Km)")
        self.vec_details_table.heading("drop_location", text="Drop Location")
        self.vec_details_table.heading("vec_num", text="Vehicle Number")
        self.vec_details_table.heading("vec_date", text="Vehicle Date")
        

        self.vec_details_table["show"]="headings"

        self.vec_details_table.column("a_id", width=120)
        self.vec_details_table.column("aname", width=120)
        self.vec_details_table.column("acontact", width=120)
        self.vec_details_table.column("aemail", width=120)
        self.vec_details_table.column("alocation", width=120)
        self.vec_details_table.column("vec_type", width=120)
        self.vec_details_table.column("akm", width=140)
        self.vec_details_table.column("drop_location", width=120)
        self.vec_details_table.column("vec_num", width=120)
        self.vec_details_table.column("vec_date", width=120)


        self.vec_details_table.pack(fill=BOTH, expand=1)
        self.vec_details_table.bind("<ButtonRelease-1>", self.get_cursor)
    


    #=================================================== Fetching Old Details ================================

    def Fetch_details(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error", "Please Enter the contact number...", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                cur=con.cursor()
                query=("Select fname, lname from registration_details where contact=%s")
                value =(self.var_contact.get(),)
                cur.execute(query, value)
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "User Does not exist!!!! \nYou should register first..", parent=self.root)
                else:
                    con.commit()
                    con.close()

                    # For fetching details and printing them
                    #=================================== For working on the Details Fetch Frame
                    # Details Frame
                    details_frame = LabelFrame(self.root, bg="white", bd=2, relief = RIDGE, text="Previous Details", font=("times new roman", 12, "bold"), padx=2, pady=2)
                    details_frame.place(x=500, y=180, width=500, height=230)

                    # For fetching Details, message
                    l_name = Label(details_frame, text = "Welcome Back !", bg="white", font = ("aerial", 12, "bold"))
                    l_name.place(x=0, y=0)

                    # For fetching name 
                    l_name = Label(details_frame, text = "Name: ", bg="white", font = ("aerial", 12, "bold"))
                    l_name.place(x=0, y=30)

                    lbl_name = Label(details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                    lbl_name.place(x=90, y=30)

                    # For fetching contact number
                    con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                    cur=con.cursor()
                    query=("Select contact from registration_details where contact=%s")
                    value =(self.var_contact.get(),)
                    cur.execute(query, value)
                    row = cur.fetchone()                    

                    l_contact = Label(details_frame, text = "Contact: ", bg="white", font = ("aerial", 12, "bold"))
                    l_contact.place(x=0, y=60)

                    lbl_contact = Label(details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                    lbl_contact.place(x=90, y=60)

                    
                    con.commit()
                    con.close()

                    # For fetching Email Id
                    con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                    cur=con.cursor()
                    query=("Select email_id from registration_details where contact=%s")
                    value =(self.var_contact.get(),)
                    cur.execute(query, value)
                    row = cur.fetchone()                    

                    l_email = Label(details_frame, text = "Email Id: ", bg="white", font = ("aerial", 12, "bold"))
                    l_email.place(x=0, y=90)

                    lbl_email = Label(details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                    lbl_email.place(x=90, y=90)

                    con.commit()
                    con.close()

            except Exception as exc1:
                    messagebox.showerror("Error", f"Error caused by:  {str(exc1)}", parent=self.root)



#================================ Function for checking availability of vehicles


    def check_availability(self):
            if  self.txt_b_contact.get() == "" or  self.txt_b_address.get()=="" or self.txt_b_date.get()=="" or self.b_book_proof.get()=="Select" or self.b_id_num.get()=="":
                messagebox.showerror("Error", "All fields are rquired !!!!!!", parent = self.root)
            else:
                try:
                    # It will connect the database and fetch the info 
                    con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                    cur=con.cursor()
                    cur.execute("select * from inventory_details")
                    row = cur.fetchone()
                    if row == None:
                        # if it doesnt get any user it will throw an error
                        messagebox.showerror("Error", "Vehicles are not available!!!!", parent=self.root)

                    else:
                        con = pymysql.connect(host="localhost", user="root", password = "", database="argo_main" )
                        cur = con.cursor()
                        cur.execute("insert into booking_details (b_contact, b_address, b_bookdate, b_idproof, b_idnumber) values (%s,%s,%s,%s,%s)", 
                                        (
                                            self.txt_b_contact.get(),
                                            self.txt_b_address.get(),
                                            self.txt_b_date.get(),
                                            self.b_book_proof.get(),
                                            self.b_id_num.get(),
                                        ))
                        con.commit()
                        con.close()

                        # Otherwise it will show vehicles are available
                        messagebox.showinfo("Success", "New Details Updated...", parent=self.root)
                        messagebox.showinfo("Success", "Vehicles are available, Select your vehicle type....", parent=self.root)
                        #self.clear()
                        self.show_details()
          

                except Exception as exc1:
                    messagebox.showerror("Error", f"Error caused by:  {str(exc1)}", parent=self.root)



#=================================== Function for saving the data in the database.
    def enter_data(self):
            if  self.b_pick_loc.get()=="Select" or self.b_book_hours.get()=="Select" or self.b_book_days.get()=="Select" or self.b_vec_type.get()=="Choose" or self.b_vec_num.get()=="" :
                messagebox.showerror("Error", "All fields are rquired !!!!!!", parent = self.root)
            elif self.var_chk.get()==0:
                messagebox.showerror("Error", "Accept the Terms and Conditions to Register", parent=self.root)
            else:
                try:
                    con = pymysql.connect(host="localhost", user="root", password = "", database="argo_main" )
                    cur = con.cursor()

                    query=("UPDATE booking_details set b_pickuploc = %s where b_contact = %s")
                    value = (self.b_pick_loc.get(), self.txt_b_contact.get())
                    cur.execute(query, value)

                    query=("UPDATE booking_details set b_booktime = %s where b_contact = %s")
                    value = (self.b_book_hours.get(), self.txt_b_contact.get())
                    cur.execute(query, value)

                    query=("UPDATE booking_details set b_bookdays = %s where b_contact = %s")
                    value = (self.b_book_days.get(), self.txt_b_contact.get())
                    cur.execute(query, value)

                    query=("UPDATE booking_details set b_vectype = %s where b_contact = %s")
                    value = (self.b_vec_type.get(), self.txt_b_contact.get())
                    cur.execute(query, value)

                    query=("UPDATE booking_details set b_vecnumber = %s where b_contact = %s")
                    value = (self.b_vec_num.get(), self.txt_b_contact.get())
                    cur.execute(query, value)


                    con.commit()
                    con.close()

                    messagebox.showinfo("Success", "Details Added Successfully...", parent = self.root)
                    self.delete_ride()
                    self.clear()     
                    self.bill_window()
                        
                except Exception as exc2:
                    messagebox.showerror("Error", f"Error due to: {str(exc2)}", parent = self.root)

                

    def clear(self):

        self.txt_b_contact.delete(0, END),
        self.txt_b_address.delete(0, END),
        self.txt_b_date.delete(0, END),
        self.b_pick_loc.current(0),
        self.b_book_hours.current(0),
        self.b_book_days.current(0),
        self.b_book_proof.current(0),
        self.b_id_num.delete(0, END),
        self.b_vec_type.current(0),
        self.b_vec_num.delete(0, END),
        self.var_chk.set(0),
        self.var_refid.set(0),
        self.search_vec.current(0),
 

#========================================== To Show Vehicle Details======================

    def show_details(self):
        try:
            # It will connect the database and fetch the info 
            con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
            cur=con.cursor()
            cur.execute("select * from inventory_details")
            rows = cur.fetchall()
            if len(rows)!=0:
                self.vec_details_table.delete(*self.vec_details_table.get_children())
                for i in rows:
                    self.vec_details_table.insert("", END, values=i)
                con.commit()
            con.close()

        except Exception as exc2:
            messagebox.showerror("Error", f"Error due to: {str(exc2)}", parent = self.root)



#============================================== To get Cursor Data ======================
    def get_cursor(self, event=""):
        cursor_row = self.vec_details_table.focus()
        content = self.vec_details_table.item(cursor_row)
        row = content["values"]
        self.var_refid.set(row[0]),
        self.var_pickuploc.set(row[7]),
        self.var_vectype.set(row[5]),
        self.var_vecnum.set(row[8])
        


#=============================================== To Delete the Booked ride
    def delete_ride(self):
        lbl_delete = messagebox.askyesno("Booking Confirmation", "Do you want to book this Ride....", parent = self.root)
        try:
            if lbl_delete>0:
                con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                cur=con.cursor()
                query = ("Delete from inventory_details where a_id = %s")
                value = (self.var_refid.get())
                cur.execute(query, value)
            else:
                if not lbl_delete:
                    return
                con.commit()
                self.show_details()
                con.close()


        except Exception as exc2:
            messagebox.showerror("Error", f"Error due to: {str(exc2)}", parent = self.root)


#============================================ Search Function ==============================

    def search_func(self):
        try:
                con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                cur=con.cursor()
                cur.execute("select * from inventory_details where " + str(self.search_var.get())+" LIKE '%"+str(self.text_search.get())+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.vec_details_table.delete(*self.vec_details_table.get_children())
                    for i in rows:
                        self.vec_details_table.insert("", END, values=i)
                    con.commit()
                con.close()          


        except Exception as exc2:
            messagebox.showerror("Error", f"Error due to: {str(exc2)}", parent = self.root)


    # Function to call the Login Page
    def bill_window(self):
        messagebox.showinfo("Good Bye", "Taking you to the Bill screen..... Please Wait....", parent=self.root)
        self.root.destroy()
        import Argo_Map




root = Tk()
obj = User_Booking(root)
root.iconbitmap("Assets\\argo_icon.ico")
root.mainloop()  # Closing mainloop
