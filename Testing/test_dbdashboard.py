import unittest
from Models import dbdashboard


class Test_Student(unittest.TestCase):

    def setUp(self):
        '''Hook method for setting up the test fixture before exercising it.'''
        self.ram = dbdashboard.Student ("11111", "Yadav12", "fmal11", "mail11", "98203011", "1990-02-9", "sarlahi11",)

    def test_set_roll_no(self):
        self.ram.set_roll_no("11111")
        self.assertEqual("11111", self.ram.get_roll_no())

    def test_get_roll_no(self):
        self.assertEqual("11111", self.ram.get_roll_no())

    def test_set_name(self):
        self.ram.set_name("Yadav12")
        self.assertEqual("Yadav12", self.ram.get_name())

    def test_get_name(self):
        self.assertEqual("Yadav12", self.ram.get_name())

    def test_set_email(self):
        self.ram.set_email("fmal11")
        self.assertEqual("fmal11", self.ram.get_email())

    def test_get_email(self):
        self.assertEqual("fmal11", self.ram.get_email())

    def test_set_gender(self):
        self.ram.set_gender("mail11")
        self.assertEqual("mail11", self.ram.get_gender())

    def test_get_gender(self):
        self.assertEqual("mail11", self.ram.get_gender())

    def test_set_contact(self):
        self.ram.set_contact("98203011")
        self.assertEqual("98203011", self.ram.get_contact())

    def test_get_contact(self):
        self.assertEqual("98203011", self.ram.get_contact())

    def test_set_dob(self):
        self.ram.set_dob("1990-02-9")
        self.assertEqual("1990-02-9", self.ram.get_dob())

    def test_get_dob(self):
        self.assertEqual("1990-02-9", self.ram.get_dob())

    def test_set_address(self):
        self.ram.set_address("sarlahi11")
        self.assertEqual("sarlahi11", self.ram.get_address())


    def test_get_address(self):
        self.assertEqual("sarlahi11", self.ram.get_address())

    def tearDown(self):
        '''Hook method for deconstructing the test fixture after testing it.'''
        self.ram = None
