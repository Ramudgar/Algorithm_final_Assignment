from tkinter import *
from tkinter import ttk
import Models.dbdashboard
from tkinter import messagebox
import Backend.dbconnection


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="pink", fg="black")
        title.pack(side=TOP, fill=X)

        self.db = Backend.dbconnection.DBConnect()



        # ======manage frame========================
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink")
        manage_frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(manage_frame, text="Manage Students", bg="pink", fg="black",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(manage_frame, text="Roll no.", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txt_roll = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                              relief=GROOVE)
        self.txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(manage_frame, text="Name", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                              relief=GROOVE)
        self.txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(manage_frame, text="Email", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_email = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                               relief=GROOVE)
        self.txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(manage_frame, text="Gender", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.combo_gender = ttk.Combobox(manage_frame, font=("times new roman", 14, "bold"),
                                         state='readonly')
        self.combo_gender['values'] = ("male", "female", "other")
        self.combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_contact = Label(manage_frame, text="Contact", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                                 relief=GROOVE)
        self.txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_dob = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
        self.txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(manage_frame, text="Address", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Entry(manage_frame, width=30, font=("times new roman", 10, "bold"))
        self.txt_address.grid(row=7, column=1,ipady=20, pady=10, padx=20, sticky="w")

        # ======button frame=====
        btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="pink")
        btn_frame.place(x=10, y=500, width=420)

        Addbtn = Button(btn_frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=10,
                                                                                        pady=10)
        Updatebtn = Button(btn_frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_frame, text="Clear",command=self.clear_data, width=10).grid(row=0, column=3, padx=10, pady=10)

        # ======detail frame========================
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink")
        detail_frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(detail_frame, text="Search By", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.combo_search = ttk.Combobox(detail_frame, font=("times new roman", 13, "bold"), state='readonly')
        self.combo_search['values'] = ("Roll", "Name", "Contact")
        self.combo_search.grid(row=0, column=1, padx=20, pady=10)

        self.txt_search = Entry(detail_frame, width=20, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(detail_frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(detail_frame, text="Show All", width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        # ============table frame=============
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="pink")
        table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                     columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")
        self.student_table['show'] = 'headings'

        #===================
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
#===== Event Handling ===================

        self.student_table.bind("<ButtonRelease-1>",self.Regenerate)
        self.fetch_data()

#===================== Function for Add button ===========================
    def add_student(self):
        roll_no = self.txt_roll.get()
        name = self.txt_name.get()
        email = self.txt_email.get()
        combo_gender = self.combo_gender.get()
        contact = self.txt_contact.get()
        dob = self.txt_dob.get()
        address = self.txt_address.get()

        u = Models.dbdashboard.Student(roll_no, name, email, combo_gender, contact, dob, address)

        query = "insert into student(roll_no,name,email,gender,contact," \
                "dob,address) values(%s,%s,%s,%s,%s,%s,%s)"
        values = (
            u.get_roll_no(), u.get_name(), u.get_email(), u.get_gender(),
            u.get_contact(), u.get_dob(), u.get_address())

        self.db.insert(query, values)
        messagebox.showinfo('Success', 'User Registration successfull')

        self.fetch_data()
        self.clear_data()
        #self.root.destroy()

    def fetch_data(self):
        self.db = Backend.dbconnection.DBConnect()
        query = 'select * from student'
        rows = self.db.selectall(query)
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)

    def clear_data(self):
        self.txt_roll.delete(0,END)
        self.txt_name.delete(0,END)
        self.txt_email.delete(0,END)
        self.combo_gender.delete(0,END)
        self.txt_contact.delete(0, END)
        self.txt_dob.delete(0, END)
        self.txt_address.delete(0, END)



        self.txt_roll.insert(0,"")
        self.txt_name.insert(0,"")
        self.txt_email.insert(0,"")
        self.combo_gender.insert(0,"")
        self.txt_contact.insert(0,"")
        self.txt_dob.insert(0,"")
        self.txt_address.insert(0,"")

    def Regenerate(self,event):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']

        self.txt_roll.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_email.delete(0, END)
        self.combo_gender.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_dob.delete(0, END)
        self.txt_address.delete(0, END)

        self.txt_roll.insert(0,row[0])
        self.txt_name.insert(1,row[1])
        self.txt_email.insert(2,row[2])
        self.combo_gender.insert(3,row[3])
        self.txt_contact.insert(4,row[4])
        self.txt_dob.insert(5,row[5])
        self.txt_address.insert(6,row[6])

# root=Tk()
# ob=Student(root)
# root.mainloop()
