import unittest
from Frontend.dashboard import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.data = [111, 'vivek', 'Purbe', 'aaa', '9852045', '2020-2-02', 'Ktm']
        self.data2 = [1, 4, 6, 11, 345, 6, 3322, 45]
        self.data3 = [1, 4, 6, 6, 11, 45, 345, 3322]
        self.o = Student()

    def test_search_data(self):
        expect = 11
        actual = self.o.binarysearch(self.data2, 11)
        self.assertEqual(expect, actual)

    def test_sorting(self):
        expected = self.data3
        actual = self.o.bubblesort_asc(self.data2)
        self.assertEqual(expected, actual)
