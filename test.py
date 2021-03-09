from tkinter import *
import math, random,os
from tkinter import messagebox
#import Backend.dbconnection
import Models.dbdashboard


class Bill_app:
    def __init__(self, bill):
        self.bill = bill
        self.bill.geometry("1350x700+0+0")
        self.bill.title("Billing software")
        bg_color = "#074463"

        #self.db = Backend.dbconnection.DBConnect()

        title = Label(self.bill, text='Billing software', bd=12, relief=GROOVE, bg=bg_color, fg='white',
                      font=('times new roman', 30, 'bold'), pady=2).pack(fill=X)



        # ======Bill No================================
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # ======== customer details frame
        F1 = LabelFrame(self.bill, text='Customer Details', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        fg='gold', bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        # =======================Customer name=======================================
        cname_lbl = Label(F1, text='Customer Name', font=('times new roman', 18, 'bold')).grid(row=0, column=0, padx=20,
                                                                                               pady=5)
        self.cname_ent = Entry(F1, font=("times new roman", 15), width=15, bd=7, relief=SUNKEN)
        self.cname_ent.grid(row=0, column=1, padx=10, pady=5)

        # ===========================   Phone number  =======================================
        cphone_lbl = Label(F1, text='Customer phone no.', font=('times new roman', 18, 'bold')).grid(row=0, column=2,
                                                                                                     padx=20, pady=5)
        self.cphone_ent = Entry(F1, font=("times new roman", 15), width=15, bd=7, relief=SUNKEN)
        self.cphone_ent.grid(row=0, column=3,padx=10,pady=5)

        # ===============================    Bill entry       ====================
        c_bill_lbl = Label(F1, text='Bill number', font=('times new roman', 18, 'bold')).grid(row=0, column=4, padx=20,
                                                                                              pady=5)
        self.bill_ent = Entry(F1, font=("times new roman", 15), width=15, bd=7, relief=SUNKEN)
        self.bill_ent.grid(row=0, column=5, padx=10,pady=5)

        # ============================ Making search Button =========================================
        bill_btn = Button(F1, text="search", command=self.find_bill, width=10, bd=7,
                          font='arial 12 bold').grid(row=0,  column=6,  padx=10,  pady=10)

        # =========FAST_FOOD FRAME========
        F2 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Fast_foods', font=('times new roman', 15, 'bold'),
                        bg=bg_color, fg='gold')
        F2.place(x=5, y=170, width=325, height=360)

        # =============chaumin==============
        chaumin_lbl = Label(F2, text='Chaumin', font=('times new roman', 16, 'bold'), bg=bg_color,
                            fg='light green').grid(row=0,column=0, padx=10, pady=10, sticky='w')

        self.chaumin_ent = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN )
        self.chaumin_ent.grid(column=1, row=0, padx=10, pady=10)

        # ==============momo=====================================
        momo_lbl = Label(F2, text='Fried_Momo', font=('times new roman', 16, 'bold'), bg=bg_color,
                         fg='light green').grid(row=1,
                                                column=0, padx=10, pady=10, sticky='w')

        self.momo_ent = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN)
        self.momo_ent.grid(column=1, row=1, padx=10, pady=10)

        # ====================mushroom========================
        mushroom_lbl = Label(F2, text='Mushroom_sauce', font=('times new roman', 16, 'bold'), bg=bg_color,
                             fg='light green').grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.mushroom_ent = Entry(F2, width=10,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN )
        self.mushroom_ent.grid(column=1, row=2,padx=10,pady=10)

        # =====================noodle===================================
        noodle_lbl = Label(F2, text='Fried_Noodle', font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='light green').grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.noodle_ent = Entry(F2, width=10, font=('times new roman', 16, 'bold'),bd=5, relief=SUNKEN)
        self.noodle_ent.grid(column=1, row=3, padx=10, pady=10)

        # =======================pastha================================
        pastha_lbl = Label(F2, text='Pastha', font=('times new roman', 16, 'bold'),
                           bg=bg_color, fg='light green').grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.pastha_ent = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN )
        self.pastha_ent.grid(column=1, row=4, padx=10, pady=10)

        # ===========================egg==================================
        egg_lbl = Label(F2, text='Fried_Egg', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=5, column=0, padx=10, pady=10, sticky='w')

        self.egg_ent = Entry(F2, width=10,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN)
        self.egg_ent.grid(column=1, row=5, padx=10,pady=10)

        ##=====Grocery Frame====================================================================
        F3 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Grocery',
                        font=('times new roman', 15, 'bold'), bg=bg_color, fg='gold')
        F3.place(x=330, y=170, width=325, height=360)

        # ===========================ice=======================================================
        ice_lbl = Label(F3, text='Ice cream', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.ice_ent = Entry(F3, width=10,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN)
        self.ice_ent .grid(row=0, column=1, padx=10,pady=10)

        # =====================================cocacola=========================================
        coc_lbl = Label(F3, text='Coca cola', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.coc_ent = Entry(F3, width=10, font=('times new roman', 16, 'bold'),bd=5, relief=SUNKEN)
        self.coc_ent.grid(row=1, column=1, padx=10, pady=10)

        # =======================================phanta=======================================
        phanta_lbl = Label(F3, text='Phanta', font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='light green').grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.phanta_ent = Entry(F3, width=10, font=('times new roman', 16, 'bold'),bd=5, relief=SUNKEN)
        self.phanta_ent.grid(row=2, column=1, padx=10, pady=10)

        # ==================================sweet=========================================================
        swt_lbl = Label(F3, text='sweet', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.swt_ent = Entry(F3, width=10, font=('times new roman', 16, 'bold'),bd=5, relief=SUNKEN)
        self.swt_ent.grid(row=3, column=1, padx=10, pady=10)

        # ==============================milk==============================================
        milk_lbl = Label(F3, text='Milk', font=('times new roman', 16, 'bold'),
                         bg=bg_color, fg='light green').grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.milk_ent = Entry(F3, width=10, font=('times new roman', 16, 'bold'),bd=5, relief=SUNKEN)
        self.milk_ent.grid(row=4, column=1, padx=10, pady=10)

        # ==================================curd======================================
        curd_lbl = Label(F3, text='Curd', font=('times new roman', 16, 'bold'),
                         bg=bg_color, fg='light green').grid(row=5, column=0, padx=10, pady=10, sticky='w')

        self.curd_ent = Entry(F3, width=10, font=('times new roman', 16, 'bold'),bd=5, relief=SUNKEN)
        self.curd_ent.grid(row=5, column=1, padx=10, pady=10)

        # ====Dinner items========================================================================
        F4 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Dinner Items', font=('ties new roman', 14, 'bold'),
                        bg=bg_color, fg='gold')
        F4.place(x=635, y=170, width=325, height=360)

        # ===========================chiken======================================
        chiken_lbl = Label(F4, text='Chiken_Biryani', font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='light green').grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.chiken_ent = Entry(F4, width=10, bd=5, relief=SUNKEN,font=('times new roman', 16, 'bold'))
        self.chiken_ent.grid(row=0, column=1, padx=10, pady=10)

        # ====================================Mutton=========================================
        mutton_lbl = Label(F4, text='Mutton_Biryani', font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='light green').grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.mutton_ent = Entry(F4, width=10, bd=5, relief=SUNKEN,font=('times new roman', 16, 'bold'))
        self.mutton_ent.grid(row=1, column=1, padx=10, pady=10)

        # =============================Fried rice==========================================
        fried_lbl = Label(F4, text='Fried_Rice', font=('times new roman', 16, 'bold'),
                          bg=bg_color, fg='light green').grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.fried_ent = Entry(F4, width=10, bd=5, relief=SUNKEN,font=('times new roman', 16, 'bold'))
        self.fried_ent.grid(row=2, column=1, padx=10, pady=10)

        # ============================cooked_vegetable================================
        cook_lbl = Label(F4, text='Cooked_Vegetable', font=('times new roman', 16, 'bold'),
                         bg=bg_color, fg='light green').grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.cook_ent = Entry(F4, width=10, bd=5, relief=SUNKEN,font=('times new roman', 16, 'bold'))
        self.cook_ent.grid(row=3, column=1, padx=10, pady=10)

        # ===================================Vegeterain food==================================
        veg_lbl = Label(F4, text='Vegeterian_Food', font=('times new roman', 16, 'bold'), bg=bg_color,
                        fg='light green').grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.veg_ent = Entry(F4, width=10, bd=5, relief=SUNKEN,font=('times new roman', 16, 'bold'))
        self.veg_ent.grid(row=4, column=1, padx=10, pady=10)

        # ====================================Andakari===================================
        Andakari_lbl = Label(F4, text='Andakari', font=('times new roman', 16, 'bold'), bg=bg_color,
                             fg='light green').grid(row=5, column=0, padx=10, pady=10, sticky='w')

        self.andakari_ent = Entry(F4, width=10, bd=5, relief=SUNKEN,font=('times new roman', 16, 'bold'))
        self.andakari_ent.grid(row=5, column=1, padx=10, pady=10)

        ##========BIl Area==========
        F5 = Frame(self.bill, bd=10, relief=GROOVE)
        F5.place(x=1000, y=170, width=350, height=380)
        bill_title = Label(F5, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # =====Button frame=====================================================================
        F6 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Bill menu', font=('times', 14, 'bold'), bg=bg_color,
                        fg='gold')
        F6.place(x=0, y=560, relwidth=1, height=140)

        # ==========================total fast food Label =====================================
        fast_lbl = Label(F6, text='Total Fast_food price', bg=bg_color, fg='white',
                         font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=20, pady=2)

        self.fast_ent = Entry(F6, bd=7, relief=SUNKEN,font=('arial 10 bold'))
        self.fast_ent .grid(row=0, column=1, padx=20, pady=2)

        # ======================================total grocery price===============================
        groc_lbl = Label(F6, text='Total Grocery price', bg=bg_color, fg='white',
                         font=('times new roman', 15, 'bold')).grid(row=1, column=0, padx=20, pady=2)

        self.groc_ent = Entry(F6, bd=7, relief=SUNKEN,font=('arial 10 bold'))
        self.groc_ent.grid(row=1, column=1, padx=20, pady=2)

        # =============================total Dinner price============================
        din_lbl = Label(F6, text='Total Dinner_items price', bg=bg_color, fg='white',
                        font=('times new roman', 15, 'bold')).grid(row=2, column=0, padx=20, pady=2)

        self.din_ent = Entry(F6, bd=7, relief=SUNKEN,font=('arial 10 bold'))
        self.din_ent.grid(row=2, column=1, padx=20, pady=2)

        # ====Tax=====================================================

        # ==============================fast food tax=======================
        tax_fast_lbl = Label(F6, text='Fast_food tax', bg=bg_color, fg='white',
                             font=('times new roman', 15, 'bold')).grid(row=0, column=2, padx=20, pady=2)

        self.tax_fast_ent = Entry(F6, bd=7, relief=GROOVE,font=('arial 10 bold'))
        self.tax_fast_ent.grid(row=0, column=3, padx=20, pady=2)

        # ===========================Grocery tax=========================
        tax_groc_lbl = Label(F6, text='Grocery tax', bg=bg_color, fg='white',
                             font=('times new roman', 15, 'bold')).grid(row=1, column=2, padx=20, pady=2)

        self.tax_groc_ent = Entry(F6, bd=7, relief=GROOVE,font=('arial 10 bold'))
        self.tax_groc_ent.grid(row=1, column=3, padx=20, pady=2)

        # =========================Dinner item tax=========================
        tax_din_lbl = Label(F6, text='Dinner_items tax', bg=bg_color, fg='white',
                            font=('times new roman', 15, 'bold')).grid(row=2, column=2, padx=20, pady=2)

        self.tax_din_ent = Entry(F6, bd=7, relief=GROOVE,font=('arial 10 bold'))
        self.tax_din_ent.grid(row=2, column=3, padx=20, pady=2)

        # ====Button=========================================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=750, width=580, height=105)

        # ==Button=====================================================================

        # ===============Total Button=============================================
        total_btn = Button(btn_f, command=self.total, text='Total', width=11,font=('arial 10 bold'), bg='cadetblue',
            fg='white', bd=2, relief=GROOVE, pady=15).grid(row=0, column=0, padx=5,pady=5)

        # ============================Generate Bill Button==================================
        GBill_btn = Button(btn_f, command=self.bill_area, text='Generate bill', width=11,
                           font=('arial 10 bold'), bg='cadetblue', fg='white', bd=2, relief=GROOVE,
                           pady=15).grid(row=0,column=1,padx=5,pady=5)

        # ======================Clear Button============================================
        Clear_btn = Button(btn_f, text='clear', command=self.clear_data, width=11,
                           font=('arial 10 bold'), bg='cadetblue', fg='white', bd=2, relief=GROOVE, pady=15).grid(row=0,column=2,padx=5,pady=5)

        # ========================================Exit Button===================================
        Exit_btn = Button(btn_f, text='Exit', command=self.Exit_data, width=11,font=('arial 10 bold'), bg='cadetblue',
                          fg='white', bd=2, relief=GROOVE, pady=15).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    # =====Assigining the total value======================================================
    def total(self):
        # # ============== variable fetches from Models.dbdashboard =========================
        self.chaumin = self.chaumin_ent.get()
        self.momo = self.momo_ent.get()
        self.mushroom = self.mushroom_ent.get()
        self.noodle = self.noodle_ent.get()
        self.pastha = self.pastha_ent.get()
        self.egg = self.egg_ent.get()
        # =====Grocery===
        self.Ice_cream = self.ice_ent.get()
        self.coca_cola = self.coc_ent.get()
        self.phanta = self.phanta_ent.get()
        self.sweet = self.swt_ent.get()
        self.Milk = self.milk_ent.get()
        self.curd = self.curd_ent.get()
        # =======Dinner_items===
        self.Chicken_Biryani = self.chiken_ent.get()
        self.Mutton_Biryani = self.mutton_ent.get()
        self.Fried_rice = self.fried_ent.get()
        self.Cooked_vegetable = self.cook_ent.get()
        self.vegeterian = self.veg_ent.get()
        self.Andakari = self.andakari_ent.get()

        # ======customer=====
        self.c_name = self.cname_ent.get()
        self.c_phone = self.cphone_ent.get()
        self.bill_no = self.bill_ent.get()
        # =============== total price Item ============
        self.fast_food_price = self.fast_ent.get()
        self.grocery_price = self.groc_ent.get()
        self.dinner_price = self.din_ent.get()
        # ============== total tax ==================
        self.fast_food_tax = self.tax_fast_ent.get()
        self.grocery_tax = self.tax_groc_ent.get()
        self.dinner_tax = self.tax_din_ent.get()

        u = Models.dbdashboard.Hotel(self.chaumin, self.momo, self.mushroom, self.noodle, self.pastha, self.egg,
                                     self.egg, self.Ice_cream, self.coca_cola, self.phanta, self.sweet, self.Milk,
                                     self.curd, self.Chicken_Biryani,
                                     self.Mutton_Biryani, self.Fried_rice, self.Cooked_vegetable, self.vegeterian,
                                     self.Andakari, self.c_name, self.c_phone, self.bill_no,
                                     self.fast_food_price, self.grocery_price, self.dinner_price, self.fast_food_tax,
                                     self.grocery_tax)

        query = "insert into Hotel(FirstName,LastName,ContactNo,Email_ID,Security_Question," \
                "Answer,Password_,Confirm_password) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (u.get_chaumin(),)
        #print(values)
        self.db.insert(query, values)
        messagebox.showinfo('Success', 'User Registration successfull')
        #self.bill.destroy()

        self.chaumin_p = self.chaumin * 30
        self.momo_p = self.momo * 250
        self.mushroom_p = self.mushroom * 300
        self.noodle_p = self.noodle * 310
        self.egg_p = self.egg * 150
        self.pastha_p = self.pastha * 325

        self.total_fast_food_price = float(
            self.chaumin_p +
            self.momo_p +
            self.mushroom_p +
            self.noodle_p +
            self.egg_p +
            self.pastha_p
        )
        # self.fast_ent.set("Rs. " + str(self.total_fast_food_price))
        # self.f_tax = round((self.total_fast_food_price * 0.05), 2)
        # self.tax_fast_ent.set("Rs. " + str(self.f_tax))
        self.f_tax = self.total_fast_food_price * 0.05

        self.i_c_p = self.Ice_cream * 40
        self.m_p = self.Milk * 70
        self.coc_p = self.coca_cola * 45
        self.phanta_p = self.phanta * 40
        self.curd_p = self.curd * 80
        self.sweet_p = self.sweet * 220

        self.total_grocery_price = float(
            self.i_c_p +
            self.m_p +
            self.coc_p +
            self.phanta_p +
            self.curd_p +
            self.sweet_p
        )
        # self.groc_ent.set("Rs. " + str(self.total_grocery_price))
        # self.g_tax = round((self.total_grocery_price * 0.1), 2)
        # self.tax_groc_ent.set('Rs. ' + str(self.g_tax))
        self.g_tax =self.total_grocery_price * 0.1

        self.biryani_p = self.Chicken_Biryani * 40
        self.mutton_p = self.Mutton_Biryani * 80
        self.rice_p = self.Fried_rice * 60
        self.vegetable_p = self.Cooked_vegetable * 40
        self.vegeterian_p = self.vegeterian * 55
        self.andakari_p = self.Andakari * 25

        self.total_dinner_price = float(
            self.biryani_p +
            self.mutton_p +
            self.rice_p +
            self.vegetable_p +
            self.vegeterian_p +
            self.andakari_p
        )
        # self.din_ent.set("Rs. " + str(self.total_dinner_price))
        # self.d_tax = round("Rs. "+(self.total_dinner_price * 0.05), 2)
        # self.tax_din_ent.set('Rs. ' + str(self.d_tax))
        self.d_tax =self.total_dinner_price * 0.05

        self.total_bill = float(self.total_fast_food_price +
                                self.total_grocery_price +
                                self.total_dinner_price+
                                 self.f_tax +
                                 self.g_tax +
                                self.d_tax
                                )

    # ==========creating bill information====================================
    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, '\t welcome bill Retail\n')
        self.textarea.insert(END, f'\n BILL NUMBER : {self.bill_no}')
        self.textarea.insert(END, f'\n Customer Name : {self.c_name()}')
        self.textarea.insert(END, f'\n Phone Number : {self.c_phone}')
        self.textarea.insert(END, f'\n =====================================')
        self.textarea.insert(END, f'\n products\t\tQTY\t\tprice')
        self.textarea.insert(END, f'\n =====================================')

    # ===========================Getting information in the bill area====================
    def bill_area(self):
        if self.c_name == "" or self.c_phone == '':
            messagebox.showerror("Error", "customer details are must")
        elif self.fast_food_price == 'Rs. 0.0' and self.grocery_price == 'Rs. 0.0' and self.dinner_price == 'Rs. 0.0':
            messagebox.showerror('Errror', 'No product purchased')
        else:
            self.welcome_bill()

            ##=====================================Getting value of Fast_food items======================
            if self.chaumin != 0:
                self.textarea.insert(END, f'\n Chaumin\t\t{self.chaumin}\t\t{self.chaumin_p}')
            if self.momo != 0:
                self.textarea.insert(END, f'\n Fried_Momo\t\t{self.momo}\t\t{self.momo_p}')
            if self.mushroom != 0:
                self.textarea.insert(END, f'\n Mushroom_sauce\t\t{self.mushroom}\t\t{self.mushroom_p}')
            if self.noodle != 0:
                self.textarea.insert(END, f'\n Fried_Noodle\t\t{self.noodle}\t\t{self.noodle_p}')
            if self.egg != 0:
                self.textarea.insert(END, f'\n Fried_Egg \t\t{self.egg}\t\t{self.egg_p}')
            if self.pastha != 0:
                self.textarea.insert(END, f'\n Pastha\t\t{self.pastha}\t\t{self.pastha_p}')

            # ==========================getting value of grocery Items=================================
            if self.Ice_cream != 0:
                self.textarea.insert(END, f'\n Ice_Cream\t\t{self.Ice_cream}\t\t{self.i_c_p}')
            if self.Milk != 0:
                self.textarea.insert(END, f'\n Milk\t\t{self.Milk}\t\t{self.m_p}')
            if self.sweet != 0:
                self.textarea.insert(END, f'\n Sweet\t\t{self.sweet}\t\t{self.sweet_p}')
            if self.curd != 0:
                self.textarea.insert(END, f'\n Curd\t\t{self.curd}\t\t{self.curd_p}')
            if self.phanta != 0:
                self.textarea.insert(END, f'\n Phanta \t\t{self.phanta}\t\t{self.phanta_p}')
            if self.coca_cola != 0:
                self.textarea.insert(END, f'\n Coco Cola\t\t{self.coca_cola}\t\t{self.coc_p}')

            # =============================Getting value of Dinner Items=========================
            if self.Chicken_Biryani != 0:
                self.textarea.insert(END, f'\n Chicken_Biryani\t\t{self.Chicken_Biryani}\t\t{self.biryani_p}')
            if self.Mutton_Biryani != 0:
                self.textarea.insert(END, f'\n Mutton\t\t{self.Mutton_Biryani}\t\t{self.mutton_p}')
            if self.Fried_rice != 0:
                self.textarea.insert(END, f'\n Fried_rice\t\t{self.Fried_rice}\t\t{self.rice_p}')
            if self.Cooked_vegetable != 0:
                self.textarea.insert(END, f'\n Cooked_vegetable\t\t{self.Cooked_vegetable}\t\t{self.vegetable_p}')
            if self.vegeterian != 0:
                self.textarea.insert(END, f'\n Vegeterian_Food \t\t{self.vegeterian}\t\t{self.vegeterian_p}')
            if self.Andakari != 0:
                self.textarea.insert(END, f'\n Andakari\t\t{self.Andakari}\t\t{self.andakari_p}')

            self.textarea.insert(END, f'\n ------------------------------------')
            if self.fast_food_tax != 'Rs. 0.0':
                self.textarea.insert(END, f'\n Fast_Food tax\t\t\t{self.fast_food_tax}')
            if self.tax_groc_ent.get() != 'Rs. 0.0':
                self.textarea.insert(END, f'\n Grocery tax\t\t\t{self.grocery_tax}')
            if self.dinner_tax != 'Rs. 0.0':
                self.textarea.insert(END, f'\n Dinner_items tax\t\t\t{self.dinner_tax}')
            self.textarea.insert(END, f'\n Total bill:\t\t\tRs.{self.total_bill}')
            self.textarea.insert(END, f'\n -----------------------------------')
            self.save_bill()

    # ===================================saving data ========================================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.textarea.get('1.0', END)
            R1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            R1.write(self.bill_data)
            R1.close()
            messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} saved Sucessfully!")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                R1 = open(f'bills/{i}', 'r')
                self.textarea.delete('1.0', END)
                for d in R1:
                    self.textarea.insert(END, d)
                R1.close()
                present = "yes"
            if present == "no":
                messagebox.showerror("Error", "Invalid Bill No.")

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------++
    #
    def clear_data(self):
        Ram = messagebox.askyesno('Clear', 'Do you really want to clear data?')
        if Ram > 0:
            # ========cosmetics======
            self.chaumin_ent = ''
            self.momo_ent =''
            self.mushroom_ent =''
            self.noodle_ent =''
            self.egg_ent =''
            self.pastha_ent =''
            # =====Grocery===
            self.ice_ent =''
            self.coc_ent=''
            self.phanta_ent =''
            self.swt_ent =''
            self.milk_ent =''
            self.curd_ent=''
            # =======Vegetable===
            self.chiken_ent=''
            self.mutton_ent=''
            self.fried_ent=''
            self.cook_ent=''
            self.veg_ent=''
            self.andakari_ent=''
            # ==Total price and tax variable
            self.fast_ent=''
            self.groc_ent=''
            self.din_ent=''

            self.tax_fast_ent=''
            self.tax_groc_ent=''
            self.tax_fast_ent=''
            # ======customer=====
            self.cname_ent=''
            self.cphone_ent=''
            self.bill_no=''
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill=''
            self.welcome_bill()

    def Exit_data(self):
        Ram = messagebox.askyesno('Exit', 'Do you really want to exit data?')
        if Ram > 0:
            self.bill.destroy()

bill=Tk()
obj=Bill_app(bill)
bill.mainloop()
