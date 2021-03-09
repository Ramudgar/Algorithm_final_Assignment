from tkinter import *
from tkinter import ttk
import Models.dbdashboard

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="pink", fg="black")
        title.pack(side=TOP, fill=X)

        self.db = Models.dbdashboard.Student()

        # ====all variables=======
        # self.Roll_N0_Var = StringVar()
        # self.name_Var = StringVar()
        # self.email_Var = StringVar()
        # self.gender_Var = StringVar()
        # self.contact_Var = StringVar()
        # self.dob_Var = StringVar()

        # ======manage frame========================
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink")
        manage_frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(manage_frame, text="Manage Students", bg="pink", fg="black",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(manage_frame, text="Roll no.", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(manage_frame, text="Name", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(manage_frame, text="Email", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(manage_frame, text="Gender", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(manage_frame, font=("times new roman", 14, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_contact = Label(manage_frame, text="Contact", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(manage_frame, text="D.O.B", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(manage_frame,  font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(manage_frame, text="Address", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address = Text(manage_frame, width=30, height=4, font=("", 10))
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # ======button frame=====
        btn_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="pink")
        btn_frame.place(x=10, y=500, width=420)

        Addbtn = Button(btn_frame, text="Add", width=10).grid(row=0, column=0, padx=10, pady=10)
        Updatebtn = Button(btn_frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_frame, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)

        # ======detail frame========================
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="pink")
        detail_frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(detail_frame, text="Search By", bg="pink", fg="black", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(detail_frame, width=20, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        Searchbtn = Button(detail_frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(detail_frame, text="Show All", width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

        # ============table frame=============
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="pink")
        table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        student_table = ttk.Treeview(table_frame,
                                     columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading("roll", text="Roll No.")
        student_table.heading("name", text="Name")
        student_table.heading("email", text="Email")
        student_table.heading("gender", text="Gender")
        student_table.heading("contact", text="Contact")
        student_table.heading("dob", text="D.O.B")
        student_table.heading("address", text="Address")
        student_table['show'] = 'headings'
        student_table.column("roll", width=100)
        student_table.column("email", width=100)
        student_table.column("gender", width=100)
        student_table.column("contact", width=100)
        student_table.column("dob", width=100)
        student_table.column("address", width=100)
        student_table.pack(fill=BOTH, expand=1)

# root=Tk()
# ob=Student(root)
# root.mainloop()