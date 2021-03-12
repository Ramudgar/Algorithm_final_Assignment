
import unittest
from Models import user

class Test_User(unittest.TestCase):

    def setUp(self):
        self.e1 = user.User("Ram udgar", "Yadav_", "9811722711", "softwarica@gmail.com",
                            "Biratnagar", "Animal", "555555", "555555")

    def test_set_FirstName(self):
        self.e1.set_FirstName("Ram udgar")
        self.assertEqual("Ram udgar", self.e1.get_FirstName())

    def test_get_FirstName(self):
        self.assertEqual("Ram udgar", self.e1.get_FirstName())


    def test_set_LastName(self):
        self.e1.set_LastName("Yadav_")
        self.assertEqual("Yadav_", self.e1.get_LastName())
    def test_get_LastName(self):
        self.assertEqual("Yadav_", self.e1.get_LastName())

    def test_set_ContactNo(self):
        self.e1.set_ContactNo("9811722711")
        self.assertEqual("9811722711", self.e1.get_ContactNo())
    def test_get_ContactNo(self):
        self.assertEqual("9811722711", self.e1.get_ContactNo())


    def test_set_Email_ID(self):
        self.e1.set_Email_ID("softwarica@gmail.com")
        self.assertEqual("softwarica@gmail.com", self.e1.get_Email_ID())
    def test_get_Email_ID(self):
        self.assertEqual("softwarica@gmail.com", self.e1.get_Email_ID())


    def test_set_Security_Question(self):
        self.e1.set_Security_Question("Biratnagar")
        self.assertEqual("Biratnagar", self.e1.get_Security_Question())
    def test_get_Security_Question(self):
        self.assertEqual("Biratnagar", self.e1.get_Security_Question())


    def test_set_Answer(self):
        self.e1.set_Answer("Animal")
        self.assertEqual("Animal", self.e1.get_Answer())
    def test_get_Answer(self):
        self.assertEqual("Animal", self.e1.get_Answer())


    def test_set_Password_(self):
        self.e1.set_Password_("555555")
        self.assertEqual("555555", self.e1.get_Password_())
    #
    def test_get_Password_(self):
        self.assertEqual("555555", self.e1.get_Password_())

    def tearDown(self):
        self.e1 = None