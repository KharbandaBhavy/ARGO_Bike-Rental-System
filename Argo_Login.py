# Argo Login Interface
# Minor Project: 3rd Year AIML CSE Batch: B5 Non-Hons. 
# Project Made By: Bhavy Kharbanda (500082531), Anuj Singh (500082307), Dhruv Gupta (500083965)

# importing libraries
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

class User_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("ARGO : Login Page")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="#bfccff")  # Background default color

        # For background image and its placement
        self.bg = ImageTk.PhotoImage(file="Assets\\login_bg.png")
        bg = Label(self.root, image=self.bg)
        bg.place(x=400, y=0, relwidth=1, relheight=1)

        # For inserting Bike image
        self.bg2 = ImageTk.PhotoImage(file="Assets\\login_fg.png")
        bg2 = Label(self.root, image=self.bg2)
        bg2.place(x=175, y=100, width=500, height=500)

        

        # Login form frame -> white
        login_frame = Frame(self.root, bg="#dadeff")
        login_frame.place(x=675, y=100, width=500, height=500)

        # For Login Page heading
        login_title1 = Label(login_frame, text="Welcome Back", font=("Rockwell Extra Bold", 24, "bold"), bg="#dadeff")
        login_title1.place(x=100, y=40)

        login_title2 = Label(login_frame, text="Please Login to your Account", font=("times new roman,", 14, ), bg="#dadeff")
        login_title2.place(x=120, y=80)

        # ======================== For Row 1
        # For creating the form: Email Id
        email_id_login = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 14, "bold"), bg="#dadeff", fg="black")
        email_id_login.place(x=120, y=150)

        self.txt_email_id_login = Entry(login_frame, font=("times new roman", 13), bg="white")
        self.txt_email_id_login.place(x=120, y=180, width=250)

        # ======================== For Row 2
        # For creating the form: Password
        login_password = Label(login_frame, text="PASSWORD", font=("times new roman", 14, "bold"), bg="#dadeff", fg="black")
        login_password.place(x=120, y=230)

        self.txt_login_password = Entry(login_frame, font=("times new roman", 13), bg="white", show='*')
        self.txt_login_password.place(x=120, y=260, width=250)
        check_pass=IntVar(value=0)
        
        # Function to hide the password
        def pass_show():
            if(check_pass.get()==1):
                self.txt_login_password.config(show='')
            else:
                self.txt_login_password.config(show='*')

        pass_check1 = Checkbutton(login_frame,text="Show Password",variable=check_pass, onvalue=1, offvalue=0, bg="#dadeff", font=("times new roman", 11),command=pass_show)
        pass_check1.place(x=120, y=290)

        # For new user
        new_user_title3 = Label(login_frame, text="New User to ARGO?", font=("Times New Roman Greek",11), bg="#dadeff")
        new_user_title3.place(x=120, y=360)

        # For creating a register button
        btn_register = Button(login_frame, text="Create Account", command = self.register_window, font=("Times New Roman Greek", 12), bg="#dadeff", bd=0, cursor="hand2", fg="blue")
        btn_register.place(x=260, y=360, height=20)

        # For creating a login button
        btn_login = Button(login_frame, text="LOGIN", command = self.argo_login, font=("times new roman", 20), bg="black", bd=5, cursor="hand2", fg="white")
        btn_login.place(x=160, y=400, width = 180, height=40)
        

    # Function to call the Registration Page
    def register_window(self):
        self.root.destroy()
        import Argo_Register



    # Login Error function and Database Connectivity
    def argo_login(self):
        # If the fields are empty it will pop an error message
        if self.txt_email_id_login.get() =="" or self.txt_login_password.get() =="":
            messagebox.showerror("Error", "All Fields are Required   !!!!!!!", parent=self.root)
        else:
            try:
                # else it will connect the database and fetch the info if the user exists or not
                con=pymysql.connect(host="localhost", user="root", password="", database="argo_main")
                cur=con.cursor()
                cur.execute("select * from registration_details where email_id=%s and password=%s", (self.txt_email_id_login.get(), self.txt_login_password.get()))
                row = cur.fetchone()
                if row == None:
                    # if it doesnt get any user it will throw an error
                    messagebox.showerror("Error", "Invalid Username and Password...", parent=self.root)

                else:
                    # Otherwise it will accept the user
                    messagebox.showinfo("Success", "Welcome to ARGO...", parent=self.root)
                    self.root.destroy()
                    import Argo_Dashboard
                con.close() 

            except Exception as exc1:
                messagebox.showerror("Error", f"Error caused by:  {str(exc1)}", parent=self.root)


root = Tk()
obj = User_Login(root)
root.iconbitmap("Assets\\argo_icon.ico")
root.mainloop()
