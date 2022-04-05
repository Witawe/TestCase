from main import Specialization
from classes.institute import Institute
from classes.getSpec import getSpecialization
import unittest

class TestAddSpec(unittest.TestCase):
    def test_one(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        inst = Institute()
        inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 1)

    def test_two(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Информатика и вычислительная техника')
        inst = Institute()
        inst.add_spec(sp)
        inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 2)
'''
    def test_three(self):
        sp = Specialization('')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 0)

    def test_four(self):
        sp = Specialization('')
        inst = Institute('')
        with self.assertRaises(Exception):
            inst.add_spec(sp)
        self.assertEqual(len(inst.specs), 0)

    def test_five(self):
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Фундаментальная информатика и информационные технологии')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec(sp)
            inst.add_spec(sp1)
        self.assertEqual(len(inst.specs), 0)

    def test_six(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_spec('')
        self.assertEqual(len(inst.specs), 1)
'''

class TestGetSpec(unittest.TestCase):
    def test_1(self): #correct
        g_spec = getSpecialization("../data/Специализация.xlsx", "ДУ")
        self.assertEqual("Математика (Дифференциальные уравнения,оптимальное управление и аналитика)", g_spec.name)

    def test_2(self):
        g_spec = getSpecialization("../data/Специализация.xlsx", None)
        with self.assertRaises(Exception):
            getSpecialization(g_spec)

    def test_3(self):
        g_spec = getSpecialization("../data/Специализация.xlsx", "")
        with self.assertRaises(Exception):
            getSpecialization(g_spec)

    def test_4(self):
        g_spec = getSpecialization("../data/Специализация.xlsx", 354652)
        with self.assertRaises(Exception):
            getSpecialization(g_spec)

    def test_5(self):
        g_spec = getSpecialization("../data/Специализация.xlsx", "Математика (Дифференциальные уравнения,оптимальное управление и аналитика)")
        with self.assertRaises(Exception):
            getSpecialization(g_spec)

if __name__ == "__main__":
    unittest.main()