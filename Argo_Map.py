# Argo Login Interface
# Minor Project: 3rd Year AIML CSE Batch: B5 Non-Hons. 
# Project Made By: Bhavy Kharbanda (500082531), Anuj Singh (500082307), Dhruv Gupta (500083965)

# importing libraries
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import tkintermapview


class User_Bill:
    def __init__(self, root):
        self.root = root
        self.root.title("ARGO : Billing Page")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="#90EE90")  # Background default color

        #=================================== For banner Image
        banner = Image.open("Assets\\map_bg.png")
        banner = banner.resize((1350, 700))
        self.banner_img = ImageTk.PhotoImage(banner)

        #=================================== For Logo Image
        label1 = Label(self.root, image = self.banner_img, bd=2, relief=RIDGE)
        label1.place(x=0, y=0, width=1350, height=700)

        # Login form frame -> white
        self.map_frame = Frame(self.root, bg="#dadeff")
        self.map_frame.place(x=50, y=100, width=750, height=500)

        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, width=750, height=500, corner_radius=0)
        self.map_widget.pack()

        self.map_widget.set_position(30.416131, 77.966858) # Default Coordinates => UPES Bidholi
        self.map_widget.set_zoom(11)
  
        marker_1 = self.map_widget.set_marker(30.416131, 77.966858, text="UPES Bidholi")
        marker_2 = self.map_widget.set_marker(30.384003, 77.968471, text="UPES Kandoli")
        marker_3 = self.map_widget.set_marker(30.3378635,77.9593852, text="Nanda Ki Chowki")
        marker_4 = self.map_widget.set_marker(30.345089, 77.936138, text="Sudhowala Chowk")
        marker_5 = self.map_widget.set_marker(30.3441477,77.9978329, text="Forest Research Institute (FRI)")
        marker_6 = self.map_widget.set_marker(30.338184, 77.992302, text="Indian Military Academy")
        marker_7 = self.map_widget.set_marker(30.334275, 77.960179, text="Premnagar")
        marker_8 = self.map_widget.set_marker(30.320479, 78.037355, text="Paltan Bazar")
        marker_9 = self.map_widget.set_marker(30.324292, 78.041937, text="Ghanta Ghar")
        marker_10 = self.map_widget.set_marker(30.366174, 78.070973, text="Pacific Mall")

        # Bill frame -> white
        self.bill_frame = Frame(self.root, bg="white")
        self.bill_frame.place(x=800, y=100, width=500, height=500)

        # For register heading
        title1 = Label(self.bill_frame, text="Enter your Contact to Fetch Bill Details", font=("times new roman", 20, "bold"), bg="green", fg="white", bd=5, relief=RIDGE)
        title1.place(x=10, y=10)

        # For creating the form: Contact
        bill_contact = Label(self.bill_frame, text="Contact No", font=("times new roman", 15), bg="white", fg="black")
        bill_contact.place(x=10, y=70)

        self.var_contact = StringVar()
        self.txt_contact = Entry(self.bill_frame, textvariable=self.var_contact, font=("times new roman", 13), bg="#EEEEEE", bd=1)
        self.txt_contact.place(x=120, y=70, width=250, height = 25)


        btn_fetch = Button(self.bill_frame, text="Fetch Bill", command = self.Fetch_details, font=("Vani", 12, "bold"), bg="black", fg="white", bd=5, cursor="hand2")
        btn_fetch.place(x=380, y=70, width=100, height=25)

    
        # For creating an Exit Button
        btn_exit = Button(self.root, text="LEAVE", command = self.argo_exit, font=("Vani", 18, "bold"), bg="white", fg="black", bd=5, cursor="hand2")
        btn_exit.place(x=500, y=650, width=400, height=35)



        #=================================== For working on the main frame
        # Details Frame
        self.details_frame = LabelFrame(self.bill_frame, bg="white", bd=2, relief = RIDGE, text="Bill Details", font=("times new roman", 12, "bold"), padx=2, pady=2)
        self.details_frame.place(x=5, y=110, width=490, height=380)

        label22 = Label(self.details_frame, bg="lightgrey")
        label22.place(x=0, y=0, width=480, height=80)

        #=================================== For banner Image
        logo = Image.open("Assets\\map_logo.png")
        logo = logo.resize((60, 60))
        self.logo_img = ImageTk.PhotoImage(logo)

        #=================================== For Logo Image
        label1 = Label(self.details_frame, image = self.logo_img, bd=2, relief=RIDGE)
        label1.place(x=50, y=10)

        # For creating the form: Contact
        label2 = Label(self.details_frame, text="A R G O", font=("times new roman", 24, "bold"), bg="lightgrey", fg="black")
        label2.place(x=220, y=8)

        # For creating the form: Contact
        label3 = Label(self.details_frame, text="Affordable Rides on Go", font=("times new roman", 20, "bold"), bg="lightgrey", fg="black")
        label3.place(x=140, y=40)


        #=================== Variables
        self.var_booking_time = StringVar()
        self.var_booking_day = StringVar()
        self.var_vehicle_type = StringVar()
        self.var_pickup_loc = StringVar()

    

    def Fetch_details(self):
            if self.var_contact.get()=="":
                messagebox.showerror("Error", "Please Enter the contact number...", parent=self.root)
            else:
                try:
                    con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                    cur=con.cursor()
                    query=("Select fname, lname from registration_details where contact=%s")
                    value =(self.var_contact.get())
                    cur.execute(query, value)
                    row = cur.fetchone()

                    if row == None:
                        messagebox.showerror("Error", "User Does not exist!!!! \nYou should register first..", parent=self.root)
                    else:


                        # For fetching name 
                        l_name = Label(self.details_frame, text = "Name: ", bg="white", font = ("aerial", 12, "bold"))
                        l_name.place(x=0, y=100)

                        lbl_name = Label(self.details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                        lbl_name.place(x=150, y=100)

                        # For fetching contact number
                        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                        cur=con.cursor()
                        query=("Select contact from registration_details where contact=%s")
                        value =(self.var_contact.get())
                        cur.execute(query, value)
                        row = cur.fetchone()                    

                        l_contact = Label(self.details_frame, text = "Contact: ", bg="white", font = ("aerial", 12, "bold"))
                        l_contact.place(x=0, y=130)

                        lbl_contact = Label(self.details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                        lbl_contact.place(x=150, y=130)


                        # For fetching Email Id
                        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                        cur=con.cursor()
                        query=("Select email_id from registration_details where contact=%s")
                        value =(self.var_contact.get())
                        cur.execute(query, value)
                        row = cur.fetchone()                    

                        l_email = Label(self.details_frame, text = "Email Id: ", bg="white", font = ("aerial", 12, "bold"))
                        l_email.place(x=0, y=160)

                        lbl_email = Label(self.details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                        lbl_email.place(x=150, y=160)

                        con.commit()
                        con.close()


                        # For fetching Booking date
                        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                        cur=con.cursor()
                        query=("Select b_bookdate from booking_details where b_contact=%s")
                        value =(self.var_contact.get())
                        cur.execute(query, value)
                        row = cur.fetchone()                    

                        l_bookdate = Label(self.details_frame, text = "Booking Date: ", bg="white", font = ("aerial", 12, "bold"))
                        l_bookdate.place(x=0, y=190)

                        lbl_bookdate = Label(self.details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                        lbl_bookdate.place(x=150, y=190)

                        # For fetching Pickup Loc
                        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                        cur=con.cursor()
                        query=("Select b_pickuploc from booking_details where b_contact=%s")
                        value =(self.var_contact.get())
                        cur.execute(query, value)
                        row = cur.fetchone()    
                        self.var_pickup_loc = row               

                        l_pickup = Label(self.details_frame, text = "Pickup Location: ", bg="white", font = ("aerial", 12, "bold"))
                        l_pickup.place(x=0, y=220)

                        lbl_pickup = Label(self.details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                        lbl_pickup.place(x=150, y=220)

                        # For fetching Book time
                        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                        cur=con.cursor()
                        query=("Select b_booktime from booking_details where b_contact=%s")
                        value =(self.var_contact.get())
                        cur.execute(query, value)
                        row = cur.fetchone()   
                        self.var_booking_time = row                

                        l_booktime = Label(self.details_frame, text = "Time Duration: ", bg="white", font = ("aerial", 12, "bold"))
                        l_booktime.place(x=0, y=250)

                        lbl_booktime = Label(self.details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                        lbl_booktime.place(x=150, y=250)

                        # For fetching Book Days
                        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                        cur=con.cursor()
                        query=("Select b_bookdays from booking_details where b_contact=%s")
                        value =(self.var_contact.get())
                        cur.execute(query, value)
                        row = cur.fetchone()                   
                        self.var_booking_day = row
                        l_bookdays = Label(self.details_frame, text = "No. of Days: ", bg="white", font = ("aerial", 12, "bold"))
                        l_bookdays.place(x=0, y=280)

                        lbl_bookdays = Label(self.details_frame, text=row, bg="white", font = ("aerial", 12, "bold"))
                        lbl_bookdays.place(x=150, y=280)

                        l_finalbill = Label(self.details_frame, text = "Final Bill: ", bg="white", font = ("aerial", 12, "bold"))
                        l_finalbill.place(x=0, y=310)

                        #=============================== Calling Bill calculate function and Map Function
                        self.bill_calculate()
                        self.map_color()

                        lbl_finalrs = Label(self.details_frame, text="Rs. ", bg="white", font = ("aerial", 12, "bold"))
                        lbl_finalrs.place(x=150, y=310)

                        lbl_finalbill = Label(self.details_frame, text=self.final_price, bg="white", font = ("aerial", 12, "bold"))
                        lbl_finalbill.place(x=180, y=310)


                        con.commit()
                        con.close()

                except Exception as exc1:
                        messagebox.showerror("Error", f"Error caused by:  {str(exc1)}", parent=self.root)
            
    def argo_exit(self):
        messagebox.showinfo("Good Bye", "Thanks for using our service....", parent=self.root)
        self.root.destroy()
        import Argo_Thanks


    def bill_calculate(self):

        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
        cur=con.cursor()
        query=("Select b_vectype from booking_details where b_contact=%s")
        value =(self.var_contact.get())
        cur.execute(query, value)
        self.var_vehicle_type = cur.fetchone()  
        con.commit()
        con.close()

        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
        cur=con.cursor()
        cur.execute("Select final_price from price_mastertable where book_time= %s AND book_day=%s AND vehicle_type=%s",
                                                (self.var_booking_time, self.var_booking_day, self.var_vehicle_type))
        row=cur.fetchone()
        self.final_price=row

        con.commit()
        con.close()


    def map_color(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
        cur=con.cursor()
        query=("Select lat_cord, long_cord from location_cords where vec_location=%s")
        value=(self.var_pickup_loc)
        cur.execute(query, value)
        row = cur.fetchone()
        print(row)
        coords = []
        coords = row
        marker_1 = self.map_widget.set_marker(coords[0], coords[1], marker_color_circle="yellow", marker_color_outside="blue")


        con.commit()
        con.close()




root = Tk()
obj = User_Bill(root)
root.iconbitmap("Assets\\argo_icon.ico")
root.mainloop()
