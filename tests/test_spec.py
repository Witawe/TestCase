from main import Specialization
from classes.institute import Institute
import unittest

class TestAddSpec(unittest.TestCase):
    def test_one(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        inst = Institute()
        #with self.assertRaises(Exception):
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_two(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Информатика и вычислительная техника')
        inst = Institute()
        #with self.assertRaises(Exception):
        inst.add_spec(sp)
        inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)
'''
    def test_three(self):
        sp = Specialization('')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_four(self):
        sp = Specialization()
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_five(self):
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Фундаментальная информатика и информационные технологии')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
            inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)

    def test_six(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(21)
        self.assertEqual(len(inst.specs), 1)
'''

if __name__ == "__main__":
    unittest.main()