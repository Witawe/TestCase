from main import Exam, Subject, Specialization
from classes.institute import Institute
from classes.getExam import getExam
from datetime import date
import unittest

class TestAddExam(unittest.TestCase):
    def test_one(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.О.07', 'Методы тестирования и верификации программных продуктов', 2, 288, spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        inst.add_exam(exam)
        #self.assertEqual(len(inst.exams), 1)

    def test_two(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        spec1 = Specialization('Информатика и вычислительная техника')

        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        sub1 = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec1)

        data = date(2021, 1, 1)
        data1 = date(2021, 1, 3)

        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        exam1 = Exam(sub1, data1, '2021-2022', 'Эверстов Владимир Васильевич')

        inst = Institute()
        inst.add_exam(exam)
        inst.add_exam(exam1)
        #self.assertEqual(len(inst.exams), 1)

    def test_three(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        spec1 = Specialization('Информатика и вычислительная техника')

        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        sub1 = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec1)

        data = date(2021, 1, 1)
        data1 = date(2021, 1, 3)

        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        exam1 = Exam(sub1, data1, '2021-2022', 'Григорьев Александр Виссарионович')

        inst = Institute()
        inst.add_exam(exam)
        inst.add_exam(exam1)
        #self.assertEqual(len(inst.exams), 1)

    def test_four(self): #correct
        spec = Specialization('Фундаментальная информатика и информационные технологии')

        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        sub1 = Subject('Б1.О.07', 'Машинное обучение', 2, 288, spec)

        data = date(2021, 1, 1)
        data1 = date(2021, 1, 3)

        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        exam1 = Exam(sub1, data1, '2021-2022', 'Григорьев Александр Виссарионович')

        inst = Institute()
        inst.add_exam(exam)
        inst.add_exam(exam1)
        #self.assertEqual(len(inst.exams), 1)
'''
    def test_five(self):
        spec = Specialization('')
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_six(self):
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, 12)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_seven(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('', '', 2, 108, spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_eight(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject(123, 123, 2, 108, spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_nine(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', '2', '108', spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_ten(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        data = date(2029, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_eleven(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', '')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_eleven(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_twelve(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        data = date(2021, 1, 1)
        exam = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        exam1 = Exam(sub, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
            inst.add_exam(exam1)
        self.assertEqual(len(inst.exams), 0)

    def test_thirteen(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(123)
        self.assertEqual(len(inst.exams), 0)

    def test_fourteen(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        sub = Subject('Б1.В.02', 'Методы тестирования и верификации программных продуктов', 2, 108, spec)
        exam = Exam(sub, 123, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)

    def test_fiveteen(self):
        spec = Specialization('Фундаментальная информатика и информационные технологии')
        data = date(2021, 1, 1)
        exam = Exam(123, data, '2021-2022', 'Эверстов Владимир Васильевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 0)
'''

class TestGetExam(unittest.TestCase):
    def test_1(self):
        g_exam = getExam("../data/Экзамены.xlsx", "Б-ФИИТ-18", "Основы программирования", date(2018, 1, 10))
        #self.assertEqual()

    def test_2(self):
        g_exam = getExam("../data/Экзамены.xlsx", "", "Основы программирования", date(2018, 1, 10))
        with self.assertRaises(Exception):
            getExam(g_exam)

    def test_3(self):
        g_exam = getExam("../data/Экзамены.xlsx", None, "Основы программирования", date(2018, 1, 10))
        with self.assertRaises(Exception):
            getExam(g_exam)

    def test_4(self):
        g_exam = getExam("../data/Экзамены.xlsx", "Б-ФИИТ-18", "", date(2018, 1, 10))
        with self.assertRaises(Exception):
            getExam(g_exam)

    def test_5(self):
        g_exam = getExam("../data/Экзамены.xlsx", "Б-ФИИТ-18", None, date(2018, 1, 10))
        with self.assertRaises(Exception):
            getExam(g_exam)

    def test_6(self):
        g_exam = getExam("../data/Экзамены.xlsx", "Б-ФИИТ-18", "Основы программирования", "")
        with self.assertRaises(Exception):
            getExam(g_exam)

    def test_7(self):
        g_exam = getExam("../data/Экзамены.xlsx", "Б-ФИИТ-18", "Основы программирования", None)
        with self.assertRaises(Exception):
            getExam(g_exam)

    def test_8(self):
        g_exam = getExam("../data/Экзамены.xlsx", "Б-ФИИТ-82", 12312, None)
        with self.assertRaises(Exception):
            getExam(g_exam)

    def test_8(self):
        g_exam = getExam("../data/Экзамены.xlsx", 123123, "Основы программирования", date(2018, 1, 10))
        with self.assertRaises(Exception):
            getExam(g_exam)

if __name__ == "__main__":
    unittest.main()