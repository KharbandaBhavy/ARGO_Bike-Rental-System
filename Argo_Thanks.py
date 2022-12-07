# Argo Thank you Interface
# Minor Project: 3rd Year AIML CSE Batch: B5 Non-Hons. 
# Project Made By: Bhavy Kharbanda (500082531), Anuj Singh (500082307), Dhruv Gupta (500083965)

# importing libraries
from tkinter import*
from tkinter import ttk
from PIL import ImageTk

class User_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("ARGO : Affordable Rides on Go")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="blue")  # Background default color

        # For background image and its placement
        self.bg = ImageTk.PhotoImage(file="Assets\\thanks_bg.png")
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # For inserting Logo image
        self.bg2 = ImageTk.PhotoImage(file="Assets\\thanks_logo.png")
        bg2 = Label(self.root, image=self.bg2)
        bg2.place(x=700, y=270, width=550, height=350)


        # For Login Page headings
        login_title1 = Label(self.root, text="Thank You for using ARGO", font=("Rockwell Extra Bold", 26, "bold"), bg="#011058", fg="white")
        login_title1.place(x=400, y=50)

        login_title2 = Label(self.root, text="Come Back Again", font=("times new roman", 20), bg="#001d7c", fg="white" )
        login_title2.place(x=600, y=100)

        # For creating an Exit Button
        btn_exit = Button(self.root, text="EXIT", command = self.exit_window, font=("Vani", 14, "bold"), bg="#011058", fg="white", bd=5, cursor="hand2")
        btn_exit.place(x=1175, y=650, width=150, height=40)


    # Function to exit app
    def exit_window(self):
        self.root.destroy()


root = Tk()
obj = User_Login(root)
root.iconbitmap("Assets\\argo_icon.ico")
root.mainloop()
