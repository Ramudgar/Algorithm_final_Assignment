
class User:
    def __init__(self, txt_fname, txt_lname,txt_Contact,txt_email,cmb_question,txt_answer,txt_pasw,txt_confirm):
        self.__FirstName=txt_fname
        self.__LastName=txt_lname
        self.__ContactNo=txt_Contact
        self.__EmailID=txt_email
        self.__Security_Question=cmb_question
        self.__Answer=txt_answer
        self.__Password=txt_pasw
        self.__Confirm_password=txt_confirm

    def set_FirstName(self,txt_fname):
        self.__FirstName=txt_fname

    def get_FirstName(self):
         return self.__FirstName

    def set_LastName(self,txt_lname):
        self.__LastName=txt_lname

    def get_LastName(self):
        return self.__LastName

    def set_ContactNo(self,txt_Contact):
        self.__ContactNo=txt_Contact

    def get_ContactNo(self):
        return self.__ContactNo

    def set_EmailID(self,txt_email):
        self.__EmailID=txt_email

    def get_EmailID(self):
        return self.__EmailID

    def set_Security_Question(self,cmb_question):
        self.__Security_Question=cmb_question

    def get_Security_Question(self):
        return self.__Security_Question

    def set_Answer(self,txt_answer):
        self.__Answer=txt_answer

    def get_Answer(self):
        return self.__Answer

    def set_Password(self,txt_pasw):
        self.__Password=txt_pasw

    def get_Password(self):
        return self.__Password

    def set_Confirm_password(self,txt_confirm):
        self.__Confirm_password=txt_confirm

    def get_Confirm_password(self):
        return self.__Confirm_password










