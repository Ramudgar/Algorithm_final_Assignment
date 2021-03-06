from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
import Backend.dbconnection
import Frontend.dashboard
import Frontend.register


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login window")
        self.root.geometry("1150x700+0+0")
        self.root.config(bg="#2EFEF7")

        self.db = Backend.dbconnection.DBConnect()

        title = Label(self.root, text="Login System for Student ledger Management ", font=("poopins", 20, "bold"),
                      bg="#2EFEF7", fg="white").place(x=0, y=0)

        left_lbl = Label(self.root, bg="#021e2f", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#2EFEF7", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

#=========BG Image==================================

        self.bg = ImageTk.PhotoImage(file="images\maxresdefault.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

# ======= Frame================================================
        login_frame = Frame(self.root, bg="#E67206")
        login_frame.place(x=200, y=100, width=800, height=500)

  #================= Title ==============================
        title = Label(login_frame, text="LOGIN SYSTEM ", font=("poopins", 30, "bold"), bg="#DA7605", fg="white")\
            .place(x=300, y=50,width=450)
#=== email =========================
        email = Label(login_frame, text="Email Address", font=("poopins", 18, "bold"), bg="#E67206", fg="black").place(
            x=250, y=150)
        self.txt_email = Entry(login_frame, font=("Times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)
#==== pasw =========================================
        pasw = Label(login_frame, text="Password", font=("poopins", 18, "bold"), bg="#E67206", fg="black").place(x=250,
                                                                                                               y=250)
        self.txt_pasw = Entry(login_frame, font=("Times new roman", 15), bg="Lightgray")
        self.txt_pasw.place(x=250, y=280, width=350, height=35)


#==========SignUp========================================
        lbl_signup = Label(login_frame, text='No account? Sign Up.',font=(20), fg='white', bg='#E67206')
        lbl_signup.place(x=250, y=330)

        lbl_signup.bind('<Button-1>', self.lbl_signup_click)# Event handling method is used to call the signup button

#==============Login Button=====================================
        btn_log = Button(login_frame, text="LOGIN", font=("POOPINS", 20, "bold"), bg="white", fg="green",
                         cursor="hand2", command=self.btn_login_click).place(x=250, y=390, width=180, height=40)

# ==========clock=======================================================
        self.lbl = Label(self.root, text="\nStudent ledger Management", font=("Book Antiqua", 18, "bold"), compound=BOTTOM,
                         bg="#081923", fg="White", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()

    def clock_image(self, hr, min_, sec_):

        ''' this function draws hour,min and sec line in to clock image and sets
        angle for rotation of hour,min and sec lines '''

        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        #  for clock Image=====
        bg = Image.open("images/clock1.jpg")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        # ===for Hour line Image===
        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="black", width=4)
        # ===for minute line Image===
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="blue", width=3)
        # ===for Second line Image===
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="green", width=2)
        draw.ellipse((190, 190, 210, 210), fill="black")
        clock.save("clock_new.png")

    def working(self):
        '''
        This function fetch current time
        :return: time
        '''
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(190, self.working)

    def btn_login_click(self):
        '''
        This function matches the input email and password with data stored in the database;
        If email and password stored in the database match with input value then open the dashboard page
        :return:none
        '''
        email=self.txt_email.get()
        pasw=self.txt_pasw.get()

        try:
            if email=='' or pasw=='':
                messagebox.showerror('Error','plz fill the empty field')
            else:
                query="select * from tbl_user where Email_ID=%s and Password_=%s"
                values=(email,pasw)
                rows=self.db.select(query,values)
                data=[]
                #print(rows)
                if len(rows)!=0:
                    for row in rows:
                        data.append(row[3])
                        data.append(row[6])
                    #print(data)
                    if email==data[0] and pasw==data[1]:

                        messagebox.showinfo('Success','Congratulations!! login successfull')
                        tk=Tk()
                        Frontend.dashboard.Student(tk)
                        self.root.destroy()

                    else:
                        messagebox.showerror('Error','Invalid email and password')
                else:
                    messagebox.showinfo("Error","User not registered !! Register first")

        except IndexError:
            print(" An error occured in btn_login_click")

    def lbl_signup_click(self,event):
        ''' This function is the listener function for sign up button'''
        tk=Toplevel()
        Frontend.register.Register(tk)






