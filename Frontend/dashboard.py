from tkinter import *
from tkinter import ttk
import Models.dbdashboard
from tkinter import messagebox
import Backend.dbconnection
import time
import datetime


class Student:

    def __init__(self, root):
        ''' this method initialize the object '''

        self.root = root
        self.root.title("Student Ledger Management System")
        self.root.geometry("1350x700+0+0")

        self.db = Backend.dbconnection.DBConnect()

# == Title ==========================================
        title = Label(self.root, text="Student Record Maintinance", bd=10, relief=GROOVE,
                      font=("poopins", 40, "bold"), bg="#0C94DD", fg="white")
        title.pack(side=TOP, fill=X, padx=0, pady=20)



   # ====== Making frame ========================
        frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="#3BD8C1")
        frame1.place(x=20, y=100, width=450, height=580)


    # =============== Assigning Title===============

        Std_title = Label(frame1, text="Student Details", bg="#3BD8C1", fg="black",
                          font=("poopins", 30, "bold"))
        Std_title.grid(row=0,columnspan=2,ipadx=10, pady=20)

        # ======roll no label and entry======
        lbl_roll = Label(frame1, text="Roll no.", bg="#3BD8C1", fg="black", font=("Book Antiqua", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.txt_roll = Entry(frame1, font=("poopins", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # ======== name label and entry=========
        lbl_name = Label(frame1, text="Name", bg="#3BD8C1", fg="black", font=("Book Antiqua", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        self.txt_name = Entry(frame1, font=("poopins", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # ===== Email label and entry=========
        lbl_email = Label(frame1, text="Email", bg="#3BD8C1", fg="black", font=("Book Antiqua", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.txt_email = Entry(frame1, font=("poopins", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # ========= gender label and combo box=======
        lbl_gender = Label(frame1, text="Gender", bg="#3BD8C1", fg="black", font=("Book Antiqua", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.combo_gender = ttk.Combobox(frame1, font=("poopins", 14, "bold"), state='readonly')
        self.combo_gender['values'] = ("male", "female", "other")
        self.combo_gender.grid(row=4, column=1, padx=20, pady=10)

        # ============== contact label and entry================
        lbl_contact = Label(frame1, text="Contact", bg="#3BD8C1", fg="black", font=("Book Antiqua", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        self.txt_contact = Entry(frame1, font=("poopins", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # ================== dob label and entry====================
        lbl_dob = Label(frame1, text="D.O.B", bg="#3BD8C1", fg="black", font=("Book Antiqua", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.txt_dob = Entry(frame1, font=("poopins", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # ===address label and entry============
        lbl_address = Label(frame1, text="Address", bg="#3BD8C1", fg="black", font=("Book Antiqua", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Entry(frame1, width=30, font=("poopins", 10, "bold"))
        self.txt_address.grid(row=7, column=1, ipady=20, pady=10, padx=20, sticky="w")

        # ====== button frame =================
        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg="#3BD8C1")
        btn_frame.place(x=10, y=500, width=420)

        Btn_add = Button(btn_frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        Btn_update = Button(btn_frame, text="Update", command=self.update_data, width=10).grid(row=0, column=1, padx=10,
                                                                                               pady=10)
        Btn_delete = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                               pady=10)
        Btn_clear = Button(btn_frame, text="Clear", command=self.clear_data, width=10).grid(row=0, column=3, padx=10,
                                                                                            pady=10)

   # ======detail frame========================
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="#65DECC")
        detail_frame.place(x=500, y=100, width=900, height=580)



       #================ Combo box for sorting ===========================================================
        self.lbl_sort = Label(detail_frame, text="Sort By", bg="#65DECC", fg="black", font=("poopins", 12, "bold"))
        self.lbl_sort.grid(row=0, column=0, pady=10, padx=5, sticky="w")

        self.sort = ttk.Combobox(detail_frame,font=("poopins", 10, "bold"), state="readonly")
        self.sort['values'] = ['By Roll_No']
        self.sort.current()
        self.sort.grid(row=0, column=1, padx=5, pady=10)


        self.combo_sort = ttk.Combobox(detail_frame, font=("poopins", 10, "bold"),state='readonly')
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.current(0)
        self.combo_sort.grid(row=0, column=2, padx=20, pady=10)
        self.combo_sort.bind('<<ComboboxSelected>>',self.sorting)   # Event Handling metod is used


        # ========== search button and sort button=========

        self.txt_search = Entry(detail_frame, width=20, font=("poopins", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        Searchbtn = Button(detail_frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,
                              column=4,padx=10,pady=10)

        ViewAll_button = Button(detail_frame, text=" View All ", width=10, pady=5, command= self.fetch_data)\
            .grid(row=0, column=5, padx=10, pady=10)

# ============ Tree view table frame=================================

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="#65DECC")
        table_frame.place(x=10, y=70, width=760, height=500)


        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # ======== tree view diagram for heading==========
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

        # ======= column for tree view==========
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.Automatic)  # Event Handling
        self.fetch_data()


    # ===================== Function for Add button ===========================

    def add_student(self):
        '''
        THIS FUNCTION WILL INSERT VALUE IN DATABASE
        :return:data
        '''

        roll_no = self.txt_roll.get()
        name = self.txt_name.get()
        email = self.txt_email.get()
        gender = self.combo_gender.get()
        contact = self.txt_contact.get()
        dob = self.txt_dob.get()
        address = self.txt_address.get()

        u = Models.dbdashboard.Student(roll_no, name, email, gender, contact, dob, address)

        query = "insert into student(roll_no,name,email,gender,contact," \
                "dob,address) values(%s,%s,%s,%s,%s,%s,%s)"
        values = (
            u.get_roll_no(), u.get_name(), u.get_email(), u.get_gender(),
            u.get_contact(), u.get_dob(), u.get_address(),)

        self.db.insert(query, values)
        messagebox.showinfo('Success', 'User Registration successfull')

        self.fetch_data()
        self.clear_data()

    def fetch_data(self):
        '''
        This function help to fetch data in to tree view table form data stored in the database '''
        self.db = Backend.dbconnection.DBConnect()
        query = 'select * from student'
        rows = self.db.selectall(query)
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)

    def clear_data(self):
        '''
        This function will clear the data from the entry box
        :return:None
        '''
        self.txt_roll.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_email.delete(0, END)
        self.combo_gender.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_dob.delete(0, END)
        self.txt_address.delete(0, END)

    # ====================== fetch data in to the entry box from database ==========
    def Automatic(self, event):
        ''' this function will generates value in the entry bos of frame 1 '''
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']

        self.txt_roll.insert(0, row[0])
        self.txt_name.insert(0, row[1])
        self.txt_email.insert(0, row[2])
        self.combo_gender.insert(0, row[3])
        self.txt_contact.insert(0, row[4])
        self.txt_dob.insert(0, row[5])
        self.txt_address.insert(0, row[6])

    def update_data(self):
        """
        This function update data in the data base
        :return: updated values
        """
        roll_no = self.txt_roll.get()
        name = self.txt_name.get()
        email = self.txt_email.get()
        gender = self.combo_gender.get()
        contact = self.txt_contact.get()
        dob = self.txt_dob.get()
        address = self.txt_address.get()

        u = Models.dbdashboard.Student(roll_no, name, email, gender, contact, dob, address)

        query = "update student set name=%s,email=%s,gender=%s,contact=%s,\
                dob=%s,address=%s where roll_no = %s "
        values = (name, email, gender, contact, dob, address, roll_no)

        self.db.insert(query, values)
        messagebox.showinfo('Success', 'data updated successfully')
        self.fetch_data()
        self.clear_data()


    def delete_data(self):
        '''
        This function will delete value from the database and from the tree view also
        :return:none
        '''
        roll_no = self.txt_roll.get()
        name = self.txt_name.get()
        email = self.txt_email.get()
        gender = self.combo_gender.get()
        contact = self.txt_contact.get()
        dob = self.txt_dob.get()
        address = self.txt_address.get()

        self.db = Backend.dbconnection.DBConnect()
        u = Models.dbdashboard.Student(roll_no, name, email, gender, contact, dob, address)
        query = 'delete from student where roll_no = %s'
        values = (u.get_roll_no(),)

        self.db.insert(query, values)
        messagebox.showinfo('Success', 'selected data deleted successfully')
        self.fetch_data()
        self.clear_data()

    def search_data(self):
        '''
        This function will search data from the database and show in the tree view table
        :return:searched value
        '''
        # print("success")
        ent = self.txt_search.get()
        if ent != "":
            try:
                lis =[]

                for row in self.student_table.get_children():
                    rows = self.student_table.item(row)['values'][0]
                    lis.append(rows)
                # print(f"list={lis}")
                # print(lis)
                search = self.binarysearch(lis, int(self.txt_search.get()))
                print(f"search={search}")
                if search:
                    messagebox.showinfo("Sucess", "Found")
                    query = "select * from Student where roll_no = %s"
                    values = (search,)
                    rows = self.db.select(query, values)
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert('', END, values=row)



                else:
                    messagebox.showerror("failed", "Inserted Data,Not found")

            except:

                messagebox.showerror("Error", "Error in for loop")

    def binarysearch(self, lis, x):
        '''
        this will search the data by using binary search method while performing sort data
        :param lis: this is the list of avaliable data
        :param x: This is the input value
        :return:searched value
        '''

        start = 0
        end = len(lis) - 1
        while start <= end:
            middle = (start + end) // 2
            midpoint = lis[middle]
            if midpoint > x:
                end = middle - 1
            elif midpoint < x:
                start = middle + 1
            else:
                return midpoint


    def sorting(self,events):
        '''
        this will sort the data in  by using bubble sort method while performing sort data
        :param events: events is used for binding method
        :return:
        '''
        if self.sort.get() == "By Roll_No" and self.combo_sort.get() == "Ascending":
            query = "select * from student;"
            data = self.db.selectall(query)
            sort_val = []
            for values in data:
                sort_val.append(values)
            sorted_val = self.bubblesort_asc(sort_val)
            if len(sorted_val) != 0:
                messagebox.showinfo("Done","Data is sorted in the ascending order")
                self.student_table.delete(*self.student_table.get_children())
                for i in sorted_val:
                    self.student_table.insert('', END, values=i)

        elif self.sort.get() == "By Roll_No" and self.combo_sort.get() == "Descending":
            query = "select * from student;"
            data = self.db.selectall(query)
            sort_val = []
            for values in data:
                sort_val.append(values)
            sorted_val = self.bubblesort_desc(sort_val)
            if len(sorted_val) != 0:
                messagebox.showinfo("Done","Sorted Decreasing order")
                self.student_table.delete(*self.student_table.get_children())
                for i in sorted_val:
                    self.student_table.insert('', END, values=i)


    def bubblesort_asc(self, lis):
        ''' this will sort the data in ascending order by using bubble sort method while performing sort data'''

        for j in range(len(lis) - 1):
            for i in range(len(lis) - 1):
                if lis[i] > lis[i + 1]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
        return lis

    def bubblesort_desc(self, lis):
        """this will sort the data in descending order by using bubble sort method while performing sort data"""
        for j in range(len(lis) - 1):
            for i in range(len(lis) - 1):
                if lis[i] < lis[i + 1]:
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
        return lis





