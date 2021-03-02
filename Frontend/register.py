# use doc string to make this code attractive
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk  # pip install pillow

import Frontend.login
#import backend.dbconnection
#import Models.user


class Register():
    def __init__(self, root):
        self.root = root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #self.db = backend.dbconnection.DBConnect()
        ### Background image
        self.bg = ImageTk.PhotoImage(file="images\maxresdefault.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # === Left Image====
        self.left = ImageTk.PhotoImage(file="images/sensors.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        # ======Register frame======
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        # =============String Var======
        # self.var_fname=StringVar()
        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="Green").place(
            x=50, y=30)

        # ======First Name===Entry field=======
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(
            x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        # ==== Last Name===========
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(
            x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        # ======Contact no============
        Contact_no = Label(frame1, text="Contact No:", font=("times new roman", 15, "bold"), bg="white",
                           fg="Black").place(x=50, y=170)
        self.txt_Contact_no = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_Contact_no.place(x=50, y=200, width=250)

        # =======Email============
        email = Label(frame1, text="Email ID", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(
            x=370, y=170)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # ========Security question=====
        question = Label(frame1, text="Security Question", font=("times new roman", 13, "bold"), bg="white",
                         fg="Black").place(x=50, y=240)

        # Using combo box=====
        self.cmb_question = ttk.Combobox(frame1, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.cmb_question["values"] = ("select", "Your first pet name", "Your birt place", "Your best friend Name")
        self.cmb_question.place(x=50, y=270, width=250)

        # to set "select" as defaul in combo box
        self.cmb_question.current(0)
        # =======Answer============
        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(x=370,
                                                                                                                  y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # ====Password=======
        pasword = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(
            x=50, y=310)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)

        # ======Confirm password============
        password_confirm = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                                 fg="Black").place(x=370, y=310)
        self.txt_confirm = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_confirm.place(x=370, y=340, width=250)

        # -------  check box-------

        self.var_chk = IntVar()
        chk_box = Checkbutton(frame1, text="I Agree The Terms And Condition", variable=self.var_chk, onvalue=1,
                              offvalue=0, bg='white', font=("times new roman", 12)).place(x=50, y=370)

        # ----set button------

        self.register_btn = Button(frame1, text="Register Now", font=("times new roman", 14, "bold"), bg="white",
                                   fg="blue", bd="5", cursor="hand2", command=self.register_data).place(x=50, y=410,
                                                                                                        width=250)


        lbl_signup = Label(frame1, text="Sign In", font=("times new roman", 14, "bold"), bg="white", fg="blue",
                             bd="5", cursor="hand2")
        lbl_signup.place(x=370, y=410)
        lbl_signup.bind('<Button-1>', self.lbl_signin_click)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_Contact_no.get() == "" or self.txt_email.get() == "" or self.cmb_question.get() == "select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_confirm.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root)

        elif self.txt_password.get() != self.txt_confirm.get():
            messagebox.showerror("Error", "Password and confirm password should be same", parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Comobox is uncheckez, plz check it", parent=self.root)

        else:
            messagebox.showinfo("success", "Register sucessful", parent=self.root)


    def lbl_signin_click(self, event):
        tk = Toplevel()
        Frontend.login.Login_window(tk)

