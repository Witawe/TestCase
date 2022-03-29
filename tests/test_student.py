from main import Student
from classes.institute import Institute
import unittest

class TestAddStudent(unittest.TestCase):
    def test_one(self): #correct
        stud = Student('185775','Луковцев Алексей Владимирович')
        inst = Institute()
        inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_two(self): #correct
        stud = Student('185775', 'Луковцев Алексей Владимирович')
        stud1 = Student('199995', 'Иванов Иван Иванович')
        inst = Institute()
        inst.add_stud(stud)
        inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 0)
'''
    def test_three(self):
        stud = Student('','')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_four(self):
        stud = Student('Луковцев Алексей Владимирович', '185775')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_five(self):
        stud = Student()
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_six(self):
        stud = Student('185775','Луковцев Алексей Владимирович')
        stud1 = Student('185775','Луковцев Алексей Владимирович')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 1)

    def test_seven(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(123)
        self.assertEqual(len(inst.students), 1)

    def test_eight(self):
        stud = Student('185775','185775')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_nine(self):
        stud = Student('Луковцев Алексей Владимирович','сто')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_ten(self):
        stud = Student('Луковцев Алексей Владимирович', '185775')
        stud1 = Student('Иванов Иван Иванович', '185775')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 2)

    def test_eleven(self):
        stud = Student('Луковцев Алексей Владимирович', '185775')
        stud1 = Student('Луковцев Алексей Владимирович', '199995')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 2)
'''

if __name__ == "__main__":
    unittest.main()