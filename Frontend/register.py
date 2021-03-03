# use doc string to make this code attractive
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk  # pip install pillow

import Frontend.login
import Backend.dbconnection
import Models.user


class Register():
    def __init__(self, root):
        self.root = root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.db = Backend.dbconnection.DBConnect()
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
        self.txt_Contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_Contact.place(x=50, y=200, width=250)

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

        # to set "select" as default in combo box
        self.cmb_question.current(0)
        # =======Answer============
        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(x=370,
                                                                                                                  y=240)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)

        # ====Password=======
        pasw = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="Black").place(
            x=50, y=310)
        self.txt_pasw = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_pasw.place(x=50, y=340, width=250)

        # ======Confirm password============
        p_confirm = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                          fg="Black").place(x=370, y=310)
        self.txt_confirm = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_confirm.place(x=370, y=340, width=250)

        # -------  check box-------

        self.var_chk = IntVar()
        chk_box = Checkbutton(frame1, text="I Agree The Terms And Condition", variable=self.var_chk, onvalue=1,
                              offvalue=0, bg='white', font=("times new roman", 12)).place(x=50, y=370)

        # ----Register button------

        self.register_btn = Button(frame1, text="Register Now", font=("times new roman", 14, "bold"), bg="white",
                                   fg="blue", bd="5", cursor="hand2", command=self.register_data).place(x=50, y=410,
                                                                                                        width=250)

        # ------------Signin Buttonn setup ---------------
        lbl_account = Label(frame1, text="Already have an Account?", font=("times new roman", 12), bg="white",
                            fg="Black").place(
            x=340, y=390)

        lbl_signup = Label(frame1, text="SignIn Here", font=("times new roman", 14, "bold"), bg="white", fg="#2EFEF7",
                           bd="5", cursor="hand2")
        lbl_signup.place(x=370, y=410)
        lbl_signup.bind('<Button-1>', self.lbl_signin_click)

    def register_data(self):
        FirstName = self.txt_fname.get()
        LastName = self.txt_lname.get()
        Confirm_password = self.txt_confirm.get()
        Password_=self.txt_pasw.get()
        Answer = self.txt_answer.get()
        Security_Question =self.cmb_question.get()
        Email_ID=self.txt_email.get()
        ContactNo=self.txt_Contact.get()


        if self.txt_fname.get() == "" or self.txt_lname.get()=="" or self.txt_Contact.get() == "" or self.txt_email.get() == "" or self.cmb_question.get() == "select" or self.txt_answer.get() == "" or self.txt_pasw.get() == "" or self.txt_confirm.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root)

        #elif self.txt_pasw.get() != self.txt_confirm.get():
         #   messagebox.showerror("Error", "Password and confirm password should be same", parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Comobox is uncheckez, plz check it", parent=self.root)

        #else:
         #   messagebox.showinfo("success", "Register sucessful", parent=self.root)

            return
        u = Models.user.User(FirstName, LastName, Confirm_password, Password_, Answer, Security_Question, Email_ID,
                             ContactNo)

        query = "insert into tbl_user(FirstName,LastName,Password_,Confirm_password,Answer,Security_Question,Email_ID,ContactNo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (u.get_FirstName(),u.get_LastName(), u.get_Password_(), u.get_Confirm_password(), u.get_Answer(),
                  u.get_Security_Question(),u.get_Email_ID(),u.get_ContactNo())

        self.db.insert(query, values)
        messagebox.showinfo('Success', 'User Registration successfull')
        self.root.destroy()




    def lbl_signin_click(self, event):
        '''THis function is the listener function for signin button'''
        tk = Toplevel()
        Frontend.login.Login_window(tk)
