# Argo Dashboard interface
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


# Class definition for Dashboard of the APP
class User_Dashboard:

    # Defining the constructor
    def __init__(self, root):
        self.root = root
        self.root.title("ARGO : Dashboard")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="#c0f9fb")  # Background default color

        # For background image and its placement
        self.bg = ImageTk.PhotoImage(file="Assets\\dashboard_bg.jpg")
        bg = Label(self.root, image=self.bg)
        bg.place(x=370, y=0, relwidth=1, relheight=1)

        # For left side image and its placement
        self.bg2 = ImageTk.PhotoImage(file="Assets\\dashboard_fg.png")
        bg2 = Label(self.root, image=self.bg2)
        bg2.place(x=120, y=100, width=550, height=500)

        
        # Creating a Frame for the information
        dashboard_frame = Frame(self.root, bg="#c0f9fb")
        dashboard_frame.place(x=670, y=100, width=550, height=500)

        # Creating a Divider Image
        self.img1 = ImageTk.PhotoImage(file="Assets\\Divider.png")
        self.male_img = ImageTk.PhotoImage(file="Assets\\dashboard_1.png")
        self.female_img = ImageTk.PhotoImage(file="Assets\\dashboard_2.png")


        # For register heading
        title1 = Label(dashboard_frame, text="AFFORDABLE RIDES ON GO", font=("Tempus Sans ITC", 24, "bold"), bg="#c0f9fb")
        title1.place(x=60, y=20)

        # For register heading
        title2 = Label(dashboard_frame, text="Welcome User, Select your service!", font=("Microsoft YaHei", 16), bg="#c0f9fb")
        title2.place(x=100, y=100)

        # For Placing that Divider Image
        img_label1 = Label(dashboard_frame, image=self.img1, bg="#046FCA")
        img_label1.place(x=0, y=70, height = 10)

        btn_male = Button(dashboard_frame, image=self.male_img, command = self.Booking_prompt, bd=2, cursor="hand2")
        btn_male.place(x=50, y=160, width=200, height = 200)

        btn_female = Button(dashboard_frame, image=self.female_img, command = self.Create_prompt, bd=2, cursor="hand2")
        btn_female.place(x=300, y=160, width=200, height = 200)

         # For creating Book Ride button
        btn_ride = Button(dashboard_frame, text="Book A Ride", command = self.Booking_window, font=("Vani", 14, "bold"), bg="#046FCA", fg="white", bd=5, cursor="hand2")
        btn_ride.place(x=50, y=370, width=200, height=40)

         # For creating Create Ride Button
        btn_create = Button(dashboard_frame, text="Create A Ride", command = self.Creating_window, font=("Vani", 14, "bold"), bg="#046FCA", fg="white", bd=5, cursor="hand2")
        btn_create.place(x=300, y=370, width=200, height=40)

        # For creating a Logout Button
        btn_logout = Button(dashboard_frame, text="Log Out", command = self.login_window, font=("Vani", 14, "bold"), bg="#046FCA", fg="white", bd=5, cursor="hand2")
        btn_logout.place(x=150, y=430, width=250, height=40)



    # Function to call the Login Page
    def login_window(self):
        messagebox.showinfo("Good Bye", "Thanks for using our service....", parent=self.root)
        self.root.destroy()
        import Argo_Thanks



    # Function to call the Booking message
    def Booking_prompt(self):
        messagebox.showinfo("Book a Ride", "Thanks for Showing interest in our service. \nPress on the button below to take you to the Booking window.", parent=self.root)

    # Function to call the creating ride message
    def Create_prompt(self):
        messagebox.showinfo("Create a Ride", "Thanks for Showing interest in our service. \nPress on the button below to take you to the Creating Ride window.", parent=self.root)


    # Function to call the Booking Page
    def Booking_window(self):
        self.root.destroy()
        import Argo_Booking

    # Function to call the Creating window Page
    def Creating_window(self):
        self.root.destroy()
        import Argo_Create



root = Tk()
obj = User_Dashboard(root)
root.iconbitmap("Assets\\argo_icon.ico")
root.mainloop()  # Closing mainloop
