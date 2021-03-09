
class Student:


    def __init__(self, roll_no, name, email,combo_gender,contact, dob,address):
        self.__roll_no = roll_no
        self.__name = name
        self.__email = email
        self.__gender = combo_gender
        self.__contact = contact
        self.__dob = dob
        self.__address=address



    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def get_roll_no(self):
        return self.__roll_no

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_gender(self, combo_gender):
        self.__gender = combo_gender

    def get_gender(self):
        return self.__gender

    def set_contact(self, contact):
        self.__contact = contact

    def get_contact(self):
        return self.__contact

    def set_dob(self, dob):
        self.__dob = dob

    def get_dob(self):
        return self.__dob

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address




