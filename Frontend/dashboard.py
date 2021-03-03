from tkinter import *
import math, random, os
from tkinter import messagebox


class Bill_app:
    def __init__(self, bill):
        self.bill = bill
        self.bill.geometry("1350x700+0+0")
        self.bill.title("Billing software")
        bg_color = "#074463"
        title = Label(self.bill, text='Billing software', bd=12, relief=GROOVE, bg=bg_color, fg='white',
                      font=('times new roman', 30, 'bold'), pady=2).pack(fill=X)
        # ========Variablas=========
        # ========Fast_foods======
        self.chaumin = IntVar()
        self.momo = IntVar()
        self.mushroom = IntVar()
        self.noodle = IntVar()
        self.pastha = IntVar()
        self.egg = IntVar()
        # =====Grocery===
        self.Ice_cream = IntVar()
        self.coca_cola = IntVar()
        self.phanta = IntVar()
        self.sweet = IntVar()
        self.Milk = IntVar()
        self.curd = IntVar()
        # =======Dinner_items===
        self.biryani = IntVar()
        self.mutton = IntVar()
        self.rice = IntVar()
        self.vegetable = IntVar()
        self.vegeterian = IntVar()
        self.andakari = IntVar()
        # ==Total price and tax variable
        self.fast_food_price = StringVar()
        self.grocery_price = StringVar()
        self.dinner_price = StringVar()

        self.fast_food_tax = StringVar()
        self.grocery_tax = StringVar()
        self.dinner_tax = StringVar()
        # ======customer=====
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        # ======== customer details frame
        F1 = LabelFrame(self.bill, text='Customer Details', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'),
                        fg='gold', bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text='Customer Name', font=('times new roman', 18, 'bold')).grid(row=0, column=0, padx=20,
                                                                                               pady=5)
        cname_txt = Entry(F1, textvariable=self.c_name, width=15, bd=7, relief=SUNKEN, font='arial 15').grid(row=0,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=5)

        cphn_lbl = Label(F1, text='Customer phone no.', font=('times new roman', 18, 'bold')).grid(row=0, column=2,
                                                                                                   padx=20, pady=5)
        cphn_txt = Entry(F1, textvariable=self.c_phone, width=15, bd=7, relief=SUNKEN, font='arial 15').grid(row=0,
                                                                                                             column=3,
                                                                                                             padx=10,
                                                                                                             pady=5)

        c_bill_lbl = Label(F1, text='Bill number', font=('times new roman', 18, 'bold')).grid(row=0, column=4, padx=20,
                                                                                              pady=5)
        c_bill_txt = Entry(F1, textvariable=self.search_bill, width=15, bd=7, relief=SUNKEN, font='arial 15').grid(
            row=0, column=5, padx=10,
            pady=5)

        bill_btn = Button(F1, text="search", command=self.find_bill, width=10, bd=7, font='arial 12 bold').grid(row=0,
                                                                                                                column=6,
                                                                                                                padx=10,
                                                                                                                pady=10)

        # =========FAST_FOOD FRAME========
        F2 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Fast_foods', font=('times new roman', 15, 'bold'),
                        bg=bg_color, fg='gold')
        F2.place(x=5, y=170, width=325, height=360)

        chaumin_lbl = Label(F2, text='Chaumin', font=('times new roman', 16, 'bold'), bg=bg_color,
                            fg='light green').grid(row=0,
                                                   column=0, padx=10, pady=10, sticky='w')
        chaumin_lbl = Entry(F2, width=10, textvariable=self.chaumin, font=('times new roman', 16, 'bold'), bd=5,
                            relief=SUNKEN, ).grid(column=1,
                                                  row=0, padx=10, pady=10)
        momo_lbl = Label(F2, text='Fried_Momo', font=('times new roman', 16, 'bold'), bg=bg_color,
                         fg='light green').grid(row=1,
                                                column=0, padx=10, pady=10, sticky='w')
        momo_lbl = Entry(F2, width=10, textvariable=self.momo, font=('times new roman', 16, 'bold'), bd=5,
                         relief=SUNKEN).grid(column=1,
                                             row=1, padx=10, pady=10)
        mushroom_lbl = Label(F2, text='Mushroom_sauce', font=('times new roman', 16, 'bold'), bg=bg_color,
                             fg='light green').grid(row=2,
                                                    column=0, padx=10, pady=10, sticky='w')
        mushroom_lbl = Entry(F2, width=10, textvariable=self.mushroom,
                             font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, ).grid(column=1, row=2, padx=10,
                                                                                               pady=10)
        noodle_lbl = Label(F2, text='Fried_Noodle', font=('times new roman', 16, 'bold'), bg=bg_color,
                           fg='light green').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        noodle_lbl = Entry(F2, width=10, textvariable=self.noodle, font=('times new roman', 16, 'bold'),
                           bd=5, relief=SUNKEN, ).grid(column=1, row=3, padx=10, pady=10)
        pastha_lbl = Label(F2, text='Pastha', font=('times new roman', 16, 'bold'),
                           bg=bg_color, fg='light green').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        pastha_lbl = Entry(F2, width=10, textvariable=self.pastha, font=('times new roman', 16, 'bold'),
                           bd=5, relief=SUNKEN, ).grid(column=1, row=4, padx=10, pady=10)
        egg_lbl = Label(F2, text='Fried_Egg', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        egg_lbl = Entry(F2, width=10, textvariable=self.egg,
                        font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(column=1, row=5, padx=10,
                                                                                        pady=10)

        ##=====Grocery=========
        F3 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Grocery',
                        font=('times new roman', 15, 'bold'), bg=bg_color, fg='gold')
        F3.place(x=330, y=170, width=325, height=360)
        ice_lbl = Label(F3, text='Ice cream', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        ice_lbl = Entry(F3, width=10, textvariable=self.Ice_cream,
                        font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10,
                                                                                        pady=10)
        coc_lbl = Label(F3, text='Coca cola', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        coc_lbl = Entry(F3, width=10, textvariable=self.coca_cola, font=('times new roman', 16, 'bold'),
                        bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        phnta_lbl = Label(F3, text='Phanta', font=('times new roman', 16, 'bold'), bg=bg_color,
                          fg='light green').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        phnta_lbl = Entry(F3, width=10, textvariable=self.phanta, font=('times new roman', 16, 'bold'),
                          bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        swt_lbl = Label(F3, text='sweet', font=('times new roman', 16, 'bold'),
                        bg=bg_color, fg='light green').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        swt_lbl = Entry(F3, width=10, textvariable=self.sweet, font=('times new roman', 16, 'bold'),
                        bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        milk_lbl = Label(F3, text='Milk', font=('times new roman', 16, 'bold'),
                         bg=bg_color, fg='light green').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        milk_lbl = Entry(F3, width=10, textvariable=self.Milk, font=('times new roman', 16, 'bold'),
                         bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        curd_lbl = Label(F3, text='Curd', font=('times new roman', 16, 'bold'),
                         bg=bg_color, fg='light green').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        curd_lbl = Entry(F3, width=10, textvariable=self.curd, font=('times new roman', 16, 'bold'),
                         bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        ##Dinner items=====
        F4 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Dinner Items', font=('ties new roman', 14, 'bold'),
                        bg=bg_color, fg='gold')
        F4.place(x=635, y=170, width=325, height=360)
        D1_lbl = Label(F4, text='Chiken_Biryani', font=('times new roman', 16, 'bold'), bg=bg_color,
                       fg='light green').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        D1_lbl = Entry(F4, width=10, bd=5, textvariable=self.biryani, relief=SUNKEN,
                       font=('times new roman', 16, 'bold')).grid(row=0, column=1, padx=10, pady=10)
        D2_lbl = Label(F4, text='Mutton_Biryani', font=('times new roman', 16, 'bold'), bg=bg_color,
                       fg='light green').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        D2_lbl = Entry(F4, width=10, bd=5, textvariable=self.mutton, relief=SUNKEN,
                       font=('times new roman', 16, 'bold')).grid(row=1, column=1, padx=10, pady=10)
        D3_lbl = Label(F4, text='Fried_Rice', font=('times new roman', 16, 'bold'),
                       bg=bg_color, fg='light green').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        D3_lbl = Entry(F4, width=10, bd=5, textvariable=self.rice, relief=SUNKEN,
                       font=('times new roman', 16, 'bold')).grid(row=2, column=1, padx=10, pady=10)
        D4_lbl = Label(F4, text='Cooked_Vegetable', font=('times new roman', 16, 'bold'),
                       bg=bg_color, fg='light green').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        D4_lbl = Entry(F4, width=10, bd=5, textvariable=self.vegetable, relief=SUNKEN,
                       font=('times new roman', 16, 'bold')).grid(row=3, column=1, padx=10, pady=10)
        D5_lbl = Label(F4, text='Vegeterian_Food', font=('times new roman', 16, 'bold'), bg=bg_color,
                       fg='light green').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        D5_lbl = Entry(F4, width=10, bd=5, textvariable=self.vegeterian, relief=SUNKEN,
                       font=('times new roman', 16, 'bold')).grid(row=4, column=1, padx=10, pady=10)
        D6_lbl = Label(F4, text='Andakari', font=('times new roman', 16, 'bold'), bg=bg_color,
                       fg='light green').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        D6_lbl = Entry(F4, width=10, bd=5, textvariable=self.andakari, relief=SUNKEN,
                       font=('times new roman', 16, 'bold')).grid(row=5, column=1, padx=10, pady=10)

        ##========BIl Area==========
        F5 = Frame(self.bill, bd=10, relief=GROOVE)
        F5.place(x=1000, y=170, width=350, height=380)
        bill_title = Label(F5, text='Bill Area', font='arial 15 bold', bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        ##==========Button frame=======
        F6 = LabelFrame(self.bill, bd=10, relief=GROOVE, text='Bill menu', font=('times', 14, 'bold'), bg=bg_color,
                        fg='gold')
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text='Total Fast_food price', bg=bg_color, fg='white',
                       font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=20, pady=2)
        m1_txt = Entry(F6, bd=7, textvariable=self.fast_food_price, relief=SUNKEN,
                       font=('arial 10 bold')).grid(row=0, column=1, padx=20, pady=2)
        m2_lbl = Label(F6, text='Total Grocery price', bg=bg_color, fg='white',
                       font=('times new roman', 15, 'bold')).grid(row=1, column=0, padx=20, pady=2)
        m2_txt = Entry(F6, bd=7, relief=SUNKEN, textvariable=self.grocery_price,
                       font=('arial 10 bold')).grid(row=1, column=1, padx=20, pady=2)
        m3_lbl = Label(F6, text='Total Dinner_items price', bg=bg_color, fg='white',
                       font=('times new roman', 15, 'bold')).grid(row=2, column=0, padx=20, pady=2)
        m3_txt = Entry(F6, bd=7, relief=SUNKEN, textvariable=self.dinner_price,
                       font=('arial 10 bold')).grid(row=2, column=1, padx=20, pady=2)

        c1_lbl = Label(F6, text='Fast_food tax', bg=bg_color, fg='white',
                       font=('times new roman', 15, 'bold')).grid(row=0, column=2, padx=20, pady=2)
        c1_txt = Entry(F6, bd=7, textvariable=self.fast_food_tax, relief=GROOVE,
                       font=('arial 10 bold')).grid(row=0, column=3, padx=20, pady=2)
        c2_lbl = Label(F6, text='Grocery tax', bg=bg_color, fg='white',
                       font=('times new roman', 15, 'bold')).grid(row=1, column=2, padx=20, pady=2)
        c2_txt = Entry(F6, bd=7, textvariable=self.grocery_tax, relief=GROOVE,
                       font=('arial 10 bold')).grid(row=1, column=3, padx=20, pady=2)
        c3_lbl = Label(F6, text='Dinner_items tax', bg=bg_color, fg='white',
                       font=('times new roman', 15, 'bold')).grid(row=2, column=2, padx=20, pady=2)
        c3_txt = Entry(F6, bd=7, textvariable=self.dinner_tax, relief=GROOVE,
                       font=('arial 10 bold')).grid(row=2, column=3, padx=20, pady=2)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=750, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text='Total', width=11,
                           font=('arial 10 bold'), bg='cadetblue', fg='white', bd=2, relief=GROOVE, pady=15).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        GBill_btn = Button(btn_f, command=self.bill_area, text='Generate bill', width=11,
                           font=('arial 10 bold'), bg='cadetblue', fg='white', bd=2, relief=GROOVE, pady=15).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        Clear_btn = Button(btn_f, text='clear', command=self.clear_data, width=11,
                           font=('arial 10 bold'), bg='cadetblue', fg='white', bd=2, relief=GROOVE, pady=15).grid(row=0,
                                                                                                                  column=2,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        Exit_btn = Button(btn_f, text='Exit', command=self.Exit_data, width=11,
                          font=('arial 10 bold'), bg='cadetblue', fg='white', bd=2, relief=GROOVE, pady=15).grid(row=0,
                                                                                                                 column=3,
                                                                                                                 padx=5,
                                                                                                                 pady=5)
        self.welcome_bill()

    # =====Assigining the value===
    def total(self):
        self.chaumin_p = self.chaumin.get() * 30
        self.momo_p = self.momo.get() * 250
        self.mushroom_p = self.mushroom.get() * 300
        self.noodle_p = self.noodle.get() * 310
        self.egg_p = self.egg.get() * 150
        self.pastha_p = self.pastha.get() * 325

        self.total_fast_food_price = float(
            self.chaumin_p +
            self.momo_p +
            self.mushroom_p +
            self.noodle_p +
            self.egg_p +
            self.pastha_p
        )
        self.fast_food_price.set("Rs. " + str(self.total_fast_food_price))
        self.f_tax = round((self.total_fast_food_price * 0.05), 2)
        self.fast_food_tax.set("Rs. " + str(self.f_tax))

        self.i_c_p = self.Ice_cream.get() * 40
        self.m_p = self.Milk.get() * 70
        self.coc_p = self.coca_cola.get() * 45
        self.phanta_p = self.phanta.get() * 40
        self.curd_p = self.curd.get() * 80
        self.sweet_p = self.sweet.get() * 220

        self.total_grocery_price = float(
            self.i_c_p +
            self.m_p +
            self.coc_p +
            self.phanta_p +
            self.curd_p +
            self.sweet_p
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.1), 2)
        self.grocery_tax.set('Rs. ' + str(self.g_tax))

        self.biryani_p = self.biryani.get() * 40
        self.mutton_p = self.mutton.get() * 80
        self.rice_p = self.rice.get() * 60
        self.vegetable_p = self.vegetable.get() * 40
        self.vegeterian_p = self.vegeterian.get() * 55
        self.andakari_p = self.andakari.get() * 25

        self.total_dinner_price = float(
            self.biryani_p +
            self.mutton_p +
            self.rice_p +
            self.vegetable_p +
            self.vegeterian_p +
            self.andakari_p
        )
        self.dinner_price.set("Rs. " + str(self.total_dinner_price))
        self.d_tax = round((self.total_dinner_price * 0.05), 2)
        self.dinner_tax.set('Rs. ' + str(self.d_tax))

        self.total_bill = float(self.total_fast_food_price +
                                self.total_grocery_price +
                                self.total_dinner_price +
                                self.f_tax +
                                self.g_tax +
                                self.d_tax
                                )

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, '\t welcome bill Retail\n')
        self.textarea.insert(END, f'\n BILL NUMBER : {self.bill_no.get()}')
        self.textarea.insert(END, f'\n Customer Name : {self.c_name.get()}')
        self.textarea.insert(END, f'\n Phone Number : {self.c_phone.get()}')
        self.textarea.insert(END, f'\n =====================================')
        self.textarea.insert(END, f'\n products\t\tQTY\t\tprice')
        self.textarea.insert(END, f'\n =====================================')

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == '':
            messagebox.showerror("Error", "customer details are must")
        elif self.fast_food_price.get() == 'Rs. 0.0' and self.grocery_price.get() == 'Rs. 0.0' and self.dinner_price.get() == 'Rs. 0.0':
            messagebox.showerror('Errror', 'No product purchased')
        else:
            self.welcome_bill()
            ##====Fast_food itams=====
            if self.chaumin.get() != 0:
                self.textarea.insert(END, f'\n Chaumin\t\t{self.chaumin.get()}\t\t{self.chaumin_p}')
            if self.momo.get() != 0:
                self.textarea.insert(END, f'\n Fried_Momo\t\t{self.momo.get()}\t\t{self.momo_p}')
            if self.mushroom.get() != 0:
                self.textarea.insert(END, f'\n Mushroom_sauce\t\t{self.mushroom.get()}\t\t{self.mushroom_p}')
            if self.noodle.get() != 0:
                self.textarea.insert(END, f'\n Fried_Noodle\t\t{self.noodle.get()}\t\t{self.noodle_p}')
            if self.egg.get() != 0:
                self.textarea.insert(END, f'\n Fried_Egg \t\t{self.egg.get()}\t\t{self.egg_p}')
            if self.pastha.get() != 0:
                self.textarea.insert(END, f'\n Pastha\t\t{self.pastha.get()}\t\t{self.pastha_p}')
                # =====grocery====
            if self.Ice_cream.get() != 0:
                self.textarea.insert(END, f'\n Ice_Cream\t\t{self.Ice_cream.get()}\t\t{self.i_c_p}')
            if self.Milk.get() != 0:
                self.textarea.insert(END, f'\n Milk\t\t{self.Milk.get()}\t\t{self.m_p}')
            if self.sweet.get() != 0:
                self.textarea.insert(END, f'\n Sweet\t\t{self.sweet.get()}\t\t{self.sweet_p}')
            if self.curd.get() != 0:
                self.textarea.insert(END, f'\n Curd\t\t{self.curd.get()}\t\t{self.curd_p}')
            if self.phanta.get() != 0:
                self.textarea.insert(END, f'\n Phanta \t\t{self.phanta.get()}\t\t{self.phanta_p}')
            if self.coca_cola.get() != 0:
                self.textarea.insert(END, f'\n Coco Cola\t\t{self.coca_cola.get()}\t\t{self.coc_p}')
                # =====Dinner Itema=====
            if self.biryani.get() != 0:
                self.textarea.insert(END, f'\n Chicken_Biryani\t\t{self.biryani.get()}\t\t{self.biryani_p}')
            if self.mutton.get() != 0:
                self.textarea.insert(END, f'\n Mutton\t\t{self.mutton.get()}\t\t{self.mutton_p}')
            if self.rice.get() != 0:
                self.textarea.insert(END, f'\n Fried_rice\t\t{self.rice.get()}\t\t{self.rice_p}')
            if self.vegetable.get() != 0:
                self.textarea.insert(END, f'\n Cooked_vegetable\t\t{self.vegetable.get()}\t\t{self.vegetable_p}')
            if self.vegeterian.get() != 0:
                self.textarea.insert(END, f'\n Vegeterian_Food \t\t{self.vegeterian.get()}\t\t{self.vegeterian_p}')
            if self.andakari.get() != 0:
                self.textarea.insert(END, f'\n Andakari\t\t{self.andakari.get()}\t\t{self.andakari_p}')

            self.textarea.insert(END, f'\n ------------------------------------')
            if self.fast_food_tax.get() != 'Rs. 0.0':
                self.textarea.insert(END, f'\n Fast_Food tax\t\t\t{self.fast_food_tax.get()}')
            if self.grocery_tax.get() != 'Rs. 0.0':
                self.textarea.insert(END, f'\n Grocery tax\t\t\t{self.grocery_tax.get()}')
            if self.dinner_tax.get() != 'Rs. 0.0':
                self.textarea.insert(END, f'\n Dinner_items tax\t\t\t{self.dinner_tax.get()}')
            self.textarea.insert(END, f'\n Total bill:\t\t\tRs.{self.total_bill}')
            self.textarea.insert(END, f'\n -----------------------------------')
            self.save_bill()

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

    def clear_data(self):
        Ram = messagebox.askyesno('Clear', 'Do you really want to clear data?')
        if Ram > 0:
            # ========cosmetics======
            self.chaumin.set(0)
            self.momo.set(0)
            self.mushroom.set(0)
            self.noodle.set(0)
            self.egg.set(0)
            self.pastha.set(0)
            # =====Grocery===
            self.Ice_cream.set(0)
            self.coca_cola.set(0)
            self.phanta.set(0)
            self.sweet.set(0)
            self.Milk.set(0)
            self.curd.set(0)
            # =======Vegetable===
            self.biryani.set(0)
            self.mutton.set(0)
            self.rice.set(0)
            self.vegetable.set(0)
            self.vegeterian.set(0)
            self.andakari.set(0)
            # ==Total price and tax variable
            self.fast_food_price.set('')
            self.grocery_price.set('')
            self.dinner_price.set('')

            self.fast_food_tax.set('')
            self.grocery_tax.set('')
            self.dinner_tax.set('')
            # ======customer=====
            self.c_name.set('')
            self.c_phone.set('')
            self.bill_no.set('')
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set('')
            self.welcome_bill()

    def Exit_data(self):
        Ram = messagebox.askyesno('Exit', 'Do you really want to exit data?')
        if Ram > 0:
            self.bill.destroy()
