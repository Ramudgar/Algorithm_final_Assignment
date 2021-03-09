
class Student:


    def __init__(self, txt_roll, txt_name, combo_gender, txt_email, txt_contact, txt_dob,txt_address):
        self.__roll_no = txt_roll
        self.__name = txt_name
        self.__email = txt_email
        self.__gender = combo_gender
        self.__contact = txt_contact
        self.__dob = txt_dob
        self.__address=txt_address



    def set_roll_no(self, txt_roll):
        self.__roll_no = txt_roll

    def get_roll(self):
        return self.__roll_no

    def set_name(self, txt_name):
        self.__name = txt_name

    def get_name(self):
        return self.__name

    def set_email(self, txt_email):
        self.__email = txt_email

    def get_email(self):
        return self.__email

    def set_gender(self, combo_gender):
        self.__gender = combo_gender

    def get_gender(self):
        return self.__gender

    def set_contact(self, txt_contact):
        self.__contact = txt_contact

    def get_contact(self):
        return self.__contact

    def set_dob(self, txt_dob):
        self.__dob = txt_dob

    def get_dob(self):
        return self.__dob

    def set_address(self, txt_address):
        self.__address = txt_address

    def get_address(self):
        return self.__address




