from main import Subject, Specialization
from classes.institute import Institute
from classes.getSubject import getSubject
import unittest

class TestAddSubject(unittest.TestCase):
    def test_one(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec)
        inst = Institute()
        inst.add_subject(sub)
        self.assertEqual(len(inst.subjects), 1)

    def test_two(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec)
        sub1 = Subject('Б1.В.03', 'Базы данных NoSQL', 2, 108, spec)
        inst = Institute()
        inst.add_subject(sub)
        inst.add_subject(sub1)
        self.assertEqual(len(inst.subjects), 2)

    def test_three(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec)
        spec1 = Specialization('Информатика и вычислительная техника')
        sub1 = Subject('Б1.В.03', 'Базы данных NoSQL', 2, 108, spec1)
        inst = Institute()
        inst.add_subject(sub)
        inst.add_subject(sub1)
        self.assertEqual(len(inst.subjects), 2)
'''
    def test_four(self):
        spec = Specialization('')
        sub = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(sub)
        self.assertEqual(len(inst.subjects), 0)

    def test_five(self):
        sub = Subject('Б1.О.07', 'Машинное обучение', 2, 288, 12)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(sub)
        self.assertEqual(len(inst.subjects), 0)

    def test_six(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('', '', 0, 0, spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(sub)
        self.assertEqual(len(inst.subjects), 0)

    def test_seven(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.О.09', 'Машинное обучение', 2, 288, spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(sub)
        self.assertEqual(len(inst.subjects), 0)

    def test_eight(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec)
        sub1 = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(sub)
            inst.add_subject(sub1)
        self.assertEqual(len(inst.subjects), 0)

    def test_nine(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.О.07', 'Машинное обучение', '2', '288', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(sub)
        self.assertEqual(len(inst.subjects), 0)

    def test_nine(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject(123, 1123, '2', '288', spec)
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(sub)
        self.assertEqual(len(inst.subjects), 0)

    def test_ten(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_subject(123)
        self.assertEqual(len(inst.subjects), 0)
'''

class TestGetSubject(unittest.TestCase):
    def test_1(self): #correct
        g_subject = getSubject("../data/2семестр.xlsx", "Межкультурная коммуникация в профессиональной деятельности")
        self.assertEqual("Б1.О.02", g_subject.code)
        self.assertEqual("Межкультурная коммуникация в профессиональной деятельности", g_subject.name)
        self.assertEqual(2, g_subject.semestr)
        self.assertEqual(72, g_subject.hours)
        self.assertEqual("ФИИТ", g_subject.specialization.name)

    def test_2(self):
        g_subject = getSubject("../data/2семестр.xlsx", None)
        with self.assertRaises(Exception):
            getSubject(g_subject)

    def test_3(self):
        g_subject = getSubject("../data/2семестр.xlsx", "")
        with self.assertRaises(Exception):
            getSubject(g_subject)

    def test_4(self):
        g_subject = getSubject("../data/2семестр.xlsx", 123123)
        with self.assertRaises(Exception):
            getSubject(g_subject)

if __name__ == "__main__":
    unittest.main()