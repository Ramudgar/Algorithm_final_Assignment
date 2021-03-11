import unittest

from Backend.dbconnection import DBConnect


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.dbObj = DBConnect()
        self.values = (1, 'ramudgar', 'ram@gmail.com')

    def test_create_db(self):
        query = "create database test_final_algorithm"
        actual = self.dbObj.create(query)
        self.assertIsNone(actual)

    def test_create_tbl(self):
        use_db_query = "use test_final_algorithm"
        exe_db_query = self.dbObj.create(use_db_query)
        self.assertIsNone(exe_db_query)

        query = "create table test_student(test_roll_no int NOT NULL, test_name varchar(40), test_email " \
                "varchar(100));"
        actual = self.dbObj.create(query)
        self.assertIsNone(actual)


    def test_insert_student_data(self):
        use_db_query = "use test_final_algorithm"
        exe_db_query = self.dbObj.create(use_db_query)
        self.assertIsNone(exe_db_query)

        query1 = "insert into test_student(test_roll_no, test_name, test_email) values (%s,%s,%s)"
        self.dbObj.insert(query1,self.values)

        query2 = "select * from test_student where test_roll_no = 1"
        actual = self.dbObj.selectall(query2)
        expected = [(1, 'ramudgar', 'ram@gmail.com'),]
        self.assertEqual(expected,actual)
